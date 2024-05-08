from django.db import models

class Member(models.Model): # Member 모델 정의
    name = models.CharField(max_length=20) # 멤버 이름 저장

class Category(models.Model): #카테고리 모델
    name = models.CharField(max_length=20) #카테고리 이름, 중복 불가능

class Assignment(models.Model): # 과제 생성 모델
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 
    #과제 : 카테고리 = 1:N 관계 설정, 카테고리가 삭제되도 과제는 삭제 x 카테고리만 NULL로 바뀜
    title = models.CharField(max_length=50) #제목
    created_at = models.DateTimeField(auto_now_add=True) #생성일자
    deadline = models.DateTimeField() #마감일자
    part = models.CharField(max_length=3, choices=[
    ('BE', 'BE'),
    ('FE', 'FE'),
    ('ALL', 'All')
    ])
    content = models.TextField() #과제 내용
    githubUrl = models.URLField() #github 주소


class Submission(models.Model):
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE,related_name='submissions')
    # 과제:제출물 = 1:N 관계 설정, 과제가 삭제되면 제출물도 삭제
    content = models.TextField() #제출물 내용
    githubUrl = models.URLField() #github 주소
    created_at = models.DateTimeField(auto_now_add=True) #생성일자(제출일자)





