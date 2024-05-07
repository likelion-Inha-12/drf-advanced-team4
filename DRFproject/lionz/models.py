from django.db import models

class Member(models.Model): # Member 모델 정의
    name = models.CharField(max_length=20) # 멤버 이름 저장

class Category(models.Model): #카테고리 모델``
    name = models.CharField(max_length=20,unique=True) #카테고리 이름, 중복 불가능


class Assignment(models.Model): # 과제 생성 모델
    catagory_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 
    #과제 : 카테고리 = 1:N 관계 설정, 카테고리가 삭제되도 과제는 삭제 x 카테고리만 NULL로 바뀜
    title = models.CharField(max_length=50) #제목
    created_at = models.DateTimeField(auto_now_add=True) #생성일자
    deadline = models.DateTimeField() #마감일자
    # part로 모델을 따로 만들었다가,3개의 파트로 과제가 분류만 되면 되니 과제 모델 안에 넣어도 무방할 것 같아서
    #이렇게 구현하고 view에서는 filter 메소드 통해서 구분하는 방법으로 생각해봤습니다. 
    # 이부분은 확인하시고 피드백해주세요!!
    part = models.CharField(max_length=3, choices=[
    ('BE', 'BE'),
    ('FE', 'FE'),
    ('ALL', 'All')
    ])
    catagory_id = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='assignments')
    # 카테고리:과제 = 1:N 관계 설정
    content = models.TextField() #과제 내용
    githubUrl = models.URLField() #github 주소


class Submission(models.Model):
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE,related_name='submissions')
    # 과제:제출물 = 1:N 관계 설정, 과제가 삭제되면 제출물도 삭제
    content = models.TextField() #제출물 내용
    githubUrl = models.URLField() #github 주소
    created_at = models.DateTimeField(auto_now_add=True) #생성일자(제출일자)





