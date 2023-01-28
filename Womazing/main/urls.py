from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="main"),
    path('about_brand',views.aboutBrand,name="about_brand"),
    path('basket',views.basket,name="basket"),
    path('contact',views.contact,name="contact"),
    path('checkout',views.checkout,name="checkout"),
    path('shop',views.shop,name="shop"),
    path('product/<int:id>',views.item,name="product"),
    
   
    path('accounts/', include('register.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)