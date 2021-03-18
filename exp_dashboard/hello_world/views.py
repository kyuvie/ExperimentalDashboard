from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello_world/home.html', {'hello_world': 'Hello World!'})
