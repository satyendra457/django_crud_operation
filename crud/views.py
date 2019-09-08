from django.shortcuts import render, redirect
from .models import BookList

# Create your views here.
def home(request):
    books = BookList.objects.all
    return render(request, 'crud/home.html', {'books':books})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        author = request.POST.get('author')
        about = request.POST.get('about')
        book_list = BookList(title=title, price=price, author=author, about=about)
        book_list.save()
        return redirect('/')

def edit(request, id):
    books = BookList.objects.get(pk=id)
    context = {'books': books}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    books = BookList.objects.get(pk=id)
    if request.method == "GET":
        books.title = request.GET['title']
        books.price = request.GET['price']
        books.author = request.GET['author']
        books.save()
        return redirect('/')

def delete(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')

def add_book(request):
    return render(request, 'crud/add_book.html')
