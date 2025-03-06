from django.shortcuts import render
from . import data
from django.http import Http404

def blog(request):
    print("blog")
    
    context = {
        'text': "Olá, blog",
        'posts': data.posts
    }

    return render(request, "blog/index.html", context)

def post(request, post_id):
    post_id = int(post_id)
    found_post = next((post for post in data.posts if post['id'] == post_id), None)

    if not found_post:
        raise Http404('Post não encontrado.')


    context={
        'title': '- ' + found_post['title'],
        'post': found_post,
        'text': "Detalhes do Post",
    }

    return render(
        request,
        "blog/post.html",
        context
    )

def exemplo(request):
    print('exemplo')

    context= {
        "text": "Hola, exemple",
        "title": "Essa é uma página de exemplo -",
    }

    return render(request, "blog/exemplo.html", context)
