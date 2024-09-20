import os
from django.views.generic import ListView
from backend.models import Upload
import json

class Display(ListView):
    model = Upload
    template_name = 'table.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        uploads = self.get_queryset()
        data = []
        
        for upload in uploads:
            file_data = {
                "category": upload.folder_category,
                "department": upload.department,
                "semester": upload.semester,
                "year": upload.year,
                "college": upload.college_or_university,
                "file": os.path.basename(upload.pdf_file.name)
            }
            data.append(file_data)
        
        # Add the data to the context
        context['file_data'] = json.dumps(data)

        return context
