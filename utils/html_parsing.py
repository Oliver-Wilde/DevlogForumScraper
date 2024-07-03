from bs4 import BeautifulSoup

def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    posts = soup.find_all('div', class_='post')
    parsed_data = []

    for post in posts:
        author = post.find('span', class_='author').text
        content = post.find('div', class_='content').text
        date = post.find('span', class_='date').text
        parsed_data.append({'author': author, 'content': content, 'date': date})

    return parsed_data
