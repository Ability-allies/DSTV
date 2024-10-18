import os
import requests
from datetime import timedelta, datetime
from dotenv import load_dotenv
import django
from django.utils.timezone import make_aware
from PyPDF2 import PdfReader
import time

# Load environment variables and setup Django
load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disable.settings")
django.setup()

# Check if API key and endpoint are loaded
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_endpoint = "https://api.openai.com/v1/chat/completions"
if not openai_api_key:
    raise ValueError("OpenAI API key not found.")

# Import Django models
from users.models import Advice, TherapySession, Child, Parent

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

def load_pdfs_and_generate_advice(directory, child):
    # Rate limiting parameters
    tokens_per_minute = 1000
    requests_per_minute = 6
    delay_between_requests = 60 / requests_per_minute

    for pdf_file in os.listdir(directory):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(directory, pdf_file)
            print(f"Processing: {pdf_path}")

            pdf_text = extract_text_from_pdf(pdf_path)
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": pdf_text}],
                "max_tokens": 1000,
            }
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {openai_api_key}"
            }
            
            retries = 0
            while retries < 5:
                try:
                    response = requests.post(openai_endpoint, headers=headers, json=data, timeout=30)
                    response.raise_for_status()
                    
                    response_data = response.json()
                    advice_content = response_data['choices'][0]['message']['content']
                    category = determine_category(advice_content)
                    current_date = make_aware(datetime.now())
                    
                    # Populate the Advice model
                    advice = Advice(                        
                        date=current_date,
                        category=category,
                        advice=advice_content
                    )
                    advice.save()
                    print(f"Saved advice for {child.name} on {current_date}")

                    # Populate the TherapySession model
                    therapy_session = TherapySession(                        
                        date=current_date,
                        category=category,
                        therapy_content=advice_content  # Replace with actual therapy content if different
                    )
                    therapy_session.save()
                    print(f"Saved therapy session for {child.name} on {current_date}")

                    time.sleep(delay_between_requests)
                    break  # Exit retry loop if successful

                except requests.exceptions.RequestException as e:
                    print(f"Error: {e}")
                    retries += 1
                    time.sleep(2 ** retries)  # Exponential backoff for retries

# Run the script with a specific child and directory
child = Child.objects.first()  # Replace with specific child lookup if needed
load_pdfs_and_generate_advice("C:\\Users\\Roy Agoya\\Desktop\\disable", child)
