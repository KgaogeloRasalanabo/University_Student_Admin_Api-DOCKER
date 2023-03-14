from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from SdtAdminApp.models import StdAdmins
from SdtAdminApp.serializers import StdAdminSerializer


# Create your views here.
@csrf_exempt
def student_administration_Api(request,id=0):
    if request.method=='GET':
        student_administrations = StdAdmins.objects.all()
        student_administration__serializer = StdAdminSerializer(student_administrations,many=True)
        return JsonResponse(student_administration__serializer.data,safe=False)
    elif request.method=='POST':
        student_administration_data = JSONParser().parse(request)
        student_administration__serializer = StdAdminSerializer(data=student_administration_data)
        if student_administration__serializer.is_valid():
            student_administration__serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        student_administration_data = JSONParser().parse(request)
        student_administration = StdAdmins.objects.get(id = student_administration_data['id'])
        student_administration__serializer = StdAdminSerializer(student_administration,data=student_administration_data)
        if student_administration__serializer.is_valid():
            student_administration__serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        student_administration = StdAdmins.objects.get(id=id)
        student_administration.delete()
        return JsonResponse("Deleted Succefully",safe=False)
