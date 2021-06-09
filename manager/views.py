from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .forms import EventVisitorForm
from .models import Event


class EventListView(ListView):

    model = Event
    template_name = 'manager/home.html'
    context_object_name = 'events'
    paginate_by = 10                #Show 10 results per page

    def get_queryset(self):

        events = Event.objects.all().order_by('-created_at')
        
        return events

    def get_context_data(self, **kwargs):

        context = super(EventListView, self).get_context_data(**kwargs)

        return context

class EventDetailView(DetailView):
    
    model = Event
    template_name = 'manager/event_page.html'
        
    def get_context_data(self, **kwargs):

        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['form'] = EventVisitorForm()

        return context

    def post(self, request, *args, **kwargs):

        v_form = EventVisitorForm(request.POST)

        if v_form.is_valid():    
            new_visitor = v_form.save(commit=False)
            new_visitor.event = self.get_object()
            new_visitor.save()
            messages.success(request, "Uspešno ste se prijavili za dogadjaj!")

            return redirect('app-home')
        else:
            pk=self.get_object().id
            messages.warning(request, "Uneli ste neispravne podatke!")

            return redirect('event-details', pk=pk)
