import os
import requests
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from PyPDF2 import PdfReader
from .models import Advice, TherapySession

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_endpoint = "https://api.openai.com/v1/chat/completions"

CATEGORIES = [
    ('expecting_a_baby', 'Expecting a Baby'),
    ('new_parents', 'New Parents'),
    ('preschool_primary_school', 'Preschool and Primary School'),
    ('secondary_school', 'Secondary School'),
    ('young_people', 'Young People'),
    ('adults', 'Adults'),
]

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""  # Append text from each page
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def determine_category(content):
    """Determine the category based on content keywords."""
    keywords = {
        "expecting_a_baby": ["baby", "expecting", "pregnancy"],
        "new_parents": ["parent", "new parents", "first-time"],
        "preschool_primary_school": ["preschool", "primary", "kindergarten"],
        "secondary_school": ["teen", "secondary", "high school"],
        "young_people": ["young", "youth", "adolescent"],
        "adults": ["adult", "mature"]
    }

    content_lower = content.lower()
    for category, words in keywords.items():
        if any(word in content_lower for word in words):
            return category
    return "adults"  # Default category if not matched

def generate_advice_and_therapy(child, pdf_directory=None, entry_date=None):
    """Generate advice and therapy for the given child based on their description and optional PDFs."""
    description = child.description
    current_date = entry_date or make_aware(datetime.now())
    print(f"Generating advice for date: {current_date}")

    # Optionally load and process PDFs if the directory is provided
    pdf_text = ""
    if pdf_directory and os.path.exists(pdf_directory):
        for pdf_file in os.listdir(pdf_directory):
            if pdf_file.endswith('.pdf'):
                pdf_path = os.path.join(pdf_directory, pdf_file)
                print(f"Processing PDF: {pdf_path}")
                pdf_text += extract_text_from_pdf(pdf_path)

    # Combine child's description and any extracted PDF text
    combined_content = description + "\n" + pdf_text
    print(f"Combined content for API: {combined_content[:50]}...")  # Print the first 50 chars for brevity

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": combined_content}],
        "max_tokens": 1000,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    try:
        response = requests.post(openai_endpoint, headers=headers, json=data, timeout=30)
        response.raise_for_status()

        response_data = response.json()
        advice_content = response_data['choices'][0]['message']['content']
        category = determine_category(advice_content)

        # Populate Advice model
        advice = Advice(
            date=current_date,
            category=category,
            advice=advice_content
        )
        advice.save()
        print(f"Saved advice for date: {current_date}")

        # Populate TherapySession model
        therapy_session = TherapySession(
            date=current_date,
            category=category,
            therapy_content=advice_content  # This can be adapted for more specific therapy content
        )
        therapy_session.save()
        print(f"Saved therapy session for date: {current_date}")

    except requests.exceptions.RequestException as e:
        print(f"Error generating advice and therapy: {e}")

def populate_advice_for_year(child, pdf_directory=None):
    """Populate advice and therapy for each day of the year for the given child."""
    start_date = datetime.now()

    for day in range(365):
        # Calculate the date for this entry
        current_date = make_aware(start_date + timedelta(days=day))
        print(f"Creating entry for: {current_date}")
        
        # Call the function to generate advice and therapy
        generate_advice_and_therapy(child, pdf_directory, current_date)

# Usage example (replace this with your actual child instance)
# child = Child.objects.get(id=1)  # Assuming you have a Child model
# pdf_directory = 'path/to/pdf_directory'  # Adjust as needed
# populate_advice_for_year(child, pdf_directory)
