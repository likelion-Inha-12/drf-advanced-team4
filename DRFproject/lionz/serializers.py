from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['category', 'title', 'created_at', 'deadline', 'part', 'content', 'githubUrl']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, _ = Category.objects.get_or_create(**category_data)
        assignment = Assignment.objects.create(category=category, **validated_data)
        return assignment
    

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['assignment_id', 'content', 'githubUrl', 'created_at']    

class AssignmentDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    submissions = SubmissionSerializer(many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = ['title', 'created_at', 'part', 'category', 'deadline', 'githubUrl', 'content', 'submissions']