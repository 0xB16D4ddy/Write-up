#!usr/bin/env python3
import requests
import re
from html import unescape


with open('natas8.html', 'w+') as out:
    username = 'natas8'
    password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

    s = requests.session()

    url = 'http://%s.natas.labs.overthewire.org' % username

    # r = s.get(url+'/index-source.html', auth = (username,password))
    res = s.post(url, auth = (username,password), data = {"secret":"oubWYf2kBq", "submit":"submit"})
    # content = r.text
    content = res.text

    # out.write(unescape(content))
    # out.write(content)
    out.write(re.findall('natas9 is (.*)\n<form', content)[0])
