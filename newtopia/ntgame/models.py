from django.db import models

# Create your models here.
class Kingdom(models.Model):

    name = models.CharField(max_length=200)
    island = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Province(models.Model):

    name = models.CharField("Province Name", max_length=200)
    race = models.CharField("Province Race", max_length=40)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
