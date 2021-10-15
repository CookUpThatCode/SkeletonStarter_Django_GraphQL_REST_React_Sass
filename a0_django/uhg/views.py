from django.shortcuts import render
from django.contrib.auth import get_user_model 

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Hike, Hiker, Trail
from .serializers import HikeSerializer, TrailSerializer, HikerSerializer

from django.contrib.auth.hashers import make_password
from rest_framework import status

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = get_user_model().objects.create_user(
            username=data['username'], 
            email=data['email'], 
            password=data['password'],
        )
        serializer = HikerSerializer(user)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def meQuery(request):
    serializer = HikerSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getHikes(request):
    hikes = Hike.objects.filter(hiker=request.user)
    serializer = HikeSerializer(hikes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getHikesOnTrail(request, id):
    trail = Trail.objects.get(id=id)
    serializer = TrailSerializer(trail)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadImage(request):
    hiker = request.user
    # data = request.data
    # hikerID = data['hikerID']
    # hiker = Hiker.objects.get(id=hikerID)
    hiker.image = request.FILES.get('image')
    hiker.save()
    return Response('Image was uploaded')