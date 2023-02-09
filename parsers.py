import logging
import lxml.etree
import lxml.html
import text
import string
import re
import requests
import parsel

from html import unescape
from lxml.cssselect import CSSSelector

from bs4 import UnicodeDammit


log = logging.getLogger(__name__)

class Parser(object):
    @classmethod
    def xpath_re(cls, node, expression):
        regexp_namespace = "http://exslt.org/regurlar-expressions"
        items = node.xpath(expression, namespaces = {'re':regexp_namespace})
        return items

    @classmethod
    def css_select(cls, node, selector):
        return node.cssselect(selector)

    @classmethod
    def fromstring(cls, html):
        cls.doc = lxml.html.fromstring(html)
        return cls.doc

    @classmethod
    # def getElementsByTag(
    #         cls, node, tag=None, attr=None, value=None, childs=False, use_regex=False) -> list:
    #     NS = None
    #     # selector = tag or '*'
    #     selector = 'descendant-or-self::%s' % (tag or '*')
    #     if attr and value:
    #         if use_regex:
    #             NS = {"re": "http://exslt.org/regular-expressions"}
    #             selector = '%s[re:test(@%s, "%s", "i")]' % (selector, attr, value)
    #         else:
    #             trans = 'translate(@%s, "%s", "%s")' % (attr, string.ascii_uppercase, string.ascii_lowercase)
    #             selector = '%s[contains(%s, "%s")]' % (selector, trans, value.lower())
    #     elems = node.xpath(selector)#, namespaces=NS)
    #     # remove the root node
    #     # if we have a selection tag
    #     if node in elems:#and (tag or childs):
    #         elems.remove(node)
    #     return elems

    # def getElementsByTag(cls, node, tag):
    #     selector = 'descendant-or-self::%s' % (tag or '*') #????????????/
    #     elems = node.xpath(selector)
    #     if node in elems:
    #         elems.remove(node)
    #     return elems

    def getElementsByTag(cls, doc, tag):
        sel = parsel.Selector(text=doc)
        eles = sel.css(tag)
        return eles


    # @classmethod
    # def getText(cls, node):
    #     txts = [i for i in node.itertext()]
    #     return text.innerTrim(' '.join(txts).strip())

    # @classmethod
    # def getAttribute(cls, node, attr=None):
    #     if attr:
    #         attr = node.attrib.get(attr, None)
    #     if attr:
    #         attr = unescape(attr)
    #     return attr