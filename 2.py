from article import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
npp = 'https://jobs.hybrid-technologies.vn/blog/nhung-lenh-git-co-ban-can-nho/'

art = Article(url)

art.download()
# art.parse()

print(art.title)