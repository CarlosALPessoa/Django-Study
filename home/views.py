from django.shortcuts import render

def context_key():
    return {
        "text": "Aplicando context na home",
        "title":" - Home"
    }

def home(request):
    return render(
        request,
        'home/main.html',
        context_key()
    )