from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projectsList = Project.objects.all()
    context = {
        "projects":projectsList
        }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single_project.html',{
        'project':projectObj,
        'tags':tags
    })

def createProject(request):
    context = {'form':ProjectForm}
    return render(request, "projects/project_form.html", context)
