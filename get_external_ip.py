import requests
import sys

try:
    external_ip = requests.get('http://ifconfig.co', headers = self.requests_useragent).content
    return external_ip.strip('\n')
    print(external_ip)
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)
