from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Assignment) #Assigment 모델 등록
admin.site.register(Submission) # Submission 모델 등록
admin.site.register(Member)
admin.site.register(Category)