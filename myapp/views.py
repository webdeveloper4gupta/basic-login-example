from django.shortcuts import render
from .models import aman
from .forms import mahajan
from django.contrib import messages
# Create your views here.

def home(request):
    fm=mahajan()
    if request.method=="POST":
        
        n2=request.POST.get('email')
        try:
            if aman.objects.get(email=n2):
                return render(request,"home.html")
            
                
        except:
            messages.error(request,"email already exist")
            
    return render(request,"index.html",{'forms':fm})
