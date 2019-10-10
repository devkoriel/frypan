import requests
from lxml import html

def isSpam(content, spamLinkDomains, redirectionDepth):
    if redirectionDepth == 0:
        if any(url in content for url in spamLinkDomains):
            return True
        else:
            return False

    session = requests.Session()
    session.max_redirects = 1

    try:
        response = session.get(content)
    except requests.exceptions.TooManyRedirects as exception:
        response = exception.response

    if response.history:
        status_code = response.history[0].status_code
    else:
        status_code = response.status_code

    if status_code in (301, 302):
        return isSpam(response.url, spamLinkDomains, redirectionDepth - 1)
    elif status_code == 200:
        webpage = html.fromstring(response.content)
        hrefs = webpage.xpath('//a/@href')

        if hrefs:
            return isSpam(hrefs[0], spamLinkDomains, redirectionDepth - 1)
        else:
            return False
    else:
        return False