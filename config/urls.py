
from django.contrib import admin
from django.urls import path
from users.views import home_list, login_list,logout_list,registor_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_list, name='home_list'),
    path('login/',login_list, name='login_list'),
    path('logout/',logout_list, name='logout_list'),
    path('registor/',registor_list, name='registor_list'),
]
