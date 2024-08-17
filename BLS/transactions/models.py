from django.db import models
from user.models import User
# Create your models here.
class Transactions(models.Model):
    tid= models.AutoField(primary_key=True)
    transactionId = models.CharField(max_length=1000)
    fromUser = models.ForeignKey(User, on_delete = models.CASCADE,related_name="fromUser")
    toUser = models.ForeignKey(User, on_delete = models.CASCADE,related_name="toUser")
    tamount = models.IntegerField()
    tdate = models.DateTimeField(auto_now_add=True)
    exchangeType = models.CharField(max_length=10)
    
    
    