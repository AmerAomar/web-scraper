import requests
from bs4 import BeautifulSoup
def get_citations_needed_count(url):

    '''
    This function takes in a url and returns the number of citations needed
    '''

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations = soup.find_all('a', title='Wikipedia:Citation needed')
    return len(citations)


def get_citations_needed_report(url):

    '''
    This function takes in a url and returns a list of passages that need citations
    '''

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations = soup.find_all('a', title='Wikipedia:Citation needed')
    report = []

    for citation in citations:
        passage = citation.find_parent('p')
        report.append(passage.text.strip())

    return report
