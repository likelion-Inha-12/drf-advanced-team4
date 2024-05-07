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

def changeAssignment(request): # 5. 특정 과제 내용 수정하기
    if request.method == 'PUT':
        modified_data = {} # 수정된 데이터 포함할 빈 딕셔너리 생성

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
