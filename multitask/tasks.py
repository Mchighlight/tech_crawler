from crawler.celery import app, QUEUE_JOBS, QUEUE_CRONJOBS
from article.models import Article
from website.models import SearchItem, Website
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
import os 
import time
import random


BLOOMBERG_URL = "https://www.bloomberg.com/topics/artificial-intelligence"
TNW_URL = "https://thenextweb.com/artificial-intelligence/"

@app.task(queue=QUEUE_JOBS)
def cronjob(data):
    crawler_info = {
        'article_num' :int(data.get('article_num')),
        'word' : data.get('word'),
        'site' : int(data.get('site')),
        'search_item' : (data.get('search_item'))
    }

    
    #將資料庫的網址抓出轉成LIST ['www.google.com', 'www.google.com', 'www.google.com'......]
    original_article = Article.objects.values('address')
    original_article_address = [i['address'] for i in original_article]

    article = [] 
    if crawler_info['site'] == 0 :
        number_of_article = round(crawler_info['article_num']/2)
        #bloomberg_article = crawler.apply_async(args=[1, number_of_article])
        bloomberg_article = crawler(1, number_of_article)
        if ( len(bloomberg_article) == 0 ):
            number_of_article = crawler_info['article_num']
        #tnw_article = crawler.apply_async(args=[2, number_of_article])
        tnw_article = crawler(2, number_of_article)
    
        article.extend(tnw_article)
        article.extend(bloomberg_article)
        article = [i for i in article if i['address'] not in original_article_address ]                
   
        random.shuffle(article)
        for i in article :
            print(i['subject'])
        print(len(article))
        new_contents = article
    else :
        crawlerc(crawler_info['site'], crawler_info['article_num'])
    
    # Add to database
    
    articles=[]
    if len(new_contents) != 0:
        for content in new_contents :
            new_article = Article(
                subject = content['subject'],
                website = Website.objects.filter(id=content['website'])[0],
                address = content['address'],
                photo_url = content['photo_url']
            )
            articles.append(new_article)
        Article.objects.bulk_create(articles)
    
def crawler( which_website, number_of_article ):
    if (which_website == 1):
        url = BLOOMBERG_URL
    else:
        url = TNW_URL

    data = []
    is_repeat = ""

    display = Display(visible=0, size=(800, 600))
    display.start()


    try:
        browser = webdriver.Firefox()

        if which_website == 1:
            class_name = "index-page__headline"
            tag_name = "h2"
        else:
            class_name = "story-title"
            tag_name = "h4"
        browser.get(url)

        page = 10
        for i in range(1, page):
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            for ele in soup.find_all(tag_name, class_=class_name):
                is_repeat = "" 
                if  which_website == 1 :
                    for i in range(0, len(data)):
                        if  ele.text.strip() == data[i]['subject']:
                            is_repeat = "false"
                    if is_repeat != "false":
                        if ele.parent.div is not None:
                            strtemp = ele.parent.div.div.div.get('style')[21:]
                            data.append({'subject' : ele.text, 'photo_url' : strtemp[:-1], 'website': 1, 'address' : "https://www.bloomberg.com" + ele.parent.get('href')})
                else:
                    for i in range(0, len(data)):
                        if ele.a.text.strip() == data[i]['subject'] :
                            is_repeat = "false"
                    if is_repeat != "false" and ele.parent.parent.a.get('style') is not None :                
                        strtemp = ele.parent.parent.a.get('style')[23:]
                        data.append({'subject' : ele.a.text.strip(), 'photo_url' : strtemp[:-3], 'website': 2, 'address' : ele.a.get('href')})
                                     
                if len(data) == number_of_article:
                    break

            if len(data) == number_of_article:
                break
            if which_website == 1 : 
                browser.find_element_by_xpath('//div[@class="module-view"]/button[contains(text(), "Load More")]').click()
            else:
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)

        browser.quit()
        display.stop()

        return data
    except:
        print("fail Scratching...")
        display.stop()