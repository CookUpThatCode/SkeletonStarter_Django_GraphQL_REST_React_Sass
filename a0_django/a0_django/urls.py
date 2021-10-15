"""a0_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView 
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView
from uhg.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),   # this makes it POST. turn to False in production
    path('rest/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('rest/hikes/', getHikes, name="hikes"),
    path('rest/hikesOnTrail/<int:id>/', getHikesOnTrail, name="hikesOnTrail"),
    path('rest/uploadImage/', uploadImage, name="uploadImage"),
    path('rest/register/', registerUser, name='register'),
    path('rest/meQuery/', meQuery, name='meQuery')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
