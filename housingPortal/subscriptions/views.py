from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        'title': 'subscriptions Homepage',
    }
    return render(request,'subscriptions/home.html', context = content)