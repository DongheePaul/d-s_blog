from django.conf import settings
from django.db import models
from uuid import uuid4
from django.utils import timezone
import os

#업로드될 이미지의 파일명을 난수로 변경해 리턴
def date_upload_to(instance, filename):
  # 길이 32 인 uuid 값
  uuid_name = uuid4().hex
  # 확장자 추출
  extension = os.path.splitext(filename)[-1].lower()
  filename_changed = uuid_name + extension
  # 결합 후 return
  return filename_changed


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    mainphoto = models.ImageField(blank=True, null=True, upload_to=date_upload_to)    
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()  # published_date 에 현재시간을 할당
        self.save()  # 변경된 데이터베이스를 저장


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete = models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text