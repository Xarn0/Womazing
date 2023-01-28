from django.shortcuts import render,redirect
from .models import *
from django.db.models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import math
import os











# Create your views here.

def index(request):
   
    try:
            product = Product.objects.order_by('-id')[:3]
            product2 = Product.objects.filter(type__name = "футболка")
            coun = Product.objects.aggregate(Min('price'))
            type11 = Product.objects.filter(type_id = 2)
            type1 = type11.latest('id')
            oldprice = Product.objects.values('price').order_by('-id')[:3]
            ul = []
            proe = 0  
            arr = []
            rov = 0
            for i in oldprice:
                    
                    ul.append(math.trunc(int(i['price'])*1.4)) 
                    proe+=1
                    
           
        
            for y in product:
                    arr.append({
                        'name': y.name,
                        'price': y.price,
                        'image': y.image,
                        'oldprice': ul[rov]
                    } ) 
            rov+=1
    
   
   

    except:
        print()
        arr = ''
    return render(request,'main/main.html',{'product':arr})

def aboutBrand(request):
    return render(request,'main/About_brand.html')

def basket(request):
    basketUser = Basket.objects.filter( user_id_id = request.user.id)#поменяй на текущего пользователя
    id_product = []
    content_product = []
    price_basket = []
    count_basket = []
    id_basket = []
    i = 0
    y = 0
    x = 0
    basketSumm = 0
    coupon = False
   
    for item in basketUser:
        id_product.append(item.id_product.id) 
    if request.POST:
     
        try:
                idCounta = request.POST.get('countElementId')
                idCounta = int(idCounta)
                updata = Basket.objects.get(pk=idCounta)
                updata.countProduct = request.POST.get('countElement')
                updata.save()
                return redirect("basket")
        except:
                idCounta =None

        print(idCounta)
        if request.POST.get('deleteEl'):
            try:
                delet = request.POST.get('deleteEl')
                Basket.objects.get(pk = delet).delete()
                return redirect('basket')
            except:
                 delet = None
   

    for element in id_product:
            product = Product.objects.filter(id = element)
            for pr in product:
               
                content_product.append({
                                    'image': pr.image,
                                    'name' : pr.name
                                        })
       
    for price in  basketUser:
        price_basket.append(price.priceProduct) 

    for count in  basketUser:
        count_basket.append(count.countProduct) 

    for basketId in basketUser:
        id_basket.append(basketId.id) 

    for it in content_product:
        it['price'] = 0
        it['count'] = 0
        it['id'] = 0
        
    for iy in  price_basket:
        content_product[i]['price'] = iy
        i+=1
    
    for ix in  count_basket:
        content_product[y]['count'] = ix
        y+=1

    for it in  id_basket:
        content_product[x]['id'] = it
        x+=1

    for it in content_product:
        it["sum"] = it['count'] * it['price']
        basketSumm +=it["sum"]

    oldsum = 0
    if request.POST:
        if request.POST.get('coupon') == '6666':
                oldsum = basketSumm
                basketSumm = 0
                for it in content_product:
                        it['price'] = math.trunc(it['price'] /1.2)
                        it["sum"] = it['count'] * it['price']
                        coupon = True
                        basketSumm +=it["sum"]
                oldsum -= basketSumm
   
    
    return render(request,'main/basket.html', {'basketUser': content_product,'summ':basketSumm,'oldsum':oldsum ,'coupon':coupon})

def  contact(request):
   return render(request,'main/contact.html')

def  checkout(request):
    
    checkout_content = []
    basketUser = Basket.objects.filter( user_id_id = request.user.id)
    sumCheckout = 0
    for i in basketUser:
        name = Product.objects.get(id = i.id_product_id)
        allsum = int(i.priceProduct) * int(i.countProduct)
        sumCheckout += allsum
        checkout_content.append({
            'name' : name,
            'price' :i.priceProduct,
            'count' : i.countProduct,
            'allSum' : allsum

        })
       
    # for u in checkout_content:
    #     sumCheckout += int(checkout_content[u].allSum)
    # checkout_content.append({ 'all' :sumCheckout})    
    
    return render(request,'main/chekout.html', {'dataCheckout':checkout_content,
                                                'all':sumCheckout
                                                })

def  item(request,id):
    
    product = Product.objects.get(pk=id)
    basket = Basket()
   
    if request.POST:
       
        color = (request.POST.get('itemColor').strip(' ' ' \t\n\r'))
        size = (request.POST.get('sizeItem').strip(' ' ' \t\n\r'))
        count = request.POST.get('countProduct')
        price = request.POST.get('price')
        user = request.POST.get('userId')
        id_product2 = request.POST.get('productId')
        Basket.objects.create(colorProduct = color, sizeProduct = size, id_product_id = id_product2  ,countProduct = count, user_id_id = user, priceProduct = price )
        return redirect('basket')
    x = len(Product.objects.all()) 
    y = 1 
    nextItem = Product.objects.get(pk=x ) 
    prevItem = Product.objects.get(pk=y) 


    return render(request,'main/item.html',{    
                                            'product':product,
                                            'next': nextItem,
                                            'prev':prevItem})

def shop(request):
    
    product = Product.objects.all()
    kali = list(Product.objects.all())
    print(kali)
    print(Product.objects.all())
    lenProduct = len(product)
    count_paginator_elementov = 3
    try:
        paginator_of_all = Paginator(product,count_paginator_elementov)
        if 'page_all' in request.GET:
            page_num = request.GET.get('page_all')
        else:
            page_num = 1

        product = paginator_of_all.get_page(page_num)
    except:
        print('какая-то залупа')
    coat = Product.objects.filter(type_id__name = "пальто")#здесь фильтор на пальто
  
    print(coat)
    count_coat = len(coat)
    count_coat_list = 4
    try:
        
        paginator_filter_coat = Paginator(coat,count_coat_list)
        if 'page_coat' in request.GET:
            page_num_coat = request.GET.get('page_coat')
        else:
            page_num_coat = 1
        coat_page = paginator_filter_coat.get_page(page_num_coat)
    except:
        print("sd")
    sweatshirts = Product.objects.filter(type_id__name = "свитшот") #здесь фильтор на свитшот
    sweatshirts_count = len(sweatshirts)
    count_sweatshirts_list = 5
    try:
        paginator_sweatshirts = Paginator(sweatshirts,count_sweatshirts_list)
        if 'page_sweatshirts' in request.GET:
            page_num_sweatshirts = request.GET.get("page_sweatshirts")
        else:
            page_num_sweatshirts = 1
        sweatshirts_page = paginator_sweatshirts.get_page(page_num_sweatshirts)
        print(sweatshirts_page)
        
    except:
        print()
    Cardigans= Product.objects.filter(type_id__name = "кардиган") #здесь фильтор на кардиган
    count_cardigans = len(Cardigans)
    count_cardigans_list = 2
    try:
        paginator_cardigans = Paginator(Cardigans,count_cardigans_list)
        if 'page_cardigans' in request.GET:
            page_cardigan = request.GET.get('page_cardigans')
        else:
            page_cardigan= 1
        cardigan = paginator_cardigans.get_page(page_cardigan)
    except:
        print()
    hoodies =  Product.objects.filter(type_id__name = "футболки")
    count_hoodies= len(Cardigans)
    count_hoodies_list = 4
    try:
        paginator_hoodies = Paginator(hoodies,count_hoodies_list)
        if 'page_hoodies' in request.GET:
            page_num_hoodies = request.GET.get('page_hoodies')
        else:
            page_num_hoodies = 1
        Hoodies = paginator_hoodies.get_page(page_num_hoodies)
    except:
        print()
    proo = Product.objects.filter(type=2)
    print(proo)
    return render(request,'main/shop.html',
                                            {    
                                                #число элементов
                                                "countAll": lenProduct,
                                                "count_coat" :count_coat,
                                                "count_sweatshirts":sweatshirts_count,
                                                'count_cardigans' : count_cardigans,
                                                'count_hoodies' : count_hoodies,


                                                #количество частей
                                                "count_coat_list":count_coat_list,
                                                'count_sweatshirts_list':count_sweatshirts_list,
                                                'count_paginator_elementov':count_paginator_elementov,
                                                'count_cardigan_list': count_cardigans_list,
                                                'count_hoodies_list': count_hoodies_list,


                                                #перебираемые объекты
                                                'productAll':product,
                                                'coat': coat_page,
                                                "sweatshirts":sweatshirts_page,
                                                'cardigan':cardigan,
                                                'hoodies':Hoodies


                                            }
                                            )