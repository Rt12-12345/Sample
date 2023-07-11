from django.urls import path
from news.views import search_news, search_history
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search_news, name='search_news'),
    path('history/', search_history, name='search_history'),
]
