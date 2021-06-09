from django.urls import path
from .views import (
	EventListView, 
	EventDetailView
) 

urlpatterns = [
    path('', EventListView.as_view(), name="app-home"),
    path('event/<int:pk>', EventDetailView.as_view(), name="event-details") 
]	