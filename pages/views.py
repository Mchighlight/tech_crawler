from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from article.models import Article

def get_topic_article(topic_id, request):
    articles = Article.objects.filter(topic_id=topic_id).order_by('-upload_time')
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
    return context

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
    context = get_topic_article(1, request)
    return render(request, 'pages/category.html', context)

def iot(request):
    context = get_topic_article(2, request)
    return render(request, 'pages/category.html', context)

def cloud_computing(request):
    context = get_topic_article(3, request)
    return render(request, 'pages/category.html', context)

def big_data(request):
    context = get_topic_article(3, request)
    return render(request, 'pages/category.html', context)

def mobile(request):
    context = get_topic_article(3, request)
    return render(request, 'pages/category.html', context)

def sillicon_valley(request):
    context = get_topic_article(3, request)
    return render(request, 'pages/category.html', context)

def about(request):
    return render(request, 'pages/about.html')








