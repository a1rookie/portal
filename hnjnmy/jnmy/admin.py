from django.contrib import admin
from .models import Carousel, HtmlDesign, News, Products, ProductImage, Newstitle, Video



admin.AdminSite.site_header ='河南金农草业发展有限公司'
admin.AdminSite.site_title = '金农草业'

admin.site.disable_action('delete_selected')

class AdminFormTinyMCE(admin.ModelAdmin):
    class Media:
        js=(
            "https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js",
            "/static/tinymce/js/tinymce/jquery.tinymce.min.js",
            "/static/tinymce/js/tinymce/tinymce.min.js",
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',
            "/static/tinymce/js/tinymce/textarea.js",
        )


class ProductsImageInline(admin.StackedInline):
    model = ProductImage
    extra = 2


class ProductAdmin(AdminFormTinyMCE):
    fields = ['species', 'name', 'image', 'video', 'detail']
    inlines = [ProductsImageInline]


class VideoAdmin(AdminFormTinyMCE):
    fields = ['video']


class NewstitleAdmin(AdminFormTinyMCE):
    fields = ['name']


class NewsAdmin(AdminFormTinyMCE):
    fields = ['title',"type", "content", "image"]


class HtmlAdmin(AdminFormTinyMCE):
    fields = ['name','slug','parent_category', 'content']


admin.site.register(Carousel,AdminFormTinyMCE)
admin.site.register(Video, VideoAdmin)
admin.site.register(HtmlDesign,HtmlAdmin)
admin.site.register(Products,ProductAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Newstitle, NewstitleAdmin)
