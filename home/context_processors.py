from advert.models import Advert
from home.models import Project
from home.models import Policy

def core(request):
    adverts = Advert.objects.all().order_by('?')
    projects = Project.objects.all()
    policies = Policy.objects.all()
    project_nav = {}
    for project in projects:
        project_nav[project.date.year] = []        
    for project in projects:
        project_nav[project.date.year].append(project)

    context = {        
        'adverts' : adverts,
        'nav_item_projects' : project_nav,
        'policies' : policies,
    }
    return context