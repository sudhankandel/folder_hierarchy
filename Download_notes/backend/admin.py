from django.contrib import admin
from .models import Upload

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('folder_category','semester', 'department', 'year', 'pdf_file', 'uploaded_at')
    list_filter = ('folder_category', 'department', 'year')
    search_fields = ('folder_category', 'department', 'year', 'pdf_file')
    readonly_fields = ('uploaded_at',)
