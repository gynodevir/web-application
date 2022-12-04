from django.shortcuts import render
from .models import about,slider,client
def home(request):
    aboutdata=about.objects.all()
    sliderdata=slider.objects.all()
    clientdata=client.objects.all()
    context = {'aboutdata' : aboutdata,'sliderdata' : sliderdata, 'clientdata' : clientdata}
    
    return render(request,'index.html',context)
def profile(request):
    return render(request,'employee/profile.html')
def aboutus(request):
    return render(request,'about.html')

# Create your views here.
