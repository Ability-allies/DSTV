from django.db import models

# Define choices for category to avoid hardcoding throughout the app
CATEGORIES = [
    ('expecting_a_baby', 'Expecting a Baby'),
    ('new_parents', 'New Parents'),
    ('preschool_primary_school', 'Preschool and Primary School'),
    ('secondary_school', 'Secondary School'),
    ('young_people', 'Young People'),
    ('adults', 'Adults'),
]

class Advice(models.Model):
    date = models.DateField(unique=True)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    advice = models.TextField()
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.date}"

class TherapySession(models.Model):
    date = models.DateField(unique=True)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    therapy_content = models.TextField()
    advice = models.TextField()

    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f"Therapy for {self.get_category_display()} - {self.date}"


class journal (models.Model):
    child = models.