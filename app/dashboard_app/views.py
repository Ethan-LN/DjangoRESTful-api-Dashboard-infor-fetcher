from django.shortcuts import render
from rest_framework import generics
from .models import Staff
from .serializers import StaffSerializer

# Create your views here.
def home(request):
    return render(request,"home.html",{})

class StaffListCreatViews(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer