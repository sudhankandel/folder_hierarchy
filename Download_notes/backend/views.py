import os
from django.views.generic import ListView
from backend.models import Upload

class Display(ListView):
    model = Upload
    template_name = './backend/templates/index.html'