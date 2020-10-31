from django.urls import include
from first_app import views

urlpatterns = [
		path('', views.index, name='index')

]
