import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_forum(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    posts = soup.find_all('div', class_='post')
    
    data = []
    for post in posts:
        author = post.find('span', class_='author').text
        content = post.find('div', class_='content').text
        date = post.find('span', class_='date').text
        data.append({'author': author, 'content': content, 'date': date})
    
    return pd.DataFrame(data)

if __name__ == '__main__':
    url = 'https://exampleforum.com/thread'  # Replace with the actual forum URL
    df = scrape_forum(url)
    df.to_csv('data/raw/forum_data_raw.csv', index=False)
