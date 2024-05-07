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
        return api_response(data=response.data, message="과제가 성공적으로 생성되었습니다.", status_code=status.HTTP_201_CREATED)

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
        response = super().list(request, *args, **kwargs)
        return api_response(data=response.data, message="과제 목록 조회 성공", status_code=status.HTTP_200_OK)

class AssignmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return api_response(data=response.data, message="특정 과제 조회 성공", status_code=status.HTTP_200_OK)

def changeAssignment(request): # 5. 특정 과제 내용 수정하기
    if request.method == 'PUT':
        modified_data = {} # 수정된 데이터 포함할 빈 딕셔너리 생성

        if 'title' in request.data: # 제목 수정 데이터
            modified_data['title'] = request.data.get('title')
        if 'githubUrl' in request.data: # 깃허브링크 수정 데이터
            modified_data['githubUrl'] = request.data.get('githubUrl')
        if 'deadline' in request.data: # 마감일자 수정 데이터
            modified_data['deadline'] = request.data.get('deadline')
        if 'content' in request.data: # 내용 수정 데이터
            modified_data['content'] = request.data.get('content')
        
        serializer = AssignmentSerializer(Assignment, data=modified_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return api_response(data=serializer.data, message="과제가 성공적으로 수정되었습니다.", status_code=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteAssignment(request, pk): # 6. 특정 과제 삭제
    if request.method == 'DELETE':
        assignment = get_object_or_404(Assignment, pk = pk) # 삭제할 과제 불러옴

        submissions = Submission.objects.filter(assignment) # 삭제할 과제와 연관된 제출물 필터링

        for submission in submissions: # 해당 제출물들 삭제
            submission.delete()

        assignment.delete() # 해당 과제 삭제

        return api_response(data=None, message=f"id: {pk}번 과제 삭제 성공", status_code=status.HTTP_200_OK)


  
