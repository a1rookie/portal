# Generated by Django 2.0.6 on 2018-07-20 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='./carousel', verbose_name='轮播图')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='HtmlDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='分类名')),
                ('slug', models.SlugField(blank=True, default='no-slug', max_length=160)),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('content', models.TextField(default='', verbose_name='标题内容')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jnmy.HtmlDesign', verbose_name='父级分类')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='标题')),
                ('content', models.TextField(default='', verbose_name='文章内容')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='./news', verbose_name='资讯封面图')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('type', models.CharField(default='公司动态', max_length=10, verbose_name='新闻类型')),
            ],
            options={
                'verbose_name': '资讯',
                'verbose_name_plural': '资讯',
            },
        ),
        migrations.CreateModel(
            name='Newstitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15, verbose_name='菜单栏')),
            ],
            options={
                'verbose_name': '资讯菜单',
                'verbose_name_plural': '资讯菜单',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default=None, upload_to='./products', verbose_name='产品图')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '产品图',
                'verbose_name_plural': '产品图',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=10, verbose_name='产品分类')),
                ('name', models.CharField(max_length=100, verbose_name='产品名称')),
                ('time', models.DateTimeField(auto_now=True)),
                ('detail', models.TextField(default='', verbose_name='文章内容')),
                ('count', models.IntegerField(default=0, verbose_name='浏览量')),
                ('image', models.ImageField(default=None, upload_to='./products', verbose_name='产品展示图')),
                ('video', models.FileField(blank=True, default=None, null=True, upload_to='./productsvideo', verbose_name='视频')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(default=None, upload_to='./video', verbose_name='视频')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jnmy.Products'),
        ),
    ]
