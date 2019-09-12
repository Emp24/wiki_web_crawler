import requests
from bs4 import BeautifulSoup 
import time

# TODO: Implement continue_crawl
def continue_crawl(search_history,target_url):
    if search_history[-1] == target_url:
        return False
    elif len(search_history)>25:
        return False
    elif search_history[-1] in search_history[:-1]:
        return False
    else:
        return True
    
# TODO: download page and find first link
def find_first_link(url):
    #get the HTML
    response = requests.get(url)
    html = response.text
    #create a bs4 object
    soup = BeautifulSoup(html, 'html.parser')
    #find the very first link in the article
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            link = element.find("a", recursive=False).get('href')
            break

    return link




def web_crawl(article_chain ,target_url):
    while continue_crawl(article_chain,target_url):
        first_link = 'https://en.wikipedia.org'+ find_first_link(article_chain[-1])
        article_chain.append(first_link)
        print(article_chain)
        time.sleep(2)
   


article_chain = ['https://en.wikipedia.org/wiki/Wolf']

web_crawl(article_chain,'https://en.wikipedia.org/wiki/Philosophy')
