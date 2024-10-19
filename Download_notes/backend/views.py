import os
from django.views.generic import ListView
from backend.models import Upload
import json
from django.http import HttpResponseBadRequest, JsonResponse
from django.views import View
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
                "id":upload.id,
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


def is_ajax(request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
class FileDeleteView(View):
    template_name = 'table.html'
    def get(self, request, pk, *args, **kwargs):
        print("This is call")
        print(pk)
        try:
            # Check if the request is made via AJAX
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                # Try to get the object and delete it
                user = Upload.objects.get(pk=pk)
                user.delete()
                return JsonResponse({"message": "File deleted successfully"})
            else:
                return HttpResponseBadRequest("Invalid request")
        except Upload.DoesNotExist:
            return JsonResponse({"error": "File not found"}, status=404)