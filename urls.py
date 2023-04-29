from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path 
from users import views
from django.contrib.auth import views as auth_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('detail/', views.detail, name='detail'),
    path('display/', views.display, name='display'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
    
    
]

urlpatterns += staticfiles_urlpatterns()


