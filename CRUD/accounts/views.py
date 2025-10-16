from django.shortcuts import render,HttpResponse,redirect
from accounts.models import CustomUser
from .forms import CustomerUserCreationForm
from django.contrib import messages
# Create your views here.
def home(request):
    return HttpResponse("Hello")

def user_signup(request):
    if request.method=="POST":
        form=CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()

            messages.info("Account created successfully")
            return redirect("login")


        
    else:
        return render(request,"signup.html")