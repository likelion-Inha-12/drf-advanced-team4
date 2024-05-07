from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
from .serializers import AssignmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
#.serializers , REST프레임워크 import 추가 필요

# Create your views here.

# 고려해야 할 점 1) assgiment를 post 할 때 카테고리가 없으면 카테고리를 생성하고, 있으면 해당 카테고리에 추가해야함
# 고려해야 할 점 2) be,fe,all에 따라 파트를 구분하는 로직이 필요함