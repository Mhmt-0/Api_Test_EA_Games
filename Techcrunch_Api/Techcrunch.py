from pprint import pprint
from requests import get


response = get("https://newsapi.org/v2/everything?q=tesla&from=2023-04-23&sortBy=publishedAt&apiKey=9462bbb1b80946c1ad4ed59652bc84c9")

techcrunch= response.json()


pprint(techcrunch)

author = techcrunch('articles')[1].get('author')
title = techcrunch('articles')[1].get('title')
published_at = techcrunch('articles')[1].get('publishedAt')

print(f'Author: {author}')
print(f'Title: {title}')
print(f'Published Date: {published_at}')






from pprint import pprint
from requests import get


response = get("https://newsapi.org/v2/everything?q=tesla&from=2023-04-23&sortBy=publishedAt&apiKey=9462bbb1b80946c1ad4ed59652bc84c9")

techcrunch = response.json()


pprint(techcrunch)

author = techcrunch.get('articles')[1].get('author')
title = techcrunch.get('articles')[1].get('title')
published_at = techcrunch.get('articles')[1].get('publishedAt')

print(f'Author: {author}')
print(f'Title: {title}')
print(f'Published Date: {published_at}')


author_name = input('Author name: ')
for article in techcrunch.get('articles'):
    if(article.get('author')) == author_name:
        print(article)

