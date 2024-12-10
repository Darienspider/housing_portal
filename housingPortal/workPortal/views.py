from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        'title': 'workPortal Homepage',
        'selected': request.resolver_match.view_name,
        'appname': request.resolver_match.view_name,
    }
    return render(request,'workPortal/home.html', context = content)