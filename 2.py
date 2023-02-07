from article import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
art = Article(url)

art.download()

print(art.html)