from django.urls import path
from . import views

urlpatterns = [
    path('search-article', views.search_article, name='search_article'),
]
