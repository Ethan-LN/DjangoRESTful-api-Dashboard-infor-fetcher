from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{"print":"This is a test"})