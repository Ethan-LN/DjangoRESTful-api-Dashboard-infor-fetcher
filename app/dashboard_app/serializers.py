from rest_framework import serializers
from .models import Staff
from .models import Customer

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
