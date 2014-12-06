import subprocess
import json

data = {
        'boots': len(subprocess.check_output(['last','reboot']).split(b'\n')) -3,
        'uptime': subprocess.check_output('uptime'),
        'cid': open('/sys/block/mmcblk0/device/cid').read().rstrip()
        }

req = urllib2.Request('http://atslash.com:4000/')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
