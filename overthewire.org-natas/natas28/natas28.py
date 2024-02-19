import requests

username = 'natas28'
password = 'skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4'

url = 'http://%s.natas.labs.overthewire.org/' % username

with open('natas28.html', 'w+') as out:
    session = requests.Session()
    res = session.get(url, auth=(username, password))
    content = res.text
    out.write(content)