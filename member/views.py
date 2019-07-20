from django.shortcuts import render
from member.models import Member
from member.models import Trustee

# Create your views here.
def index(request):
    trustee = Trustee.objects.all()
    print(len(trustee))
    context = {
        'trustee' : trustee
    }
    return render(request, 'member/members.html', context)

def committee(request):
    members = Member.objects.all()
    print(len(members))
    context = {
        'members' : members
    }
    return render(request, 'member/committee.html', context)

def advisory(request):

    return render(request, 'member/advisory_board.html')
