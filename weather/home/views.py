from django.shortcuts import render, HttpResponse
# Create your views here.

def index(request):
    context = {
        "variable":"HIIII SGSI"
    }
    return render(request, 'home.html',context)
