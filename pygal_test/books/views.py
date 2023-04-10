from django.shortcuts import render, get_object_or_404, redirect
from .models import Books
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf.urls.static import static
import pygal   

# Create your views here.
def BookGraph(request):
    data = []
    context = {}
    books_list = Books.objects.all()
    context['books_list'] = books_list
    
    for book in Books.objects.all(): 
        data.append(book.price)
    
    # make the graph
    book_chart = pygal.Bar()
    book_chart.add('Books', data)
    book_chart.render_to_file('static/book_chart.svg')
    
    
    return render(request, 'books/home.html', context)