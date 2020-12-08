from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
import markdown


# Create your views here.
def index(request):
    articles = Article.objects.all()
    # return (HttpResponse("hello"))
    return render(request, 'blog/index.html', {'articles': articles})


def detail(request, request_id):
    article = get_object_or_404(Article, id=request_id)
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    return render(request, 'blog/detail.html', {'article': article})
