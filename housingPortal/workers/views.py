from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        'title': 'Workers Homepage',
        'selected': request.resolver_match.view_name,
        'appname': request.resolver_match.view_name,
    }
    return render(request,'workers/home.html', context = content)