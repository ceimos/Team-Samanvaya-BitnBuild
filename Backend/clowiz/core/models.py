from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.utils import timezone
# Create your models here.
class User(AbstractUser):
    pass

class Cloth(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    type = models.CharField(max_length=100, blank=True, null=True)
    usecount = models.IntegerField(default=0, blank=False, null=False)
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    #purchase_date = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Outfit(models.Model):
    id = models.AutoField(primary_key=True)
    usecount = models.IntegerField()
    owner = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class OutfitCloth(models.Model):
    id = models.AutoField(primary_key=True)
    outfit = models.ForeignKey('outfit', on_delete=models.CASCADE)
    cloth = models.ForeignKey('Cloth', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    doner = models.ForeignKey('User', on_delete=models.CASCADE, related_name='doner')
    reciever = models.ForeignKey('User', on_delete=models.CASCADE, related_name='reciever')
    cloth = models.ForeignKey('Cloth', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name

class Sell(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey('User', on_delete=models.CASCADE, related_name='seller')
    buyer = models.ForeignKey('User', on_delete=models.CASCADE, related_name='buyer')
    cloth = models.ForeignKey('Cloth', on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class SustainibilityDetails(models.Model):
    id = models.AutoField(primary_key=True)
    cloth = models.ForeignKey('Cloth', on_delete=models.CASCADE)
    carbonfootprint = models.FloatField()
    waterfootprint = models.FloatField()
    energyfootprint = models.FloatField()
    wastefootprint = models.FloatField()

    def __str__(self):
        return self.name