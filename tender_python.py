import csv
import json
import os
import random
from datetime import datetime, timedelta
from bson import ObjectId
import pandas as pd


# פונקציה ליצירת שם אקראי
def random_name():
    return ''.join(random.choices(names))


# פונקציה ליצירת תאריך אקראי בטווח נתון
def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


# פונקציה ליצירת סכום אקראי
def random_amount():
    return random.randint(1000, 10000)


def random_number():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    return f'{num1}/{num2}'


# יצירת נתונים מגוונים
num_records = 5
data = []

# עדכון הקטגוריות להכללת יותר אפשרויות
body_names = ["אוניברסיטת חיפה", "עיריית פתח תקווה", "מועצה מקומית קרית עקרון", "משרד הביטחון", "עיריית תל אביב-יפו",
              "המוסד לביטוח לאומי", "משרד החינוך", "עיריית ירושלים", "משרד הבריאות", "האוניברסיטה העברית בירושלים",
              "מועצה אזורית חוף הכרמל", "עיריית חיפה", "משרד התחבורה", "הטכניון - מכון טכנולוגי לישראל",
              "אוניברסיטת בר אילן", "עיריית באר שבע", "משרד האוצר", "אוניברסיטת תל אביב", "עיריית אשדוד", "משרד הפנים"
              ]

categories = ["home", "office", "garden", "technology", "health", "education", "sports", "entertainment"]
reasons = ["late submission", "incomplete documents", "not meeting criteria", "invalid bid"]
tender_names = ["furniture", "stationery", "tools", "electronics", "software", "medical equipment", "sports gear",
                "entertainment system"]
committee_members = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Eve White", "Michael Green", "Emma Black"]
names = ["John Doe", "Jane Smith", "alice_smith", "bob_johnson", "carol_davis", "eve_martin", "frank_wright",
         "grace_adams", "henry_brown", "isabella_taylor", "jack_evans", "karen_wilson", "nathan_hall", "olivia_scott",
         "peter_robinson", "queen_smith", "robert_adams", "samantha_brown"]

for i in range(num_records):
    tender_number = random.randint(1, 1000)
    tender_name = random.choice(tender_names)
    submission_date = random_date(datetime(2023, 1, 1), datetime(2024, 12, 31)).strftime('%Y-%m-%d')
    published_date = random_date(datetime(2023, 1, 1), datetime(2024, 12, 31)).strftime('%Y-%m-%d')
    category = random.choice(categories)
    winner_name = random_name()
    details_winner = f'https://{winner_name}.com'
    participants = random_name()
    amount_bid = random_amount()
    estimate = amount_bid - 87

    data.append({
        'body_name': random.choice(body_names),
        'tender_number': tender_number,
        'tender_name': tender_name,
        'published_date': published_date,
        'submission_date': submission_date,
        "category": category,
        'winner_name': winner_name,
        'details_winner': details_winner,
        'participants': participants,
        'amount_bid': amount_bid,
        'estimate': estimate
    })

# הגדרת כותרות העמודות
csv_columns = [
    "שם הגוף", "מספר מכרז", "שם מכרז", "תאריך פרסום", "תאריך הגשה", "קטגוריות", "שם הזוכה", "מידע על הזוכה",
    "מציעים", "סכום ההצעה", "אומדן"
]

# כתיבת הנתונים לקובץ CSV
csv_file = "tender.csv"
try:
    print(f'tender python')
    with open(csv_file, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        if os.path.getsize(csv_file) == 0:
            writer.writeheader()
        for item in data:
            normalized_item = {
                "שם הגוף": item["body_name"],
                "מספר מכרז": item["tender_number"],
                "שם מכרז": item["tender_name"],
                "תאריך פרסום": item["published_date"],
                "תאריך הגשה": item["submission_date"],
                "קטגוריות": item["category"],
                "מציעים": item["participants"],
                "שם הזוכה": item["winner_name"],
                "מידע על הזוכה": item["details_winner"],
                "סכום ההצעה": item["amount_bid"],
                "אומדן": item["estimate"]
            }
            writer.writerow(normalized_item)
except IOError as e:
    print(f"I/O error: {e}")
