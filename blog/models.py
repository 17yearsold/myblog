from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tags'
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=20)
    body = models.TextField()
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('最后发布')
    summary = models.CharField('简介', max_length=200, blank=True)
    categories = models.ForeignKey(Category, verbose_name='分类', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        db_table = 'articles'
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)
