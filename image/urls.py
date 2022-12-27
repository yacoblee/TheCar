from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'image'

urlpatterns = [
    path('', ImageListView.as_view(), name='list'),
    path('create/', ImageCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ImageDetailView.as_view(model=Image, template_name='image/image_detail.html'), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)