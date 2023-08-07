from django.shortcuts import render
from rest_framework import generics
from .models import Staff
from .serializers import StaffSerializer
from pymongo import MongoClient
from .utils import get_db_handle
from django.http import JsonResponse
from decouple import config
import json
from bson import ObjectId

# Create your views here.
def home(request):
    return render(request,"home.html",{})

class StaffListCreatViews(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def Customer(request):
    db_name = config('mongodb_db_name')
    db_host = config('mongodb_host')
    db_port = config('mongodb_port', default=27017, cast=int)
    db_user = config('mongodb_username')
    db_password = config('mongodb_password')
    
    db_handle, client = get_db_handle(db_name,db_host,db_port,db_user,db_password)

    if client:
        print("Connected to the database")
    else:
        print("Failed to connect to the database")
   
    collection = db_handle['contacts']
    print(collection.find())
    customers_data= list(collection.find())
    serialized_customers_data = JSONEncoder().encode(customers_data)

    client.close()

    return JsonResponse({'customers_data': serialized_customers_data})
