import requests

FAIL_ENCODING = 'ISO-8859-1'

def get_html(url):
    response = requests.get(url)
    html = get_html_from_response(response)
    return html

def get_html_from_response(response):
    html = response.text
    return html
