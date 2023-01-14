import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.amazon.com/Microsoft-Surface-Intel-Newest-Version/dp/B078Z37H9T/ref=sr_1_14?keywords=xiaomi+tab&link_code=qs&qid=1673478951&sourceid=Mozilla-search&sr=8-14'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'cookie':'session-id-time=2082787201l; session-id=134-8642357-8466425; ubid-main=133-3518247-7284347; i18n-prefs=USD; sp-cdn="L5Z9:BD"; session-token=ruXyHimW9Vb1DNkvHQZhL2nXZ1TV5pm4JboF/9GNEh6XPfhJBWsr2uGtZH0EBX2DF+WdeUaTLnn6qLt5fQ22AT+g1nyCixuKS/r1YDsZM8OdwvQylfGbOzqIqHmytQ1q2oTG05qLO/0XYCxCs5rUh2tmSkVjH/0pa/xF8lI1qr5MMnGq4KOvPRcYy53LOIJiV+a9XeR4aPopbGSIRMT5TD0OFI8FcgHr7DXK2X2gOVA= '    
}

res = requests.get(url, headers=headers)
data = res.text
soup = bs(data,'html.parser')
heading=soup.find('h1')
print(heading.text.strip())
         