from django.db import models


# Create your models here.
class StdAdmins(models.Model):

    std_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=60)
    id_no = models.CharField(max_length=30)
    course_id = models.CharField(max_length=20)
    course_name = models.TextField(max_length=200)
    Course_code = models.CharField(max_length=20)
    