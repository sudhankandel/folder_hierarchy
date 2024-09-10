from django.urls import path
from .views import UploadHierarchyListView

urlpatterns = [
    path('', UploadHierarchyListView.as_view(), name='upload_hierarchy'),
]
