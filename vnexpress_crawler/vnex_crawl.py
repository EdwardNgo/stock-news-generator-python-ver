import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import pprint
import sys
import os
def get_url():
    start_url='https://vnexpress.net/kinh-doanh/chung-khoan-p'
    file=open('/home/viethoang/web_crawler/vnexpress_crawler/url.txt', 'w')
    for i in range(1,61):
        stock_news_url=[]
        url=start_url+''+str(i)
        print(url)
        # try:
        html=urlopen(url)
        print(url)
        soup = BeautifulSoup(html.read(),features="html.parser")
        for section in soup.findAll('section',attrs={'class':'sidebar_1'}):
            for link in section.findAll('a',attrs={'class':'icon_commend'}):
                stock_news_url.append(link['href'].replace('#box_comment',''))
        # print(stock_news)
        # except:
        # print('can not get the link')
        # for news in stock_news:
        #     # soup=BeautifulSoup(nes,features="html.parser")
        #     # url=soup.find_all('a',href=True)
        #     # print(url['href'])
        #     stock_news_url.append(news['href'].replace('#box_comment',''))
        # print(stock_news_url)
        for stock_url in stock_news_url:
            file.write(stock_url+'\n')
    file.close()


def scrape():
    dataset=[]
    print(type(dataset))
    url_list=open('/home/viethoang/web_crawler/vnexpress_crawler/url.txt','r').read().split('\n')
    url_list=url_list[0:-2]
    print(url_list)
    file=open('/home/viethoang/web_crawler/vnexpress_crawler/result.json','w',encoding='utf-8')
    id=1
    for url in url_list:
        print(url)
        news_item={'url':'','title':'','time':'','description':'','content':''}
        html=urlopen(url)
        soup=BeautifulSoup(html.read(),'html.parser')
        news_item['url']=url

        try:
            news_item['title']=soup.find('h1',attrs={'class':'title_news_detail'}).text.replace('\n','')
            news_item['time']=soup.find('span',attrs={'class':'time left'}).text
            news_item['description']=soup.find('p',attrs={'class':'description'}).text
        except:
            news_item['time']=''
            news_item['description']=''
            news_item['title']=''
        contents_html=soup.findAll('p',attrs={'class':'Normal'})
        try:
            author=contents_html[-1].text
        except:
            print('NOT in right format')
        content_list=[]
        for content in contents_html[0:-1]:
            content_list.append(content.text)

        news_item['content']=' '.join(content_list).replace('\n','')
        news_item['content']=news_item['content'].replace('\\','')
        news_item['content']=news_item['content'].replace('\t','')
        dataset.append(news_item)
    # print(dataset)
    json.dump(dataset,file, sort_keys=True,ensure_ascii=False,indent=4)
    file.close()

def get_corpus():
    sen_file=open("/home/viethoang/web_crawler/vnexpress_crawler/corpus.txt","w")
    with open('result.json','r') as f:
        articles=json.load(f)
        for article in articles:
            sentence=article['content'].split('. ')
            for sent in sentence:
                sen_file.write(sent + '\n')

if __name__ == '__main__':
    get_url()
    scrape()
    get_corpus()
