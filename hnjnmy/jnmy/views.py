from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import time
from PIL import Image
from django.conf import settings
from django.http import HttpResponse
from .models import HtmlDesign, News, Newstitle, Carousel, Products, ProductImage, Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pure_pagination import PageNotAnInteger,Paginator,EmptyPage
static_base = 'http://127.0.0.1:8000'
static_url = settings.MEDIA_URL  # 上传文件展示路径前缀
# Create your views here.


# 图片存储
@csrf_exempt
def upload_img(request):
    file = request.FILES['file']
    data = {
        'error':True,
        'path':'',
    }
    if file:
        timenow = int(time.time()*1000)
        timenow = str(timenow)
        try:
            img = Image.open(file)
            img.save(settings.MEDIA_ROOT + "/content/" + timenow + str(file))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps(data), content_type="application/json")
        imgUrl = static_url + 'content/' + timenow + str(file)
        data['error'] = False
        data['path'] = imgUrl
    return HttpResponse(json.dumps(data), content_type="application/json")


# 主页
def index(request):
    banners_images = Carousel.objects.all().order_by('time')
    classlists = HtmlDesign.objects.all().order_by('id')
    video = Video.objects.all().order_by('time')
    video = video[0]
    msg = News.objects.all().order_by('-time')
    first = msg[0]
    other = msg[1:5] if msg.count() > 0 else None
    return render(request, 'intro.html', {'banners_images': banners_images,'first':first,
                                         'other':other, 'classlists': classlists, 'video': video})


# 走进金农
def introduce(request, id):
    classlists = HtmlDesign.objects.all().order_by('id')
    content = classlists.get(id=id)
    if content.parent_category_id == 6 or id == 6:
        if content.id == 6:
            product_all = Products.objects.all()
        else:
            product_all = Products.objects.filter(species=content.name).all()
        product_list = []
        for thing in product_all:
            product_list.append([thing, ProductImage.objects.filter(product_id=thing.id)])
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(product_all, 4, request=request)
        news = p.page(page)
        return render(request, 'me5.html',
                      {'product_list': product_list, 'news': news, 'classlists': classlists})
    if content.parent_category_id == 7:
        newslist = News.objects.all().filter(type=content.name).order_by('-time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(newslist, 4, request=request)
        news = p.page(page)
        return render(request, 'nowslist.html', {'news': news, 'classlists': classlists})

    if content.parent_category_id == 8 or id == 8:
        return render(request, 'position.html', {'classlists': classlists, 'content': content})

    if content.parent_category_id == 9 or id == 9:
        return render(request, 'contact.html', {'classlists': classlists, 'content': content})
    return render(request, 'introduce.html', {'classlists': classlists, 'content': content})


# 基地展示
def zhanshi(request):
    classlists = HtmlDesign.objects.all().order_by('id')
    return render(request, 'zhanshi.html', {'classlists': classlists})


# 主页
def info(request):
    classlists = HtmlDesign.objects.all().order_by('id')
    return render(request, 'intro.html', {'classlists': classlists})


# 新闻
def news(request):
    classlists = HtmlDesign.objects.all().order_by('id')
    titles = Newstitle.objects.all()
    demo = []
    for title in titles:
        sky = News.objects.all().filter(type=title).order_by('-time')
        sky = sky[0:5]
        demo.append(sky)
    msg = News.objects.all().order_by('-time')
    first = msg[0]
    other = msg[:] if msg.count() > 0 else None
    return render(request, 'menu3.html',{'first':first,
                                         'other':other, 'classlists': classlists, 'demo': demo})


# 产品详情
def product_detail(request):
    classlists = HtmlDesign.objects.all().order_by('id')
    product_id = request.GET['product_id']
    text = Products.objects.get(id=product_id)
    text.count += 1
    text.save()
    image = ProductImage.objects.filter(product_id=product_id)
    return HttpResponse(json.dumps([text.name,text.time.strftime("%Y-%m-%d"),text.count,text.detail,[one.image.url for one in image]]))


# 新闻详情
def show(request, new_id):
    classlists = HtmlDesign.objects.all().order_by('id')
    if News.objects.count() > 1:
        article = News.objects.all().order_by('time')
        content = article.get(id=new_id)
        pre_new = article.filter(id__lt=new_id).first()
        next_new = article.filter(id__gt=new_id).first()
    else:
        content = News.objects.get(id=new_id)
        pre_new = None
        next_new = None
    return render(request,'news_info.html',{'content':content,
                                            'pre_new':pre_new,
                                            'next_new':next_new,
                                            'classlists': classlists})


def new_detail(request):
    news_id = request.GET['new_id']
    text = News.objects.all(id=news_id)
    return HttpResponse(json.dumps([text.title,text.time.strftime("%Y-%m-%d")]))
