from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import UserRegistrationForm
from members.models import Community, Member

# Create your views here.
def home(request):
    community_id = 2
    community = Community.objects.filter(id=community_id).first() 
    member = Member.objects.filter(user=request.user)

    content = {
        'title': 'Homepage',
        'authenticated': request.user.is_authenticated,
        'user': request.user,
        'selected': request.resolver_match.view_name,
        'appname': request.resolver_match.view_name,
        # 'community': Community.objects.filter(id='2')
        'community':community,
        'member': member,

    }
    return render(request,'home.html', context = content)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse(f'<h2> Username created Successfully - {form.cleaned_data['username']} <br> <a href="../"> Back to home page </a> ') 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})