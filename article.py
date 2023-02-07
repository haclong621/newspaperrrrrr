
import network
import urls


class ArticleDownloadState(object):
    NOT_STARTED = 0
    FAILED_RESPONSE = 1
    SUCCESS = 2

class Article(object):

    def __init__(self, url):
        self.url = urls.prepare_url(url)
        self.html = ''

    def download(self, input_html=None):
        if input_html is None:
            html = network.get_html(self.url)
        self.html = html


    # def set_html(self, html):
    #     """Encode HTML before setting it
    #     """
    #     if html:
    #         if isinstance(html, bytes):
    #             html = self.config.get_parser().get_unicode_html(html)
    #         self.html = html
    #         self.download_state = ArticleDownloadState.SUCCESS