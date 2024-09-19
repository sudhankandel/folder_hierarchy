import os
from django.views.generic import ListView
from backend.models import Upload

class Display(ListView):
    model = Upload
    template_name = 'table.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uploads = self.get_queryset()

        for i in uploads:
            print(i)
        return context
    