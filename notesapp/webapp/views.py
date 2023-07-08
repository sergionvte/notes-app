from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'list': [x + 1 for x in range(10)]
    }
    return render(request, 'index.html', context)
