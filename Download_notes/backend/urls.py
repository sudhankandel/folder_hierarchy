from django.urls import path
from .views import Display,FileDeleteView

urlpatterns = [
    path('admin/', Display.as_view(), name='upload_hierarchy'),
    path('delete-file/<int:pk>/', FileDeleteView.as_view(), name='delete_file'),

]
