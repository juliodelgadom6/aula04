from django.urls import path

from .views import paginaInicioView, paginaAboutView, paginaHomeView
from .views import ProdutoListView, ProdutoDetailView

urlpatterns = [
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('', paginaInicioView, name='inicio'),
    path('sobre', paginaAboutView, name='sobre'),
    path('home', ProdutoListView.as_view(), name='home')
]