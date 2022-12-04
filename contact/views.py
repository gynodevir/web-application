from django.shortcuts import render
from .models import contactlist,contactform
def contactus(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contactformdata=contactform(name=name,email=email,subject=subject,message=message)
        contactformdata.save()

    contactlistdata=contactlist.objects.all()[0]
    context={'contactlistdata' : contactlistdata}
    return render(request,'contact.html',context)

# Create your views here.
