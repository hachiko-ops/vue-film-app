from django.urls import path
from . import views

urlpatterns = [
    path('films/filters/', views.search, name='search'),
    path('films/filters/<int:session_id>/', views.search, name='search_session'),
]