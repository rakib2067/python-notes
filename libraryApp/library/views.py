from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book
# Create your views here.


def index(request):
    data = {'books': Book.objects.all()}

    return render(request, 'index.html', data)


def show(request, book_id):

    # filtered = list(filter(lambda book: book['id'] == book_id, dummy_data))
    book = get_object_or_404(Book, pk=book_id)
    data = {'book': book}
    return render(request, 'show.html', data)
