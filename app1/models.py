from django.db import models


class travel(models.Model):
    Username=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=40,default="")
    Password=models.CharField(max_length=40,default="")
    Confirmpassword=models.CharField(max_length=40,default="")
   
