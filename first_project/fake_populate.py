import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord, Users
from faker import Faker

fakegen = Faker()

topics = ['search','marketwatch','news','games','social']
users = ['saichand','eluri','puja','harsha']

def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t



def populate(n=5):
    for entry in range(n):

        top = add_topics()

        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()

        webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url = fake_url)[0]

        arecord = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

        users = Users.objects.get_or_create(firstname = fake_firstname, lastname = fake_lastname, email = fake_email)[0]

if __name__ == '__main__':
    print("Populating script")
    populate(10)
    print("Data populated successfully")
