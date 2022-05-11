from django.urls import path

from .views import ProjectsIndex

urlpatterns = [
    path('', ProjectsIndex.as_view(), name='projects-index'),
]
