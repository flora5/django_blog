from django.shortcuts import render
from django.http import HttpResponse


#return pure string
def index_string(request):
    return HttpResponse("Hello, this is index...")

#return html
def index(request):
    data = "Hello, i'm come from mysql"
    return render(request,'index.html',{'data': data})