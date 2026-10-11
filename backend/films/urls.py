from django.urls import path
from . import views

urlpatterns = [
    path('films/search/', views.search, name='search'),
    path('films/search/<uuid:session_id>/', views.search, name='search_session'),
]