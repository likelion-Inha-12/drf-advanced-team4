from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('assignments', AssignmentCreateAPIView.as_view(), name='assignment-create'),
    path('submissions', SubmissionCreateAPIView.as_view(), name='submission-create'),
    path('assignments/all', AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>', AssignmentRetrieveUpdateDestroyAPIView.as_view(), name='assignment-detail'),
    path('assignments/part', AssignmentPartAPIView.as_view(), name='assignment-part-list'),
    path('assignments/category', AssignmentCategoryAPIView.as_view(), name='assignment-category-list'),
]