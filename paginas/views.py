from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Produto

# Create your views here.

def paginaInicioView(req):
    if req.method == 'GET':
        print(req.headers)
        return HttpResponse('<h1>Benvindo ao curso de E-commerce!</h1>')

def paginaAboutView(req):
    #return HttpResponse('<h2>Uma pagina com informação de nosso site!</h2>')
    return render(req, 'paginas/sobre.html', {})

def paginaProdutoView(req):
    return HttpResponse('<h2>Esta seria uma pagina con informacao de um produto!</h2>')

def paginaHomeView(req):
    return render(req, 'paginas/home.html', {})

    # return HttpResponse('<h2>Esta seria uma pagina con informacao de um produto!</h2>')

class ProdutoListView(ListView):
    model = Produto
    template_name = "paginas/home.html"

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = "paginas/produto_detail.html"