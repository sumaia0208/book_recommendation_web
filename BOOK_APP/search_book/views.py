import requests
from django.shortcuts import render, redirect
from django.views import View


def get_free_books(query):
    if query:
        base_url = "http://openlibrary.org/search.json"
        params = {"title": query}

        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    else:
        return None


# Create your views here.

class SearchBook(View):
    def get(self, request):
        if request.user.is_authenticated:
            query = request.GET.get("title")
            result = get_free_books(query)

            book_list = list()
            if not result:
                return render(request, 'search_book.html', context={"books": None})
            # access all books author and Name.
            for data in result.get("docs")[:10]:
                book_list.append({"title": data.get("title", None), "author_name": data.get("author_name")[0]})
            return render(request, 'search_book.html', context={"books": book_list})

        else:
            return redirect("login")
