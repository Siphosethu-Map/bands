from django.db import models


""" Create your models here.
 Band class, where the parameters of the data the user will input is created
 this model is found in the administration side """


class Band(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    genre = models.CharField(max_length=80, null=False, blank=False)
    formed_date = models.DateField()
    description = models.TextField()


def __str__(self):
    return self.title
