from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # route for admin panel
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('', include("search_book.urls"))
]

