from django.views.generic import TemplateView
from django.shortcuts import render

class ProjectsIndex(TemplateView):
    template_name = "projects_index.html"
