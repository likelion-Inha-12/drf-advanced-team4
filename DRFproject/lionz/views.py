from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse, HttpResponse
from .models import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
#.serializers , REST프레임워크 import 추가 필요

# Create your views here.

# 고려해야 할 점 1) assgiment를 post 할 때 카테고리가 없으면 카테고리를 생성하고, 있으면 해당 카테고리에 추가해야함
# 고려해야 할 점 2) be,fe,all에 따라 파트를 구분하는 로직이 필요함

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
        
        serializer = AssignmentSerializer(Assigment, data=modified_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

