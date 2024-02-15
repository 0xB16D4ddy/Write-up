#!/usr/bin/env python3
import requests 
import re

username = "natas0"
password = username

s = requests.session()

url = 'http://%s.natas.labs.overthewire.org' % username

r = s.get(url, auth = (username, password))
content = r.text

print(re.findall('<!--The password for natas1 is (.*) -->',content)[0])