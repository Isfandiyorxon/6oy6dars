from django.shortcuts import render

# Create your views here.
from .models import Author,Category,Book
def hom(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    contex={
        'categories':categories,
        'books':books,
        'authors':authors,
    }
    return render(request,'index.html',contex)

def books_to_catigores(request,category_id):
    categories = Category.objects.all()
    books=Book.objects.filter(category_id=category_id)

    contex={
        'books':books,
        'categories':categories
    }
    return render(request,'index.html',contex)
