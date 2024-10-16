import os
from datetime import timedelta, datetime
import openai
import django
from django.utils.timezone import make_aware
from .models import Advice, TherapySession  # Update with your app's name

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up the categories for the app
CATEGORIES = ["expecting a baby", "new parents", "preschool and primary school", 
              "secondary school", "young people", "adults"]

def load_pdfs_and_generate_advice(directory):
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    
    # Assuming January 1st as the start date
    start_date = datetime(datetime.now().year, 1, 1)
    
    for day in range(365):  # Loop through each day of the year
        date = make_aware(start_date + timedelta(days=day))
        
        # Choose a PDF file at random for each day
        pdf_path = os.path.join(directory, pdf_files[day % len(pdf_files)])
        with open(pdf_path, 'rb') as pdf_file:
            pdf_content = pdf_file.read()
        
        # Send request to OpenAI to generate advice
        response = openai.Completion.create(
            model="gpt-4",
            prompt=f"Based on this content, generate daily advice for {CATEGORIES}: {pdf_content.decode('latin1', errors='ignore')}",
            max_tokens=200
        )
        
        # Store the generated advice content and assign category dynamically
        advice_content = response.choices[0].text.strip()
        category = determine_category(advice_content)  # Helper function for category
        
        # Create the Advice entry
        Advice.objects.create(
            date=date,
            category=category,
            advice=advice_content
        )
        
        # Example therapy session generation for each day (repeat similar logic as needed)
        TherapySession.objects.create(
            date=date,
            category=category,
            therapy_content="Generated therapy content based on the advice.",  # Replace with actual content
            advice=advice_content
        )

# Helper function to determine the category based on content
def determine_category(content):
    # Placeholder logic to choose a category
    if "baby" in content.lower():
        return "expecting a baby"
    elif "parent" in content.lower():
        return "new parents"
    # Add more conditions for other categories...
    return "adults"  # Default category if not matched

# Run the script
load_pdfs_and_generate_advice('/path/to/your/pdf/folder')
