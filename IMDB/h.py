import os,sys,webbrowser,requests,bs4
st  = sys.argv[1]
path, filename = os.path.split(st)
res = requests.get('http://www.google.co.in/search?q=' + 'IMDB' + filename)
soup = bs4.BeautifulSoup(res.text)
link = soup.select('.r a')
webbrowser.open('http://www.google.co.in/'+link[0].get('href'))
