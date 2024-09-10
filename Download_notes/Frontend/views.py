from django.views.generic import ListView
from backend.models import Upload

class UploadHierarchyListView(ListView):
    model = Upload
    template_name = 'index.html'
    context_object_name = 'uploads'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Group uploads by folder_category, department, year, and college/university
        uploads = self.get_queryset()
        
        context['uploads_by_category'] = {}
        for upload in uploads:
            category = upload.folder_category
            if category not in context['uploads_by_category']:
                context['uploads_by_category'][category] = {}
            
            if upload.department not in context['uploads_by_category'][category]:
                context['uploads_by_category'][category][upload.department] = {}
                
            if upload.year not in context['uploads_by_category'][category][upload.department]:
                context['uploads_by_category'][category][upload.department][upload.year] = {}
                
            if upload.college_or_university:
                if upload.college_or_university not in context['uploads_by_category'][category][upload.department][upload.year]:
                    context['uploads_by_category'][category][upload.department][upload.year][upload.college_or_university] = []
                context['uploads_by_category'][category][upload.department][upload.year][upload.college_or_university].append(upload)
            else:
                if 'files' not in context['uploads_by_category'][category][upload.department][upload.year]:
                    context['uploads_by_category'][category][upload.department][upload.year]['files'] = []
                context['uploads_by_category'][category][upload.department][upload.year]['files'].append(upload)
        print(context)        
        return context
