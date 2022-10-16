import requests
import os
import glob
import re
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from datetimerange import DateTimeRange
import docx

api_url_base = 'https://api.linkedin.com/v2/'

access_token = "VOTRE TOKEN"
urn = "VOTRE URN"
author = f"urn:li:person:{urn}"

from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path
dotenv_path = join(dirname(__file__), '.env')

# load file from the path
load_dotenv(dotenv_path)

headers = {'X-Restli-Protocol-Version': '2.0.0',
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'}


def send_to_linkedin_api(current_document_text):
    api_url = f'{api_url_base}ugcPosts'

    post_data = {
        "author": author,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": current_document_text
                },
                "shareMediaCategory": "NONE"
            },
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTIONS"
        },
    }

    response = requests.post(api_url, headers=headers, json=post_data)

    if response.status_code == 201:
        print(" Le post a été envoyé sur LinkedIn.")
        print(response.content)
    else:
        print("\033[1;31;40m Erreur : ")
        print(response.content)

def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def get_document(filename):
    doc = docx.Document(filename)
    fullText = []
    for element in doc.paragraphs:
        fullText.append(element.text)

    return '\n'.join(fullText)

def check_documents_every_hour():
    documents_in_repertory = glob.glob("./scheduled_posts/*.docx")
    current_date_minus_one_hour = datetime.today() - timedelta(hours=1)
    current_date_plus_one_hour = datetime.today() + timedelta(hours=1)

    for key, filename in enumerate(documents_in_repertory):
        cleaned_filename = re.sub(r'^.*?___', '', filename).split('.docx')[0].split('__')
        
        date = cleaned_filename[0].split('_')
        date_day = int(date[0]) 
        date_month = int(date[1])
        date_year = int(date[2])

        time = cleaned_filename[1].split('_')
        time_hour = int(time[0])
        time_minute = int(time[1])

        scheduled_document_date = datetime(date_year, date_month, date_day, time_hour, time_minute)

        time_range = DateTimeRange(current_date_minus_one_hour, current_date_plus_one_hour)

        if scheduled_document_date in time_range:
            current_document_text = get_document(filename)
            send_to_linkedin_api(current_document_text)

def send_test():
    print("\n\033[1;33;40m Un document dans ./scheduled_posts,")
    print("\033[1;33;40m A la date et l'heure d'aujourd'hui, doit être présent,")
    print("\033[1;33;40m Pour ce test.\n")

    check_documents_every_hour()

def init():
    print("\033[1;33;40m Automatisation lancée ...")
    print("\033[1;33;40m Ne fermez pas ce terminal.")

    scheduler = BlockingScheduler()
    scheduler.add_job(check_documents_every_hour, 'interval', hours=1)
    scheduler.start()
