import requests
import bs4

HEADERS = {'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Connection': 'keep-alive',
'Host': 'ads.betweendigital.com',
'Referer': 'https://habr.com/',
'Sec-Fetch-Dest': 'script',
'Sec-Fetch-Mode': 'no-cors',
'Sec-Fetch-Site': 'cross-site',
'TE': 'trailers',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}

KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Робототехника'}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_='tm-article-snippet tm-article-snippet') ##########
print(len(articles))  

 
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
        print('Подходящая статья')
        print('Дата: <',article_datetime,'> - Заголовок: <',article_name,'> - ссылка: <',url,'>')
        
                        
    
    
    
    