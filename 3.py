import requests
from lxml import html

from parsel import Selector

# selector = Selector(text="""<html>
#         <body>
#             <h1>Hello, Parsel!</h1>
#             <ul>
#                 <li><a href="http://example.com">Link 1</a></li>
#                 <li><a href="http://scrapy.org">Link 2</a></li>
#             </ul>
#         </body>
#         </html>""")
# print(selector.css('h1::text').get())
# # 'Hello, Parsel!'
# print(selector.xpath('//h1/text()').re(r'\w+'))
# # ['Hello', 'Parsel']
# for li in selector.css('ul > li'):
#     print(li.xpath('.//@href').get())
# # http://example.com
# # http://scrapy.org

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
npp = 'https://jobs.hybrid-technologies.vn/blog/nhung-lenh-git-co-ban-can-nho/'

page = requests.get(url)
tree = html.fromstring(page.content)

# sel = Selector(text=page.text)
# print(sel.css('h1::text').get())
# # for li in sel.css('ul > li'):
# #     print(li.xpath('.//@href').get())

print(page.text)