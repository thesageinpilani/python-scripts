import os,sys,webbrowser,requests,bs4,datetime,json
# m = ['january','february','march','april','may','june','july','august','september','october','november','december']
# st  = str(m[datetime.datetime.today().month - 1]) +'_'+str(datetime.datetime.today().day + 1)
# req_bb = 'https://en.wikipedia.org/wiki/' + st
# # webbrowser.open(req_bb)
# res = requests.get(req_bb)
# soup = bs4.BeautifulSoup(res.text)
# link = soup.select('ul')
# linkli = link[1].select('li')
# for i in linkli:
# 	source = str(i.getText(), encoding='utf-8', errors = 'ignore')
# 	print(source)
st  = 'http://history.muffinlabs.com/date/' + str(datetime.datetime.today().month) +'/'+str(datetime.datetime.today().day)
res = requests.get(st)
# webbrowser.open(st)
jsondata = json.loads(res.text)
events = jsondata['data']['Events']
# target = open('myfile.txt','w')
with open(jsondata['date'], 'w', encoding='utf-8') as target:
	target.write(jsondata['date'])
	target.write('\n')
	for i in events:
		target.write(i['year'] + '-' + i['text'])
		target.write('\n')
