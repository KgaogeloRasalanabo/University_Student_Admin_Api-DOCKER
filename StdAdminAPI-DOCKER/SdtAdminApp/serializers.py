from rest_framework import serializers
from SdtAdminApp.models import StdAdmins



class StdAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = StdAdmins
        fields = '__all__'
