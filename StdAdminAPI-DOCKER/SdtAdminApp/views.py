from rest_framework.viewsets import ModelViewSet
from SdtAdminApp.models import StdAdmins
from SdtAdminApp.serializers import StdAdminSerializer


# Create your views here.
class StdAdminViewSet (ModelViewSet):
    serializer_class = StdAdminSerializer
    queryset = StdAdmins.objects.all()
