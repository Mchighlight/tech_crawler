###
# celery shit
###
from article.models import Article
from website.models import SearchItem, Website


def cronjob(data):
    # site 0 update all
    print(data)
    crawler_info = {
        'article_num' : int(data.get('article_num')),
        'word' : data.get('word'),
        'site' : int(data.get('site')),
        'search_item' : int(data.get('search_item'))
    }

    print(crawler_info)

    original_article = Article.objects.values('website')
    new_contents = crawler(crawler_info, [i['address'] for i in original_article])
    '''
    articles = []
    for content in new_contents :
        new_article = Article(
            subject = content['subject'],
            website = content['site'],
            address = content['address'],
            photo_url = content['photo_url']
        )
        articles.append(new_article)
    Article.objects.bulk_Create(articles)
    '''

def crawler(crawler_info, original_article):
    after_crawler = []
    for i in range(10):#預設爬10篇
        article = {
            'subject' : 'test subject' + str(i),
            'website' : 1,
            'address' : 'www.google.com',
            'photo_url': 'https://i.imgur.com/8jIFgo0.jpg'
        }
        after_crawler.append(article)

    #交叉比對 這是錯的我拿全部去比 TODO:要修改
    new_article = (list(set(li1) - set(original_article))) 
    return  new_article