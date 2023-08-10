from django.shortcuts import render
from django.views.generic import TemplateView

# definir la classe index view

class IndexclView(TemplateView):
    template_name= 'index.html'

class Menuview(TemplateView):
    template_name= 'menu.html'

class Bookview(TemplateView):
    template_name = 'book.html'
    
class ProposView(TemplateView):
    template_name = 'about.html'
