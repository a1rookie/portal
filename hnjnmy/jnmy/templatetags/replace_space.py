from django import template

register = template.Library()


# 去除空格
@register.filter(name='cut')
def cut(value, arg):
   return value.replace(arg, '')