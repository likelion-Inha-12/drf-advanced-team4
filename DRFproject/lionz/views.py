from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse, HttpResponse
from .models import *
from .serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
#.serializers , REST프레임워크 import 추가 필요

# Create your views here.

# 고려해야 할 점 1) assgiment를 post 할 때 카테고리가 없으면 카테고리를 생성하고, 있으면 해당 카테고리에 추가해야함
# 고려해야 할 점 2) be,fe,all에 따라 파트를 구분하는 로직이 필요함

# API 응답 포맷을 표준화하는 함수
def api_response(data, message, status_code):
    response = {
        "message": message,
        "data": data
    }
    return Response(response, status=status_code)

class AssignmentCreateAPIView(generics.CreateAPIView):
    queryset = Assignment.objects.all()  #
    serializer_class = AssignmentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return api_response(data=response.data, message=f"{response.data['id']}번 과제가 성공적으로 생성되었습니다.", status_code=status.HTTP_201_CREATED)

class SubmissionCreateAPIView(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return api_response(data=response.data, message="제출물이 성공적으로 생성되었습니다.", status_code=status.HTTP_201_CREATED)


class AssignmentListAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs) #요 다음에 정보 필터링 해야 하는 로직 추가되어야 할 것 같아요!
        return api_response(data=response.data, message="과제 목록 조회 성공", status_code=status.HTTP_200_OK)


class AssignmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return api_response(data=response.data, message="특정 과제 조회 성공", status_code=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)  # partial=True로 설정하여 부분 업데이트를 지원
        response = super().update(request, partial=partial, *args, **kwargs)
        return api_response(data=response.data, message="특정 과제 수정 성공", status_code=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()  # 과제 인스턴스를 불러옵니다.
        instance_id = instance.id  # 과제의 ID를 저장합니다.
        self.perform_destroy(instance)
        # 과제 삭제 후, ID를 포함한 메시지를 반환합니다.
        return Response({'message': f'과제 ID {instance_id}번이 성공적으로 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        submissions = Submission.objects.filter(assignment_id=instance.id)
        submissions.delete()  # 연관된 제출물 모두 삭제
        instance.delete()  # 과제 삭제


class AssignmentFilterAPIView(generics.ListAPIView):
    serializer_class = AssignmentViewSerializer

    def get_queryset(self):
        queryset = Assignment.objects.all()

        if 'part' in self.request.query_params:
            part = self.request.query_params.get('part')
            queryset = queryset.filter(part = part)

        if 'category' in self.request.query_params:
            category = self.request.query_params.get('category')
            queryset = queryset.filter(category = category)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return api_response(data=serializer.data, message="과제 조회 성공", status_code=status.HTTP_200_OK)