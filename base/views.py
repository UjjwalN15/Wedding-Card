from django.shortcuts import render, redirect
from .models import *
from django.utils.timezone import now
from googletrans import Translator
from django.utils import formats
from django.utils.translation import gettext_lazy as _
from datetime import datetime


# Initialize the translator
translator = Translator()
# Define a translation map for English to Nepali digits
english_to_nepali_digits = str.maketrans("0123456789", "०१२३४५६७८९")



# Function to translate text to Nepali
def translate_to_nepali(text):
    translated = translator.translate(text, src='en', dest='ne')
    return translated.text
def home(request):
    if request.method == 'POST':
        # Groom Details
        groom_photo = request.FILES.get('groom_photo')  # Handle file uploads with request.FILES
        groom_first_name = request.POST.get('groom_first_name')
        groom_last_name = request.POST.get('groom_last_name')
        groom_father = request.POST.get('groom_father')
        groom_mother = request.POST.get('groom_mother')
        groom_relative1 = request.POST.get('groom_relative1')
        groom_relative2 = request.POST.get('groom_relative2')
        groom_relative3 = request.POST.get('groom_relative3')

        # Bride Details
        bride_photo = request.FILES.get('bride_photo')  # Handle file uploads with request.FILES
        bride_first_name = request.POST.get('bride_first_name')
        bride_last_name = request.POST.get('bride_last_name')
        bride_father = request.POST.get('bride_father')
        bride_mother = request.POST.get('bride_mother')
        bride_relative1 = request.POST.get('bride_relative1')
        bride_relative2 = request.POST.get('bride_relative2')
        bride_relative3 = request.POST.get('bride_relative3')

        # Marriage Details
        date = request.POST.get('date')
        time = request.POST.get('time')
        venue = request.POST.get('venue')
        date_obj = datetime.strptime(date, "%Y-%m-%d")

        # bs_date = NepaliDate(date_obj).to_nepali()
        # bs_date_str = bs_date.to_date_string()  
            # For date formatting in Nepali

        # Creating Instances in Database
        marriage = Marriage.objects.create(
            groom_photo=groom_photo,
            groom_first_name=groom_first_name,
            groom_last_name=groom_last_name,
            groom_father=groom_father,
            groom_mother=groom_mother,
            groom_relative1=groom_relative1,
            groom_relative2=groom_relative2,
            groom_relative3=groom_relative3,
            
            
            bride_photo=bride_photo,
            bride_first_name=bride_first_name,
            bride_last_name=bride_last_name,
            bride_father=bride_father,
            bride_mother=bride_mother,
            bride_relative1=bride_relative1,
            bride_relative2=bride_relative2,
            bride_relative3=bride_relative3,
            
            
            date=date_obj,
            time=time,
            venue=venue,
            
            
            groom_first_name_nepali=translate_to_nepali(groom_first_name),
            groom_last_name_nepali=translate_to_nepali(groom_last_name),
            groom_father_nepali=translate_to_nepali(groom_father),
            groom_mother_nepali=translate_to_nepali(groom_mother),
            groom_relative1_nepali=translate_to_nepali(groom_relative1),
            groom_relative2_nepali=translate_to_nepali(groom_relative2),
            groom_relative3_nepali=translate_to_nepali(groom_relative3),
            
            
            bride_first_name_nepali=translate_to_nepali(bride_first_name),
            bride_last_name_nepali=translate_to_nepali(bride_last_name),
            bride_father_nepali=translate_to_nepali(bride_father),
            bride_mother_nepali=translate_to_nepali(bride_mother),
            bride_relative1_nepali=translate_to_nepali(bride_relative1),
            bride_relative2_nepali=translate_to_nepali(bride_relative2),
            bride_relative3_nepali=translate_to_nepali(bride_relative3),
            # Convert time (e.g., '14:30') to Nepali numerals
            # date_in_nepali = bs_date_str,
            time_in_nepali = time.translate(english_to_nepali_digits),
            venue_nepali=translate_to_nepali(venue)
        )
        # Pass data to index.html
        context = {
            'marriage': marriage,
        }
        return render(request,'index.html', context)
        # Redirect to 'card' after successful save}
    return render(request, 'form.html')



