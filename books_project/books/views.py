from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Book

# /books/
def books_view(request):
    books = Book.objects.all().order_by('pub_date')

    context = {
        'books': books
    }
    return render(request, 'books/books_list.html', context)

# /books/2021-01-02/
def books_by_date(request, pub_date):
    date = datetime.strptime(pub_date, "%Y-%m-%d").date()

    books = Book.objects.filter(pub_date=date).order_by('pub_date')

    # предыдущая дата
    prev_date = (
        Book.objects
        .filter(pub_date__lt=date)
        .order_by('-pub_date')
        .values_list('pub_date', flat=True)
        .distinct()
        .first()
    )

    # следующая дата
    next_date = (
        Book.objects
        .filter(pub_date__gt=date)
        .order_by('pub_date')
        .values_list('pub_date', flat=True)
        .distinct()
        .first()
    )

    context = {
        'books': books,
        'current_date': date,
        'prev_date': prev_date,
        'next_date': next_date,
    }

    return render(request, 'books/books_date.html', context)