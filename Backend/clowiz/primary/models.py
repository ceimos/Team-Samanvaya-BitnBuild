from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Cloth:
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    usecount = models.IntegerField()
    owner = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Outfit:
    id = models.AutoField(primary_key=True)
    usecount = models.IntegerField()
    owner = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class OutfitCloth:
    id = models.AutoField(primary_key=True)
    outfit = models.ForeignKey('outfit', on_delete=models.CASCADE)
    cloth = models.ForeignKey('Cloth', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Donation:
    id = models.AutoField(primary_key=True)
    doner = models.ForeignKey('User', on_delete=models.CASCADE)
    reciever = models.ForeignKey('User', on_delete=models.CASCADE)
    cloth = models.ForeignKey('Cloth', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name

class Sell:
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey('User', on_delete=models.CASCADE)
    buyer = models.ForeignKey('User', on_delete=models.CASCADE)
    cloth = models.ForeignKey('Cloth', on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class SustainibilityDetails:
    id = models.AutoField(primary_key=True)
    cloth = models.ForeignKey('Cloth', on_delete=models.CASCADE)
    carbonfootprint = models.FloatField()
    waterfootprint = models.FloatField()
    energyfootprint = models.FloatField()
    wastefootprint = models.FloatField()

    def __str__(self):
        return self.name