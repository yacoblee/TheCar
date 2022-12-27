from django.urls import reverse
from .models import Image
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic.detail import DetailView


class ImageListView(ListView):
    model = Image
    paginate_by = 12

class ImageCreateView(CreateView):
    model = Image
    fields = ['author', 'image_img', 'title', 'text']
    template_name_suffix = '_create'
    def get_success_url(self):
        return reverse('image:list')


class ImageDetailView(DetailView):
    model = Image
    fields = ['id', 'author', 'image_img', 'title', 'text']
    template_name_suffix = '_detail'
