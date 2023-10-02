import os
import django
from faker import Faker
import random

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

# Import your Django models after setting up Django
from mysiteApp.models import User

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name = fake_first_name,
                                          last_name= fake_last_name,
                                          email =fake_email)[0]

if __name__ == '__main__':
    print("Populating the database...Please wait.")
    populate(20)
    print("Population complete!")
