from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def paginaInicioView(req):
    if req.method == 'GET':
        print(req.headers)
        return HttpResponse('<h1>Benvindo ao curso de E-commerce!</h1>')

def paginaAboutView(req):
    return HttpResponse('<h2>Uma pagina com informação de nosso site!</h2>')

def paginaProdutoView(req):
    return HttpResponse('<h2>Esta seria uma pagina con informacao de um produto!</h2>')

def paginaHomeView(req):
    return render(req, 'paginas/home.html', {})

    # return HttpResponse('<h2>Esta seria uma pagina con informacao de um produto!</h2>')

