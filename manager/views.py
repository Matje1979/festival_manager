from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import EventVisitorForm
from .models import Event


class EventListView(ListView):
    model = Event
    template_name = 'manager/home.html'
    context_object_name = 'events'
    paginate_by = 2
    def get_queryset(self):
        events = Event.objects.all().order_by('-created_at')
        # for  in posts:
        #     print (post.Sadržaj)
        #     for tag in post.tags.all():
        #         print ("Tag:", tag)
        #         print ("Tag type:", type(tag))
        return events
    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        return context
    # ordering = ['-date_posted']
    #for a ListView, default context object name is object_list, but that can be overriden in the way above.
    #for DetailView, defaul context object name is 'object'

class EventDetailView(DetailView):
    
    model = Event
    template_name = 'manager/event_page.html'
        
    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        # context['upravnik'] = Upravnik.objects.get(ulaz=self.request.user.Ulaz)
        # context['ulaz'] = translit(self.request.user.Ulaz.Ulica_i_broj, 'sr', reversed=True)
        # post = get_object_or_404(Post, pk = self.kwargs['pk'])
        # context['comments'] = Comment.objects.filter(post=post)
        context['form'] = EventVisitorForm()
        return context

    def post(self, request, *args, **kwargs):
        v_form = EventVisitorForm(request.POST)
        if v_form.is_valid():    
            new_visitor = v_form.save(commit=False)
            new_visitor.event = self.get_object()
            new_visitor.save()
            return redirect('app-home')
        else:
        	return redirect('event-details')
