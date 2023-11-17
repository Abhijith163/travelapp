from django.shortcuts import render
from django.http import HttpResponse
from.models import Place,Pnames


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    jb=Pnames.objects.all()
    return render(request,'index.html',{'result':obj,'res':jb})





    
