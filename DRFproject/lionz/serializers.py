from rest_framework import serializers
from .models import *

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assigment
        fields = '__all__'
