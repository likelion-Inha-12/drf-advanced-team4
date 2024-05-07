from django.contrib import admin
from django.urls import path
from . import *
from .views import *

urlpatterns = [
    path('assignments/', AssignmentCreateAPIView.as_view(), name='assignment-create'),
    path('submissions/', SubmissionCreateAPIView.as_view(), name='submission-create'),
    path('assignments/', AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', AssignmentRetrieveAPIView.as_view(), name='assignment-detail'),
    
]