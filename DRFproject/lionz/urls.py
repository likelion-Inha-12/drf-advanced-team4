from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('assignments', AssignmentCreateAPIView.as_view(), name='assignment-create'),
    path('submissions/create/', SubmissionCreateAPIView.as_view(), name='submission-create'),
    path('assignments/list/', AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignments/detail/<int:pk>/', AssignmentRetrieveAPIView.as_view(), name='assignment-detail'),
    path('assignments/update/', updateAssignment, name='assignment-update'),
    path('assignments/delete/<int:pk>/', deleteAssignment, name='assignment-delete'),
    path('assignments/part/', AssignmentPartAPIView.as_view(), name='assignment-part-list'),
    path('assignments/category/', AssignmentCategoryAPIView.as_view(), name='assignment-category-list'),
]