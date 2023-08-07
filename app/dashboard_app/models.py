from django.db import models

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    access_level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"