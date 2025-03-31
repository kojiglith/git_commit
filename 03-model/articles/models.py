from django.db import models

# Create your models here.

# 게시글이 저장될 테이블을 설계하는 클래스
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
