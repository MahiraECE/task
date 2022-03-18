from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView # new
from django.contrib.auth.models import User
from .models import itemsList,CreatingUser
from .models import Brand,Category

# Create your views here.
# Home Page View and rendering the products details
class HomePageView(ListView):
    model = itemsList
    template_name = 'sam.html'
# Getting Category details in the Page 
class categoryPageView(ListView):
    model = Category
    template_name = 'category.html'
# Getting Brand details in the Page 
class brandsPageView(ListView):
    model = Brand
    template_name = 'brand.html'
# Entire product list
class productPageView(ListView):
    model = itemsList
    template_name = 'products.html'
#Functional view for Signuo
def gettingFormDetails(request):
    # userForm=userDetails()
   
    user1=CreatingUser()
    if request.method=="POST":
        user1.first_name=request.POST.get("first_name")
        user1.last_name=request.POST.get("last_name")
        user1.email_address=request.POST.get("email_address")
        user1.mobileNumber=request.POST.get("mobileNumber")
      
        user1.save()
    return render(request,"auth.html")
#getting login details
def getDetails(request):
    getting=CreatingUser.objects.all()
    for gett in getting:
        print(gett)
        if request.method=="POST":
            global x1
            x1=request.POST["userName"]
            # print(x1)
            x2=request.POST["passWord"]
            
   
            if x1==gett.userName:
                if x2==gett.passWord:
                    print("success")
                    return redirect(dashBoard)
                else:
                    # Modification for password Worng
                    print("check password")

            
         
    return render(request,"login.html")
#dashboard redirectinf
def dashBoard(request):
    dash = CreatingUser.objects.get(userName=x1)
    return render(request,"dashboard.html",{'dash':dash})
