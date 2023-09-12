import requests
from django.shortcuts import render, redirect
from django.views import View


def get_free_books(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&filter=free-ebooks&subject:programming&maxResults=10"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


# Create your views here.

class SearchBook(View):
    def get(self, request):
        if request.user.is_authenticated:
            query = request.GET.get("title")
            result = get_free_books(query).get("items")
            return render(request, 'search_book.html', context={"books": result if query else None})
        else:
            return redirect("login")
