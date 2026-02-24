from django.urls import path
from .views import books_view, books_by_date

urlpatterns = [
    path('', books_view, name='books_list'),
    path('<str:pub_date>/', books_by_date, name='books_by_date'),
]