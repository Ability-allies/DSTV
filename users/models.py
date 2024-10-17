from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Parent(models.Model):
    # Extending the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Location fields using latitude and longitude
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6,
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6,
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )

    # Additional fields for Parent
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'


class child (models.Model):
    name = models.CharField(max_length=50)
    parent = models.ManyToManyField(Parent, null = False,blank = False)
    age = models.IntegerField ()
    gender = models.CharField (max_length=50)
    description = models.TextField