from django.db import models

# Create your models here.
class airport(models.Model):
    code=models.CharField(max_length=4)
    city=models.CharField(max_length=64)
    def __str__(self):
        return f'{self.city} ( {self.code} )'


class flight(models.Model):
    origin=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='departures')
    destination=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='arivals')
    duration=models.IntegerField()
    def __str__(self):
        return f'{self.id} : from {self.origin} : to {self.destination}'
