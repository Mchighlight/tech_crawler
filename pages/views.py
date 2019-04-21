from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from article.models import Article

def get_topic_article(topic_id):
    return Article.objects.filter(topic_id=topic_id).order_by('-upload_time')

def index(request):
    articles = Article.objects.order_by('subject')
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

def ai(request):
    articles = get_topic_article(1)
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
    return render(request, 'pages/ai.html', context)

def iot(request):
    articles = get_topic_article(2)
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
    return render(request, 'pages/ai.html', context)

def cloud_computing(request):
    articles = get_topic_article(3)
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
    return render(request, 'pages/ai.html', context)

def about(request):
    return render(request, 'pages/about.html')








