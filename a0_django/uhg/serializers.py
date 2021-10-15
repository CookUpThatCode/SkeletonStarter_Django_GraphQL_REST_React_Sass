from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Hike, Trail, Hiker

class HikerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hiker
        fields = '__all__'

class HikeSerializerForTrail(serializers.ModelSerializer):
    hiker = HikerSerializer(read_only=True)         # add many=True if it's a list

    class Meta:
        model = Hike
        fields = ['checkInDate', 'hiker']

class TrailSerializer(serializers.ModelSerializer):
    hikes = HikeSerializerForTrail(many=True, read_only=True)

    class Meta:
        model = Trail
        fields = '__all__'

class HikeSerializer(serializers.ModelSerializer):
    hiker = HikerSerializer(read_only=True)         # add many=True if it's a list
    trail = TrailSerializer(read_only=True)

    class Meta:
        model = Hike
        fields = ['checkInDate', 'hiker', 'trail']
        # fields = '__all__'
