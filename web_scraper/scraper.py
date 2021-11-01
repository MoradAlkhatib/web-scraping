import requests
import time
from bs4 import BeautifulSoup

url='https://en.wikipedia.org'
def get_citations_needed_count(url):
    domain = url
    citation_url = f"{domain}/wiki/History_of_Mexico"
    res = requests.get(citation_url)
    html_text = res.text
    file=open('History_of_Mexico.htm',"w")
    file.write(html_text)
    file.close()
    soup = BeautifulSoup(html_text, "html.parser")
    citation = soup.find_all('a', { "title" : "Wikipedia:Citation needed"})
    return len(citation)

    
def get_citations_needed_report(url):
    domain = url
    citation_url = f"{domain}/wiki/History_of_Mexico"
    res = requests.get(citation_url)
    html_text = res.text
    soup = BeautifulSoup(html_text, "html.parser")
    citation = soup.find_all('a', { "title" : "Wikipedia:Citation needed"})
    list_str=[]
    for c in citation:
        par=c.parent.parent.parent
        list_str+=[par.text] 
    return list_str    
print(get_citations_needed_report(url))
time.sleep(1)