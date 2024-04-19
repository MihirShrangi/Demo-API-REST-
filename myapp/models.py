from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptnm=models.CharField(max_length=30)
    location=models.CharField(max_length=20)

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    job=models.CharField(max_length=20)
    salary=models.IntegerField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    