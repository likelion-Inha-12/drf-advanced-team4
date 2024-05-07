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

class AssignmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return api_response(data=response.data, message="특정 과제 조회 성공", status_code=status.HTTP_200_OK)


@api_view(['PUT'])
def updateAssignment(request, pk): # 과제 수정 API
    assignment = get_object_or_404(Assignment, pk=pk)
    serializer = AssignmentSerializer(assignment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignmentDeleteView(generics.DestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # 연관된 제출물 삭제
        submissions = Submission.objects.filter(assignment_id=instance)
        for submission in submissions:
            submission.delete()
        
        # 과제 삭제
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssignmentPartAPIView(generics.ListAPIView):
    serializer_class = AssignmentViewSerializer

    def get_queryset(self):
        part = self.request.data.get('part')
        return Assignment.objects.filter(part=part)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return api_response(data=serializer.data, message="과제 조회 성공", status_code=status.HTTP_200_OK)

class AssignmentCategoryAPIView(generics.ListAPIView):
    serializer_class = AssignmentViewSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        return Assignment.objects.filter(category=category)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return api_response(data=serializer.data, message="과제 조회 성공", status_code=status.HTTP_200_OK)