from django.db import models

# Create your models here.
class Person(models.Model):
    """docstring for ClassName"""

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return '%s %s' % (self.first_name + self.last_name)

        