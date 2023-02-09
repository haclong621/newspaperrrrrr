import parsel

from urllib.parse import urljoin, urlparse, urlunparse
from configuration import Configuration
from parsers import Parser
from parsel import Selector

class ContentExtractor(object):
    def __init__(self,config):
        self.config = config or Configuration
        self.parser = Parser()

    def get_title(self,doc):
        # from h1
        title_h1 = ''
        title_h1_list = self.parser.getElementsByTag(doc, tag ='h1::text')
        if title_h1_list:
            title_h1 = title_h1_list[0].text
        # from meta
        title_meta = self.get_meta_content(doc, 'meta[property="og:title"]') or self.get_meta_content(doc, 'meta[name="og:title"]' or '')
        # compare
        if title_h1 == title_meta:
            title = title_h1 or title_meta
        else: title = title_h1
        return title


    def get_meta_content(self,doc,metaname):
        meta = self.parser.css_select(doc, metaname)
        content = None
        if meta is not None and  len(meta) > 0:
        #     content = self.parser.getAttribute(meta[0], 'content')
        # if content:
        #     return content.strip()
        # return ''
            content = meta[0].get('content')
        return content

    # def get_img_urls(self, article_url, doc):
    #     """Return all of the images on an html page, lxml root
    #     """
    #     img_kwargs = {'tag': 'img'}
    #     img_tags = self.parser.getElementsByTag(doc, **img_kwargs)
    #     urls = [img_tag.get('src')
    #             for img_tag in img_tags if img_tag.get('src')]
    #     img_links = set([urljoin(article_url, url)
    #                      for url in urls])
    #     return img_links

