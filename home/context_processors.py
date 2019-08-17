from advert.models import Advert
from home.models import Project

def core(request):
    advert = Advert.objects.all().order_by('?')
    projects = Project.objects.all()

    project_nav = {}
    for project in projects:
        project_nav[project.date.year] = []        
    for project in projects:
        project_nav[project.date.year].append(project)

    context = {        
        'adverts' : advert,
        'nav_item_projects' : project_nav,
    }
    return context