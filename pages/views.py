from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from article.models import Article

def index(request):
    articles = Article.objects.order_by('-upload_time')
    articles_carousel_active = articles[0]
    articles_carousel = articles[1:4]
    articles_listing  = articles[4:]

    paginator = Paginator(articles_listing, 6)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        'articles_carousel_active': articles_carousel_active,
        'articles_carousel' : articles_carousel,
        'articles_listing'  : paged_articles
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')








