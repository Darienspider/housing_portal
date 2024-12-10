from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        'title': 'subscriptions Homepage',
        'selected': request.resolver_match.view_name,
        'appname': request.resolver_match.view_name,
    }
    return render(request,'subscriptions/home.html', context = content)