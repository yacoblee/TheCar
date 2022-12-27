from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Info
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class InfoListView(ListView):
    model = Info
    paginate_by = 10


class InfoCreateView(CreateView):
    model = Info
    fields = ['author', 'title', 'text']
    success_url = reverse_lazy('info:list')
    template_name_suffix = '_create'


class InfoDetailView(DetailView):
    model = Info


class InfoUpdateView(UpdateView):
    model = Info
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class InfoDeleteView(DeleteView):
    model = Info
    success_url = reverse_lazy('list')


