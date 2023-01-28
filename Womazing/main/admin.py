from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.


# admin.site.register(Size)
# admin.site.register(Color)
# admin.site.register(Type)
# admin.site.register(Product)

@admin.register(Color)

class ColorAdmin(admin.ModelAdmin):
    list_display=["id","name"]

@admin.register(Type)

class TypeAdmin(admin.ModelAdmin):
    list_display=["id","name"]



@admin.register(Basket)

class BasketAdmin(admin.ModelAdmin):
    list_display=["id","colorProduct","sizeProduct","id_product_id","countProduct","user_id"]

@admin.register(Size)

class SizeAdmin(admin.ModelAdmin):
    list_display=["id","name"]

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','type','display_color','display_size','price','image_show']

    def image_show(self,obj):
        if obj.image:
            return mark_safe("<img src='{}' width='100'/>".format(obj.image.url))
        return 'none'
    image_show.__name__ = 'Картинка'

   