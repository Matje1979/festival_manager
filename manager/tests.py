from django.test import TestCase, Client
from django.urls import reverse, resolve
from .models import Event, Visitor
from .views import EventListView, EventDetailView
import datetime


class TestUrls(TestCase):

    def setUp(self):

        self.client = Client()
        self.time1= datetime.datetime(2021, 8, 10)
        self.time2=datetime.datetime(2021, 8, 14)

    def test_list_events_url_resolves(self):
        
        url = reverse('app-home')
        print (resolve(url)) 
        self.assertEqual(resolve(url).func.view_class, EventListView)

    def test_event_details_url_resolves(self):
        
        event = Event.objects.create(name="Filozofijada", beggining=self.time1, end=self.time2, country="Srbija", city="Beograd", address="Terazije 6")
        url = reverse('event-details', args=[event.id])
        self.assertEqual(resolve(url).func.view_class, EventDetailView)


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.time1= datetime.datetime(2021, 8, 10)
        self.time2=datetime.datetime(2021, 8, 14)
        self.event = Event.objects.create(name="Filozofijada", beggining=self.time1, end=self.time2, country="Srbija", city="Beograd", address="Terazije 6")
        self.list_url = reverse('app-home')
        self.details_url = reverse('event-details', args=[self.event.id])
        self.post_url = reverse('event-details', args=[self.event.id])

    def test_event_list_view(self):
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_event_detail_view(self):
        
        self.data = {
            "first_name": "Jane", "last_name": "Doe", "email":"janedoe@gmail.com", "event": self.event.id
        }

        response1 = self.client.get(self.details_url)
        response2 = self.client.post(self.details_url, data=self.data)

        self.assertEqual(response1.status_code, 200)
        self.assertIsNotNone(Visitor.objects.get(email="janedoe@gmail.com")) #Checking if the view creates a Visitor instance.