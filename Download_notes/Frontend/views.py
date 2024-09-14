import os
from django.views.generic import ListView
from backend.models import Upload

class UploadHierarchyListView(ListView):
    model = Upload
    template_name = 'index.html'
    context_object_name = 'uploads'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uploads = self.get_queryset()

        context['uploads_by_category'] = {}

        for upload in uploads:
            category = upload.folder_category
            if category not in context['uploads_by_category']:
                context['uploads_by_category'][category] = {}

            department = upload.department
            if department not in context['uploads_by_category'][category]:
                context['uploads_by_category'][category][department] = {}
            semester = upload.semester
            if semester:
                if semester not in context['uploads_by_category'][category][department]:
                    context['uploads_by_category'][category][department][semester] = {}

                year = upload.year
                if year not in context['uploads_by_category'][category][department][semester]:
                    context['uploads_by_category'][category][department][semester][year] = {}

                college_or_university = upload.college_or_university
                if college_or_university:
                    if college_or_university not in context['uploads_by_category'][category][department][semester][year]:
                        context['uploads_by_category'][category][department][semester][year][college_or_university] = []
                    context['uploads_by_category'][category][department][semester][year][college_or_university].append({
                        'file_name': os.path.basename(upload.pdf_file.name),  # Only the file name without the path
                        'file_url': upload.pdf_file.url  # Full URL for file download
                    })
                else:
                    if 'files' not in context['uploads_by_category'][category][department][semester][year]:
                        context['uploads_by_category'][category][department][semester][year]['files'] = []
                    context['uploads_by_category'][category][department][semester][year]['files'].append({
                        'file_name': os.path.basename(upload.pdf_file.name),  # Only the file name
                        'file_url': upload.pdf_file.url  # Full URL
                    })
            else:
                if semester not in context['uploads_by_category'][category][department]:
                    context['uploads_by_category'][category][department][semester] = {}
                if 'files' not in context['uploads_by_category'][category][department][semester]:
                    context['uploads_by_category'][category][department][semester]['files'] = []
                context['uploads_by_category'][category][department][semester]['files'].append({
                    'file_name': os.path.basename(upload.pdf_file.name),  # Only the file name
                    'file_url': upload.pdf_file.url  # Full URL
                })
        print(context)
        return context