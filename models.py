from django.db import models


# Create your models here.
class Grades(models.Model):
    gname=models.CharField(max_length=20)
    gdate=models.DateTimeField()
    ggirlnum=models.IntegerField()
    gboynum=models.IntegerField()
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return "%s-%d-%d"%(self.gname,self.ggirlnum,self.gboynum)

class Students(models.Model):
    sname=models.CharField(max_length=20)
    sgender=models.BooleanField(default=True)
    sage=models.IntegerField()
    scontend=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    sgrade=models.ForeignKey("Grades",on_delete=models.CASCADE) #关联外键

from tinymce.models import HTMLField
class text(models.Model):
    str=HTMLField()
