"""heroes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'hero', views.HeroViewSet)
router.register(r'abilitytype', views.AbilityTypeViewSet)
router.register(r'ability', views.AbilityViewSet)
router.register(r'relationship', views.RelationshipViewSet)
router.register(r'relationshiptype', views.RelationshipTypesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('current-datetime/', views.current_datetime, name='current-datetime'),
    path('Hero/<int:hero_id>/', views.get_hero),
    path('Hero/', views.get_hero),
    path('api/', include(router.urls)),
]




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
