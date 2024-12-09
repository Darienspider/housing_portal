from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        'title': 'Workers Homepage',
    }
    return render(request,'workers/home.html', context = content)