from django.shortcuts import render
from member.models import Member
from member.models import Trustee
from member.models import Advisor

# Create your views here.
def trustees(request):
    trustee = Trustee.objects.all()
    context = {
        'trustee' : trustee
    }
    return render(request, 'member/trustees.html', context)

def managment(request):
    members = Member.objects.all()
    context = {
        'members' : members
    }
    return render(request, 'member/managment.html', context)

def advisors(request):

    advisors = Advisor.objects.all()
    context = {
        'advisors' : advisors
    }
    return render(request, 'member/advisors.html', context)

def membership(request):
    return render(request, 'member/membership.html')