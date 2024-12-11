from django.shortcuts import render
from .forms import *
from django.contrib.auth import login
from django.http import HttpResponse

# Create your views here.
def home(request):
    content = {
        'title': 'Member Homepage',
        'selected': request.resolver_match.view_name,
        'appname': request.resolver_match.view_name,
    }
    return render(request,'members/home.html', context = content)

# def register(request):
#     if request.method == 'POST':
#         form = memberRegistration(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return HttpResponse(f'<h2> Member created Successfully - {form.cleaned_data['username']} <br> <a href="../"> Back to home page </a> ') 
#     else:
#         form = memberRegistration()
#     return render(request, 'register.html', {'form': form})