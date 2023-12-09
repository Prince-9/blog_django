from django.shortcuts import render
from home.models import Contact

def index(request):
    return render(request,'home_templates/home.html')


def about(request):
    return render(request, 'home_templates/about.html')

# def contact(request):
#     return render(request,'home_templates/contact.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, "home_templates/contact.html")


