from django.db import models

# Create your models here.
class User(models.Model):
    uid= models.CharField(max_length=10, primary_key=True)
    uname= models.CharField(max_length=30)
    uphone=  models.CharField(max_length=13)
    password=  models.CharField(max_length=100)
    userImg = models.ImageField(upload_to='')
    
    
    
class ExpectedBooks(models.Model):
    bookId= models.AutoField(primary_key=True)
    bname= models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

   