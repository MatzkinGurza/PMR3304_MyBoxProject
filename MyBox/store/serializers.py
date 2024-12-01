from rest_framework import serializers
from .models import Box

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['id', 'name', 'tag', 'price', 'description', 'image_url']
