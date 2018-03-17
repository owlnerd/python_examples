from django.db import models


class Mathematician(models.Model):
    fname = models.CharField(max_length = 40)
    lname = models.CharField(blank = True,
                             null = True,
                             max_length = 40,
                             default = 'Nepoznato')


class Theorem(models.Model):
    name = models.CharField(max_length = 100)
    area = models.CharField(max_length = 100)
    author = models.ManyToManyField(Mathematician)
