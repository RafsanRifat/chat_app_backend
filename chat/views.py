from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return render(request, "chat/index.html")
    return render(request, "chat/index.html")
    # return HttpResponse("working")