from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class EstudianteView(TemplateView):
    template_name='index.html'
class CreditosView(TemplateView):
    template_name='creditos.html'