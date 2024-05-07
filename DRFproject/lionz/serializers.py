from rest_framework import serializers
from .models import *
from datetime import datetime
from django.utils.timesince import timesince

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class AssignmentSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Assignment
        fields = ['category', 'title', 'created_at', 'deadline', 'part', 'content', 'githubUrl']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        assignment = Assignment.objects.create(category=category, **validated_data)
        return assignment
    

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['assignment_id', 'content', 'githubUrl', 'created_at']    

class AssignmentDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    submissions = SubmissionSerializer(many=True, read_only=True)
    remaining_time = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = ['title', 'created_at', 'part', 'category', 'deadline', 'content', 'submissions', 'remaining_time']

    def get_remaining_time(self, obj):
        if obj.deadline:
            now = datetime.now(obj.deadline.tzinfo)
            if obj.deadline > now:
                return timesince(now, obj.deadline) + ' 남았습니다'
            else:
                return '마감기한이 지났습니다.'
        return None

class AssignmentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'created_at', 'part']
