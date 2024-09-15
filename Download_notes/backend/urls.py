from django.urls import path
from .views import Display

urlpatterns = [
    path('admin/', Display.as_view(), name='upload_hierarchy'),
]
