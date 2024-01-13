"""
URL configuration for beekeeping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers


from api.views.users import UserViewSet
from api.views.groups import GroupViewSet
from api.views.beeyards import BeeyardViewSet
from api.views.hives import HiveViewSet
from api.views.diseases import DiseaseViewSet
from api.views.actions import HarvestViewSet, TreatmentViewSet
from api.views.common import beeyards

from public.views.beeyards import VBeeyardViewSet
from public.views.hives import VHiveViewSet
from public.views.users import VUserViewSet

from api.models.beeyards import Beeyard
from api.models.hives import Hive
from api.models.diseases import Disease

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'hive', HiveViewSet)
router.register(r'beeyard', BeeyardViewSet)
router.register(r'disease', DiseaseViewSet)
router.register(r'harvest', HarvestViewSet)
router.register(r'vusers', VUserViewSet)
router.register(r'treatment', TreatmentViewSet)
router.register(r'vbeeyard', VBeeyardViewSet)
router.register(r'vhive', VHiveViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    #admin and fakeadmin routes
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('admin2/', admin.site.urls),
    
    #url from the app api
    #regarder le premier cours
    path('api/Beeyard/', beeyards),
    path('api/Hive/', Hive),
    #path('__debug__/', include(debug_toolbar.urls)),#to be added when debug toolbar is added
]
