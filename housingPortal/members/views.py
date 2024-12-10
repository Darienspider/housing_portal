from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        'title': 'Member Homepage',
        'selected': request.resolver_match.view_name,
        'appname': request.resolver_match.view_name,
    }
    return render(request,'members/home.html', context = content)