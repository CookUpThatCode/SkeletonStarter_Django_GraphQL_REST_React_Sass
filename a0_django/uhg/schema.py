from django.contrib.auth import get_user_model 
import graphene 
from graphene_django import DjangoObjectType 
from datetime import date

from .models import Hiker, Trail, Hike

class HikerType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class TrailType(DjangoObjectType):
    class Meta:
        model = Trail

class HikeType(DjangoObjectType):
    class Meta:
        model = Hike 

class Query(graphene.ObjectType):
    me = graphene.Field(HikerType)
    hikers = graphene.List(HikerType)
    hiker = graphene.Field(HikerType, hikerID=graphene.Int())
    trails = graphene.List(TrailType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in.")
        return user

    def resolve_hikers(self, info):
        return Hiker.objects.all() 

    def resolve_hiker(self, info, hikerID):
        return Hiker.objects.get(id=hikerID)

    def resolve_trails(self, info):
        return Trail.objects.all() 

class CreateHiker(graphene.Mutation):
    hiker = graphene.Field(HikerType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        bio = graphene.String() 

    def mutate(self, info, username, password, email, **kwargs):
        bio = kwargs.get('bio', '')
        hiker = Hiker.objects.create_user(username=username, email=email, password=password, bio=bio)
        # hiker = get_user_model()(username=username, email=email, bio=bio)
        # hiker.set_password(password)
        # hiker.save()
        return CreateHiker(hiker=hiker)

class CreateTrail(graphene.Mutation):
    trail = graphene.Field(TrailType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        trail = Trail.objects.create(name=name)
        return CreateTrail(trail=trail)

class CreateHike(graphene.Mutation):
    hike = graphene.Field(HikeType)

    class Arguments:
        trailID = graphene.Int(required=True)
        hikerID = graphene.Int(required=True)

    def mutate(self, info, trailID, hikerID):
        trail = Trail.objects.get(id=trailID)
        hiker = Hiker.objects.get(id=hikerID)
        hike = Hike.objects.create(trail=trail, hiker=hiker)
        return CreateHike(hike=hike)

class Mutation(graphene.ObjectType):
    create_hiker = CreateHiker.Field()
    create_trail = CreateTrail.Field()
    create_hike = CreateHike.Field()
