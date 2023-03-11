from django.shortcuts import render
from django.views.generic import ListView
from .models import Ishchi
class IshchiView(ListView):
    model = Ishchi
    context_object_name = "Ish"
    template_name = "index.html"

