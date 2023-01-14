import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.amazon.com/Microsoft-Surface-Intel-Newest-Version/dp/B078Z37H9T/ref=sr_1_14?keywords=xiaomi+tab&link_code=qs&qid=1673478951&sourceid=Mozilla-search&sr=8-14'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Cookie' : 'session-id-time=2082787201l; session-id=134-8642357-8466425; ubid-main=133-3518247-7284347; i18n-prefs=USD; sp-cdn="L5Z9:BD"; csm-hit=adb:adblk_no&t:1673480844035&tb:WKJH31EZ7XFXFBY39AQ3+s-H771HB0T0DF70VVPZJMX|1673480844035; session-token="i50ZJlgSnKQWlmGGQl481VgzJPU5WmVvCuzCbSyhrwvqTDkkk1te3y/vbzsv93by3gpmxcVabG9YGquv4XjZ9bZqZZeYeREy/J3zXtzmOtuOyvPCrunh+9D+QShVAXL+B+yqG1Ceapplj6FGOlrnm9KRp9jzyKDpqGBvVohmMGHZDVuMCC1L6VS9aNSZ3zsiyUo/lRegYqV1Dl0/zeosC4qCliOU5/NDqm5poDjYQ34="'
}

res = requests.get(url, headers=headers)
data = res.text
soup = bs(data, 'html.parser')
title_data = soup.find('span', {'id': 'productTitle'})
product_title = title_data.text.strip()
specification = soup.find('table', {'class': 'a-normal a-spacing-micro'})
product_rows = specification.findAll('tr')
product_Specefi = {}
for product_row in product_rows:
    product_data = product_row.findAll('td')
    if len(product_data) > 1:
        product_Specefi[product_data[0].text.strip()]= product_data[1].text.strip()

product_Specefi['title'] = product_title

print(product_Specefi)
            