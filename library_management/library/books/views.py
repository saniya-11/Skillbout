from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.http import HttpResponse

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book-list')
    return render(request, 'books/book_form.html')


def book_update(request, id):  # ✅ Accept pk here
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book-list')
    return render(request, 'books/book_form.html', {'book': book})


def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
