from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Book, Author

def books(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'index.html', context)

def newbook(request):
    Book.objects.create(title=request.POST['book_title'], desc=request.POST['book_desc']) 
    return redirect('/')

def authors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request,'authors.html', context)

def newauthor(request):
    Author.objects.create(first_name=request.POST['author_first'],
    last_name=request.POST['author_last'], notes=request.POST['author_notes'])
    return redirect('/authors')

def book_info(request, id):
    other_authors = []
    book = Book.objects.get(id=id)
    for author in Author.objects.all():
        if author not in book.authors.all():
            other_authors.append(author)
    context = {
        "authors": other_authors,
        "book": book 
    }
    return render(request, 'book_info.html', context)

def author_info(request, id):
    other_books = []
    author = Author.objects.get(id=id)
    for book in Book.objects.all():
        if book not in author.books.all():
            other_books.append(book)
    context = { 
        "books": other_books,
        "author": author 
    }
    return render(request, 'author_info.html', context)

def addbooktoauthor(request, id):
    author = Author.objects.get(id=id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f'/authors/{author.id}')


def addauthortobook(request, id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{book.id}')