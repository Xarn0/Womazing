from django.urls import path, include, re_path
from register import views
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register', views.RegisterView.as_view(), name='reg'),

]
