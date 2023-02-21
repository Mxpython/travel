from django.http import HttpResponse
from django.shortcuts import render

from .models import Place
from .models import Person

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    per=Person.objects.all()
    return render(request,'index.html',{'result': obj,'team': per})






# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     sub=x-y
#     div=x/y
#     mul=x*y
#
#     return render(request,'result.html',{'result':res,'subtract':sub,'division':div,'multiplication':mul})