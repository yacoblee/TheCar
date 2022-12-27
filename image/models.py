from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image_img = models.ImageField(blank=True, upload_to="image/%y/%m/%d", default='image/no_image.png')
    title = models.TextField(null=True, blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-updated']

    # 작성자의 이름과 글 작성일을 합친 문자열 반환
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    # 상세페이지 주소 반환 메서드, 객체이동 주소 호출, 상세화면 이동링크만들때 호출
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.author)])