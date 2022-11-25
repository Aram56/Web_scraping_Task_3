import requests
import bs4

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Connection': 'keep-alive',
'Cookie': '_ga=GA1.2.1355361232.1664224760; _ym_uid=1664224760926288798; _ym_d=1664224760; habr_web_home_feed=/all/; hl=ru; fl=ru; visited_articles=537174:280238; _gid=GA1.2.154474891.1669401511; _gat_gtag_UA_726094_1=1; _ym_isad=2',
'Referer': 'https://yandex.ru/',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'cross-site',
'TE': 'trailers',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}


KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Гаджеты', 'Карьера в IT-индустрии'}

def selection_articles():

    response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    articles = soup.find_all(class_='tm-article-snippet tm-article-snippet') ##########
    
    for article in articles:
        hubs = article.find_all(class_ = "tm-article-snippet__hubs-item") #######
        hubs = {hub.find('a').text.strip() for hub in hubs} 
        
        if hubs & KEYWORDS:
            article_date = article.find(class_ = "tm-article-snippet__datetime-published") #####
            article_tag_a = article.find('h2').find('a') #####
            article_datetime = article_date.text
            article_name = article_tag_a.text
            href = article_tag_a.attrs['href']
            url = 'https://habr.com' + href
            print('------------------')
            print('Подходящая статья')
            print('Дата: <',article_datetime,'> - Заголовок: <',article_name,'> - ссылка: <',url,'>')
        
                        
if __name__ == "__main__":
    selection_articles()
    
    
    
    