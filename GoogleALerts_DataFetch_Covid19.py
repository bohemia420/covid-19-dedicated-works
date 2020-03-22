import requests
import time

cookies = {
    # your cookies
}

headers = {
    # your header

params = (
    ('params', '[null,null,%s,604800]'%(int(time.time()))),
    ('s', 'AB2Xq4gH_n9KG4Snz-NldMyMve2oRPbUpIowwRQ'),
)

response = requests.get('https://www.google.co.in/alerts/history', headers=headers, params=params, cookies=cookies)

from bs4 import BeautifulSoup
from datetime import datetime, timedelta
count = 0
f = open("my-google-alerts-%s.csv"%(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")),"w")
soup = BeautifulSoup(response.content, "html.parser")
b = soup.findAll('div', {'class':'history_message'})
for bb in b:
    ts = bb["data-timestamp"]
    bsoup = BeautifulSoup(str(bb), "html.parser")
    br = bsoup.findAll('li',{'class':'result'})
    for brr in br:
        brsoup = BeautifulSoup(str(brr), "lxml")
        link = brsoup.li.h4.a["href"]
        source = brsoup.li.h4.div.text
        title = brsoup.li.h4.text
        text = list(brsoup.li.children)[3].text
        f.write("%s;%s;%s;%s;%s\n"%(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(ts))), 
            link, source, title, text)
        )
        count = count + 1
print("processed total %d google alerts" %(count))
f.close()
