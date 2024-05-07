from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('assignments/create/', AssignmentCreateAPIView.as_view(), name='assignment-create'),
    path('submissions/create/', SubmissionCreateAPIView.as_view(), name='submission-create'),
    path('assignments/list/', AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignments/detail/<int:pk>/', AssignmentRetrieveAPIView.as_view(), name='assignment-detail'),
]