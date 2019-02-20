from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'name', 'type', 'manufacture_year', 'capacity', 'price')
