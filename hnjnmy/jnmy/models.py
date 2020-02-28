from django.db import models
import os
from bs4 import BeautifulSoup
from django.conf import settings
from datetime import datetime

# Create your models here.


# 轮播图
class Carousel(models.Model):
    image = models.ImageField("轮播图",upload_to='./carousel',blank=True,null=True)
    time = models.DateTimeField("创建日期",auto_now=True)

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = "轮播图"

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete()

    def __str__(self):
        return self.image.name


# 页面设计
class HtmlDesign(models.Model):
    name = models.CharField('分类名', max_length=30, unique=True)
    slug = models.SlugField(default='no-slug', max_length=160, blank=True)
    created_time = models.DateTimeField('创建时间', auto_now=True)
    parent_category = models.ForeignKey('self', verbose_name="父级分类", blank=True, null=True,
                                        on_delete=models.CASCADE)
    content = models.TextField("标题内容", default="")

    class Meta:
        ordering = ['name']
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 视频
class Video(models.Model):
    video = models.FileField("视频", upload_to='./video', default=None)
    time = models.DateTimeField("创建时间",auto_now=True)
    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


# 资讯新闻
class News(models.Model):
    title = models.CharField("标题", max_length=100, default="")
    content = models.TextField("文章内容", default="")
    image = models.ImageField("资讯封面图", upload_to='./news', blank=True, null=True, default=None)
    time = models.DateTimeField("发布时间",auto_now=True)
    type = models.CharField("新闻类型", max_length=10, default="公司动态")

    def delete(self, using=None, keep_parents=False):
        soup = BeautifulSoup(self.content,'lxml')
        imgs = soup.find_all('img')
        for img in imgs:
            if img.get('src').split(':')[0] == "data":
                pass
            else:
                path = settings.MEDIA_ROOT+'/content/'+ img.get('src').split('/')[-1]
                os.remove(path)
        os.remove(self.image.path)
        super().delete()

    class Meta:
        verbose_name = "资讯"
        verbose_name_plural = "资讯"

    def __str__(self):
        return self.type


# 资讯菜单
class Newstitle(models.Model):
    name = models.CharField("菜单栏", max_length=15, default="")

    class Meta:
        verbose_name = "资讯菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 商品详情
class Products(models.Model):
    species = models.CharField("产品分类", max_length=10)
    name = models.CharField("产品名称", max_length=100)
    time = models.DateTimeField(auto_now=True)
    detail = models.TextField("文章内容", default="")
    count = models.IntegerField("浏览量",default=0)
    image = models.ImageField("产品展示图", upload_to='./products', default=None)
    video = models.FileField("视频", upload_to='./productsvideo', blank=True, null=True, default=None)
    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"

    def delete(self, using=None, keep_parents=False):
        soup = BeautifulSoup(self.detail,'lxml')
        imgs = soup.find_all('img')
        for img in imgs:
            path = settings.MEDIA_ROOT+'/content/'+img.get('src').split('/')[-1]
            os.remove(path)
        img = ProductImage.objects.all().filter(product__id=self.id)
        for one in img:
            os.remove(one.image.path)
        super().delete()

    def __str__(self):
        return self.name


# 商品图片
class ProductImage(models.Model):
    image = models.FileField("产品图",upload_to='./products', default=None)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    time = models.DateTimeField("创建日期", auto_now=True)

    class Meta:
        verbose_name = "产品图"
        verbose_name_plural = "产品图"



