from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
# Create your views here.

def index(request):
	Webpage_list = AccessRecord.objects.order_by('date')
	my_dict = {"insert_me":Webpage_list}
	return render(request, 'index.html', context=my_dict)