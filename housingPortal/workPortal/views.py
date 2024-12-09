from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        'title': 'workPortal Homepage',
    }
    return render(request,'workPortal/home.html', context = content)