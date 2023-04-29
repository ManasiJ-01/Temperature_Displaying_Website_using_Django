from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.models import Detail
from django.http import HttpResponse
from datetime import datetime
from users.models import TempDisplay



# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully. Now login yourself')
            return redirect('index')
        
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def login(request):
    return render(request,'login.html')

def display(requests):
    temp = TempDisplay.object.all()
    return render(request,'display.html',{'temp':temp})
     

def detail(request):
    n=''
    if request.method =="POST":
        aadhar=request.POST.get('aadhar')
        img=request.POST.get('img')
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        gender=request.POST.get('gender')
        date=request.POST.get('date')
        #validation
        error_message = None
        
        if(not aadhar):
            error_messsage = "Aadhar number is required !!"
        elif len(aadhar) < 13:
            error_message = "Aadhar card number must be 12 digits long"
        elif(not name):
            error_message = "Name is required !!"
        elif len(not email):
            error_message = "Email is required"
        elif not mobile:
            error_message = "Mobile number is required"
        elif len(mobile) < 10:
            error_message = "Mobile number must be 10 digits long"
        
        
        #saving
        if not error_message:
            print(aadhar,img,name,email,mobile,gender,date)
        saveDetail = Detail(aadhar=aadhar,img=img,name=name,email=email,mobile=mobile,gender=gender,date=date)
        saveDetail.save()
        n='Successfully Data Inserted '
        
    return render(request,'detail.html',{'n':n})  

def TempDisplay(request):
    if request.method =="POST":
        aadhar=request.POST.get('aadhar')
        name=request.POST.get('name')
        temp=request.POST.get('temp')
        date=request.POST.get('date')
        time=request.POST.get('time') 
        
        en = TempDisplay(aadhar=aadhar,name=name,temp=temp,date=date,time=time)
        en.save()
        messages.success(request,'Post has been submitted successfully')
        return redirect('/')
    return render(request,'display.html')
        
    
        
    
    
    


   
    
    





