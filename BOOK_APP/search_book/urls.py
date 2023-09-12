from django.contrib import admin
from django.urls import path, include
from .views import SearchBook

urlpatterns = [
    path('', SearchBook.as_view(), name="search_book"),
]
