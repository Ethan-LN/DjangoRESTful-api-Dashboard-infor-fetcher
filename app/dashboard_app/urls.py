from django.urls import path
from . import views
from .views import StaffListCreateViews, StaffRetrieveUpdateDeleteView, Customer

urlpatterns = [
    path('',views.home, name='home'),
    path('staff/', StaffListCreateViews.as_view(), name='staff-list'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDeleteView.as_view(), name='staff-detail'),
    path('customers/', Customer, name='customer'), 
]