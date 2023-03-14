from rest_framework.routers import DefaultRouter
from django.urls import path, include
from SdtAdminApp.views import StdAdminViewSet


router = DefaultRouter()
router.register('SdtAdminApp', StdAdminViewSet)
urlpatterns = [
    path('api/', include(router.urls)),  
]
