from django.db import models

# Create your models here.
class EMP(models.Model):
    Name=models.CharField(max_length=50)
    FullName=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Address=models.TextField(max_length=50)
    Age=models.IntegerField()
    Contact=models.CharField(max_length=50)
    
    class Meta:
        db_table='emp'

from django import forms

class EmpForm(forms.ModelForm):
    class Meta:
        model=EMP
        fields='__all__'



class IMG(models.Model):
    Customer_Name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='images/')
    class Meta:
        db_table='empimg'

class ImgForm(forms.ModelForm):
        class Meta:
             model=IMG
             fields='__all__'




    
