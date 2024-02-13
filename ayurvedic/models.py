from datetime import timezone
from django.db import models

# Create your models here.


class login1(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

class doctereg(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    post=models.CharField(max_length=20)
    pin=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    lid=models.ForeignKey(login1,on_delete=models.CASCADE)

class patientsreg(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    place = models.CharField(max_length=30)
    post = models.CharField(max_length=20)
    pin = models.BigIntegerField()
    phone = models.BigIntegerField()
    lid=models.ForeignKey(login1,on_delete=models.CASCADE)

class stafftreg(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    place = models.CharField(max_length=30)
    post = models.CharField(max_length=20)
    pin = models.BigIntegerField()
    phone = models.BigIntegerField()
    lid = models.ForeignKey(login1, on_delete=models.CASCADE)

class sendcomplaints1(models.Model):
    complaint=models.CharField(max_length=500)
    date=models.DateField(max_length=20)
    reply=models.CharField(max_length=500)
    userid=models.ForeignKey(patientsreg,on_delete=models.CASCADE)


class shedule(models.Model):
    day = models.DateField(null=True, blank=True)
    fromtime = models.TimeField()
    totime = models.TimeField()
    did = models.ForeignKey(doctereg, on_delete=models.CASCADE)


class booking(models.Model):
    date=models.DateField(max_length=20)
    status=models.CharField(max_length=20)
    userid=models.ForeignKey(patientsreg,on_delete=models.CASCADE)
    sid=models.ForeignKey(shedule,on_delete=models.CASCADE)

class medicine(models.Model):
    medicine2=models.CharField(max_length=50)
    usage=models.CharField(max_length=50)
    discription=models.CharField(max_length=100)
    price=models.BigIntegerField()






