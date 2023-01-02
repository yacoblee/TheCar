from django.urls import reverse, reverse_lazy
from .models import Image
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class ImageListView(ListView):
    model = Image
    paginate_by = 12

class ImageCreateView(CreateView):
    model = Image
    fields = ['author', 'image_img', 'title', 'text']
    template_name_suffix = '_create'
    def get_success_url(self):
        return reverse_lazy('image:list')


class ImageDetailView(DetailView):
    model = Image
    fields = ['id', 'author', 'image_img', 'title', 'text']
    template_name_suffix = '_detail'

class ImageUpdateView(UpdateView):
    model = Image
    fields = ['title', 'image_img', 'text']
    template_name_suffix = '_update'
    success_url = reverse_lazy('image:list')

class ImageDeleteView(DeleteView):
    model = Image
    success_url = reverse_lazy('image:list')
    template_name = 'image/image_delete.html'