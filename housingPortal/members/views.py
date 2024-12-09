from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        'title': 'Member Homepage',
    }
    return render(request,'members/home.html', context = content)