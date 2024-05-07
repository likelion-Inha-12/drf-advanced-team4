from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('assignments/create/', AssignmentCreateAPIView.as_view(), name='assignment-create'),
    path('submissions/create/', SubmissionCreateAPIView.as_view(), name='submission-create'),
    path('assignments/list/', AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignments/detail/<int:pk>/', AssignmentRetrieveAPIView.as_view(), name='assignment-detail'),
    path('assignments/update/', updateAssignment, name='assignment-update'),
    path('assignments/delete/<int:pk>/', deleteAssignment, name='assignment-delete'),
    path('assignments/part/', AssignmentListAPIView.as_view({'get': 'get_serializer_part'}), name='assignment-list-part'),  # get_serializer_part 함수 연결
    path('assignments/category/', AssignmentListAPIView.as_view({'get': 'get_serializer_category'}), name='assignment-list-category'),  # get_serializer_category 함수 연결
]