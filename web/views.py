from django.shortcuts import render

# Create your views here.


def index(request):
    context={}
    return render(request,'web/index.html' ,context)

def shop(request):
    context={}
    return render(request,'web/shop.html' ,context)