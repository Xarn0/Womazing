from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.hashers import make_password


def reg(request):
    form = UserForm
   
    if request.POST:
        
        dataForm = form(request.POST)
        if dataForm.is_valid(): 
           
            name = dataForm.cleaned_data['username']
            
           
            password = dataForm.cleaned_data['password1']
            password_repeat = dataForm.cleaned_data['password2']
            email = dataForm.cleaned_data['email']
            date = datetime.datetime.now()
            if password == password_repeat:
                user = User.objects.create_user(name)
                user.password = make_password(password)
                user.last_login = date
                user.email = email
               
                user.save()
        
                
              
            return redirect('login')
         
            
    return render(request,'register/register.html',  {
                'form' : form,
               
                
            })