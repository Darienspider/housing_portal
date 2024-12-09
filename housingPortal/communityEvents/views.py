from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        'title': 'Events Homepage',
    }
    return render(request,'communityEvents/home.html', context = content)