import subprocess
import json
import requests

data = {
        'boots': len(subprocess.check_output(['last','reboot']).split(b'\n')) -3,
	'uptime': subprocess.check_output('uptime'),
	'cid': open('/sys/block/mmcblk0/device/cid').read().rstrip()
}

url = 'http://atslash.com:4000/'
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(data), headers=headers)
