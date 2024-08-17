from django.db import models
from user.models import User
# Create your models here.
class Books(models.Model):
    bookId= models.AutoField(primary_key=True)
    bname= models.CharField(max_length=100)
    bdesc= models.TextField(max_length=200)
    buser= models.ForeignKey(User, on_delete = models.CASCADE)
    bprize= models.IntegerField()
    plprize= models.IntegerField()
    exchange= models.BooleanField(default=True)
    bsold= models.BooleanField(default=False)

    

