from time import sleep

import requests

print('==================GET====================')
# GET
URL = "https://deploy-preview-1--yarmarok-test.netlify.app/"

response = requests.request(method="GET", url=URL)
print(response.status_code)
print(response.text)
print("=" * 50)
sleep(3)
