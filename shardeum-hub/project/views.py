from multiprocessing import context
from django.shortcuts import render
from .models import ShardeumProjects

# Create your views here.

def index(request):
    project_hub = {}
    #project_hub.update({'DeFi': ShardeumProjects.objects.filter(cat_defi__contains=True)})
    #project_hub.update({'NFT': ShardeumProjects.objects.filter(cat_nft__contains=True)})
    #project_hub.update({'GameFi': ShardeumProjects.objects.filter(cat_gamefi__contains=True)})
    project_hub.update({'Newly Added': ShardeumProjects.objects.all()})
    
    context = {
        "project_hub": project_hub
    }
    return render(request,"index.html",context)
    
def details(request, id):
    project = ShardeumProjects.objects.filter(id=id).first()
    
    context = {
        "project":project
    }
    return render(request,"details.html",context)
    
def results(request, id):
    if id == 1:    
        projects = ShardeumProjects.objects.all()
    elif id == 2:    
        projects = ShardeumProjects.objects.filter(cat_defi__contains=True)
    elif id == 3:    
        projects = ShardeumProjects.objects.filter(cat_nft__contains=True)
    elif id == 4:    
        projects = ShardeumProjects.objects.filter(cat_gamefi__contains=True)
    else:
        projects = None
    
    context = {
        "projects":projects
    }
    return render(request,"results.html",context)
    
def searchresults(request, keyword):
    projects = []
    for project in ShardeumProjects.objects.all():
        if keyword in project.project_name:
            projects.append(project)
    context = {
        "projects":projects
    }
    return render(request,"searchresults.html",context)

def about(request):
    return render(request,"about.html")