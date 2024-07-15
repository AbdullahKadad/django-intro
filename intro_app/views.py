from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePage(TemplateView):
    template_name = "home.html"
    
class CascadingStyleSheetsPage(TemplateView):
    template_name = "css.html"

class JavaScriptPage(TemplateView):
    template_name = "js.html"