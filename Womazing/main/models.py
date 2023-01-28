from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.


class Size(models.Model):
    name = models.CharField(max_length=10,verbose_name="Размер")


    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Размер"
        verbose_name_plural="Размеры"

class Color(models.Model):
    name = models.CharField(max_length=16, verbose_name='Цвет')

  
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Цвет"
        verbose_name_plural="Цвета"

class Type(models.Model):
    name = models.CharField(max_length=120, verbose_name='Вид')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Вид"
        verbose_name_plural="Виды"

class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name="Название продукта")
    discripton = models.CharField(max_length=300,verbose_name="Описание Продукта")
    size = models.ManyToManyField(Size,verbose_name="Размеры продукта")
    color = models.ManyToManyField(Color,verbose_name="Цвета продукта")
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    price= models.IntegerField(verbose_name='Цена(Р)')

    def __str__(self):
        return self.name

    def display_color(self):
        return ', '.join(color.name for color in self.color.all()) 
    display_color.short_description = 'Цвета'

    def display_size(self):
        return ', '.join(size.name for size in self.size.all()) 
    display_size.short_description = 'Размеры'

    def get_absolute_url(self):
        return reverse('product', kwargs={'id' : self.id})


    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"

class Basket(models.Model):
    colorProduct = models.CharField(max_length=30, verbose_name='Цвет продукта')
    sizeProduct = models.CharField(max_length=10, verbose_name='Размер продукта')
    id_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    countProduct = models.IntegerField(default=1)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    priceProduct = models.IntegerField(default=0)

    class Meta:
        verbose_name="Корзину"
        verbose_name_plural="Корзины"