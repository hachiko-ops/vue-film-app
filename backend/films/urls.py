from django.urls import path
from . import views

urlpatterns = [
    path('films/filters/', views.filters, name='filters'),
    path('films/filters/<int:session_id>/', views.filters, name='filters_session'),
]