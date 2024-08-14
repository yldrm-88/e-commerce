from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import*


# Create your views here.
def userLogin(request):
    if request.method=='POST':
        userName=request.POST["userName"]
        userPass=request.POST["userPass"]

        user=authenticate(request,username=userName,password=userPass)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return render(request,'login.html',{'error':'Kullanıcı adı ya da parola yanlış.'})
    return render(request,'login.html')

def userRegister(request):
    if request.method =="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]
        if password==repassword:
            if User.objects.filter(username=username).exists():
                return render(request,'register.html',{"error":"Kullanıcı adı mevcut."})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,'register.html',{"error":"Bu email mevcut."})
                else:
                    user=User.objects.create_user(first_name=firstname,
                                                  last_name=lastname,
                                                  username=username,
                                                  email=email,
                                                  password=password
                                                  )
                    user.save()
                    Customer.objects.create(user=user, name=username, email=email)
                    return render(request, 'register.html', {"success": "Kayıt başarılı. Giriş yapabilirsiniz."})
        else:
            return render(request,'register',{"error":"Parolalar eşleşmiyor."})
    return render(request,'register.html')

def comunucation(request):
    if request.method=='POST':
        customer=request.user.customer
        message=request.POST.get('message')
        Communucation.objects.create(customer=customer,message=message)
        messages.success(request,'Mesaj Gönderildi.')
        return render(request, 'comunucation.html')
    return render(request, 'comunucation.html')



def userLogout(request):
    logout(request)
    return redirect("homepage")

def account(request):
    return render(request,'account.html')

def deleteAccount(request):
    user=request.user
    user.delete()
    return redirect("login")


#exists() -->Belirli bir ürünün veritabanında olup olmadığını kontrol etmek için