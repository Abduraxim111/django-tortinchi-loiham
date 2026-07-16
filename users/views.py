from django.shortcuts import render,redirect
from users.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,logout
from users.validator import user_validator,phone_validator,password_validator
# Create your views here.

def home_list(request):
    if (request.user.is_authenticated):
        return render(request,'home.html')
    return redirect("login_list")

def login_list(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        user = User.objects.filter(username=username)
        if user:
            
            user = user.first()
            parol = check_password(password,user.password)
            if parol:
                login(request,user)
                return redirect('home_list')
            
            
        return redirect('login_list')
    return render(request,'login.html')

def registor_list(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        phone_number = data.get('phone_number')
        password = data.get('password')
        datas = (first_name, username, phone_number, password)
        if None not in datas:
            user = user_validator(username)
            if not user:
                phone = phone_validator(phone_number)
                if phone:
                    password_chek = password_validator(password)
                    if password_chek:
                        user = User.objects.create(
                            first_name = first_name,
                            last_name = last_name,
                            username = username,
                            phone_nomber= phone_number,
                            password = password,
                        )
                        user.set_password(password)
                        user.save()
                        login(request,user)
                        return redirect('home_list')

    return render(request,'registor.html')

def logout_list(request):
    logout(request)
    return redirect('login_list')
