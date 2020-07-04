from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):

    # 为属性字段定义类型（文本？数字？字符？日期？与另一个对象的关联关系？）
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # 与另一个对象的连接
    title = models.CharField(max_length=200)  # 用字符定义文本
    text = models.TextField()  # 没有长度限制的文本
    create_date = models.DateTimeField(default=timezone.now)  # 时间和日期
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

