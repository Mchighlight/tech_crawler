from crawler.celery import app, QUEUE_JOBS, QUEUE_CRONJOBS
from article.models import Article
from website.models import SearchItem, Website

@app.task(queue=QUEUE_CRONJOBS)
def test_period():
    print("testing")


@app.task(queue=QUEUE_JOBS)
def cronjob(data):
    crawler_info = {
        'article_num' : int(data.get('article_num')),
        'word' : data.get('word'),
        'site' : int(data.get('site')),
        'search_item' : int(data.get('search_item'))
    }

    print(crawler_info)

    original_article = Article.objects.values('address')
    #new_contents = crawler(crawler_info, [i['address'] for i in original_article])
    original_article_address = [i['address'] for i in original_article]
    new_contents = crawler.apply_async(args=[crawler_info, original_article_address])
    print(new_contents)
    '''
    articles = []
    for content in new_contents :
        new_article = Article(
            subject = content['subject'],
            website = Website.objects.filter(id=content['site'])[0],
            address = content['address'],
            photo_url = content['photo_url']
        )
        articles.append(new_article)
    Article.objects.bulk_Create(articles)
    '''

@app.task(queue=QUEUE_JOBS)
def crawler(crawler_info, original_article):
    new_article = "hello, word"
    return  new_article