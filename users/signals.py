# users/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Child
from .dstv import generate_advice_and_therapy

@receiver(post_save, sender=Child)
def generate_advice_for_new_child(sender, instance, created, **kwargs):
    """Generate advice and therapy sessions when a new child is registered."""
    if created:
        print(f"New child registered: {instance.name}")
        # Specify the directory containing the PDFs
        pdf_directory = "C:\\Users\\Roy Agoya\\Desktop\\disable"  # Adjust this to your PDF folder
        # Generate advice and therapy for the newly created child
        generate_advice_and_therapy(instance, pdf_directory=pdf_directory)
