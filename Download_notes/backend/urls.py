from django.urls import path
from .views import Display,FileDeleteView,AddFile

urlpatterns = [
    path('admin/', Display.as_view(), name='upload_hierarchy'),
    path('delete-file/<int:pk>/', FileDeleteView.as_view(), name='delete_file'),
    path('addfile/',AddFile.as_view(), name='addfile')

]
