import os
import requests
from datetime import timedelta, datetime
from dotenv import load_dotenv
import django
from django.utils.timezone import make_aware
from PyPDF2 import PdfReader
import time

load_dotenv()

# Set up environment variables for Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disable.settings")

# Now import Django and set it up
django.setup()

# Load environment variables
azure_openai_key = os.getenv("AZURE_OPENAI_KEY")
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

# Check if API key is loaded
if not azure_openai_key or not azure_openai_endpoint:
    raise ValueError("Azure OpenAI key or endpoint not found.")

# Import models after setting up Django
from care.models import Advice, TherapySession

# Set up the categories for the app
CATEGORIES = ["expecting a baby", "new parents", "preschool and primary school", 
              "secondary school", "young people", "adults"]

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

def load_pdfs_and_generate_advice(directory):
    api_key = os.getenv("AZURE_OPENAI_API_KEY")  # Ensure your API key is set in the environment
    endpoint = "https://desai.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-08-01-preview"
    
    # Set the rate limit parameters
    tokens_per_minute = 1000  # Your quota
    requests_per_minute = 6    # 1K tokens / 150 tokens per request (estimate)
    delay_between_requests = 60 / requests_per_minute  # Delay in seconds between requests

    for pdf_file in os.listdir(directory):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(directory, pdf_file)
            print(f"Processing: {pdf_path}")

            with open(pdf_path, 'rb') as f:
                pdf_reader = PdfReader(f)
                pdf_text = ''
                for page in pdf_reader.pages:
                    pdf_text += page.extract_text() + '\n'

            data = {
                "messages": [
                    {"role": "user", "content": pdf_text}
                ],
                "max_tokens": 1000,  # Adjust based on your needs
            }
            headers = {
                "Content-Type": "application/json",
                "api-key": api_key,
            }

            retries = 0
            while retries < 5:
                try:
                    response = requests.post(endpoint, headers=headers, json=data, timeout=30)
                    response.raise_for_status()
                    
                    # Check for 401 error
                    if response.status_code == 401:
                        print("Authorization failed. Please check your API key and deployment.")
                        break
                    
                    advice = response.json()
                    print(f"Advice for {pdf_file}: {advice}")

                    # Wait before making the next request to adhere to the rate limit
                    time.sleep(delay_between_requests)
                    break  # Exit the retry loop if successful
                
                except requests.exceptions.RequestException as e:
                    print(f"Error generating advice for {pdf_path}: {e}")
                    if 'Connection aborted' in str(e) or 'RemoteDisconnected' in str(e):
                        time.sleep(2 ** retries)
                        retries += 1
                        print(f"Retrying... Attempt {retries}")
                    else:
                        break

# Helper function to determine the category based on content
def determine_category(content):
    """Determine the category based on content keywords."""
    keywords = {
        "expecting a baby": ["baby", "expecting", "pregnancy"],
        "new parents": ["parent", "new parents", "first-time"],
        "preschool and primary school": ["preschool", "primary", "kindergarten"],
        "secondary school": ["teen", "secondary", "high school"],
        "young people": ["young", "youth", "adolescent"]
    }

    content_lower = content.lower()
    for category, words in keywords.items():
        if any(word in content_lower for word in words):
            return category

    return "adults"  # Default category if not matched

# Run the script
load_pdfs_and_generate_advice("/mnt/c/Users/Roy Agoya/OneDrive/Documents/dsai primary school")
