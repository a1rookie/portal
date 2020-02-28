from django.urls import path
from . import views


urlpatterns = [
    path('upload/',views.upload_img,name='upload'),
    path('',views.index,name="index"),
    path('news/',views.news,name="news"),
    path('index/', views.info, name="info"),
    path('show/<int:new_id>/',views.show,name="show"),
    path('detail/', views.product_detail, name="detail"),
    path('introduce/<int:id>', views.introduce, name='introduce'),
    path('new_detail/',views.new_detail,name='new_detail'),
    path('zhanshi/',views.zhanshi,name='zhanshi'),
]