import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'first_project.settings')

import django
django.setup()


import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker
fakeGen = Faker()

topics = ['FlipKart','Walmart','AWS','Internet','Mozilla']


def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t


def populate(N=5):

	for entry in range(N):
		top = add_topic()

		fake_url = fakeGen.url()
		fake_name = fakeGen.company()
		fake_date = fakeGen.date()

		web = Webpage.objects.get_or_create(topic=top, url=fake_url,name=fake_name)[0]

		acc_rec = AccessRecord.objects.get_or_create(title=web,date=fake_date)[0]



if __name__ == "__main__":
	print("populating script...")
	populate(20)
	print("populating ")

