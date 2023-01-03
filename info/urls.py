from django.urls import path
from .views import *


app_name = 'info'

urlpatterns = [
    path('list/', InfoListView.as_view(), name='list'),
    path('create/', InfoCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', InfoDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', InfoDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', InfoUpdateView.as_view(), name='update'),
]
