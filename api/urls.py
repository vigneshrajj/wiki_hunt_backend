from django.urls import path
from . import views

urlpatterns = [
    path('search-article', views.search, name='search_article'),
]
