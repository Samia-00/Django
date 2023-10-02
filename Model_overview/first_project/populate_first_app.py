import os
import django
from faker import Faker
import random

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
django.setup()

# Import your Django models after setting up Django
from firstApp.models import Webpage, Topic, AccessRecord

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating the database...Please wait.")
    populate(20)
    print("Population complete!")
