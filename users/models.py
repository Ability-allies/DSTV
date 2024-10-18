from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6,
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6,
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'


class Child(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ManyToManyField(Parent, blank=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


CATEGORIES = [
    ('expecting_a_baby', 'Expecting a Baby'),
    ('new_parents', 'New Parents'),
    ('preschool_primary_school', 'Preschool and Primary School'),
    ('secondary_school', 'Secondary School'),
    ('young_people', 'Young People'),
    ('adults', 'Adults'),
]

class Advice(models.Model):
    # child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=30, choices=CATEGORIES)
    advice = models.TextField()

    class Meta:
        ordering = ['date']
        # unique_together = ['child', 'date']

    def __str__(self):
        return f"Advice for {self.date}: {self.advice}"


class TherapySession(models.Model):
    # child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=30, choices=CATEGORIES)
    therapy_content = models.TextField()

    class Meta:
        ordering = ['date']
        # unique_together = ['child', 'date']

    def __str__(self):
        return f"Therapy for {self.date}: {self.therapy_content}"


class Journal(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    entry = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return f"Journal entry for {self.child.name} by {self.parent.user.username} at {self.time}"
