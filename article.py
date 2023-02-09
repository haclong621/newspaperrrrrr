
import network
import urls
import extractors

from extractors import ContentExtractor
from configuration import Configuration


class ArticleDownloadState(object):
    NOT_STARTED = 0
    FAILED_RESPONSE = 1
    SUCCESS = 2

class Article(object):

    def __init__(self, url, title = '',config=None):
        self.config = config or Configuration()
        self.url = urls.prepare_url(url)
        self.html = ''
        self.extractor = ContentExtractor(self)
        self.title = title
        self.imgs = self.images = []
        self.top_img = self.top_image = ''
        self.doc = None

    def download(self, input_html=None):
        if input_html is None:
            html = network.get_html(self.url)
        self.html = html

    def parse(self):
        self.doc = self.config.get_parser().fromstring(self.html)

        self.title = self.extractor.get_title(self.doc)

    #     self.fetch_images()

    # def fetch_images(self):
    #     imgs = self.extractor.get_img_urls(self.doc)
        # imgs = self.extractor.get_img_urls(self.html)
