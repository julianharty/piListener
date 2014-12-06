import subprocess
import json

data = {
        'boots': len(subprocess.check_output(['last','reboot']).split(b'\n')) -3
}

req = urllib2.Request('http://abc.com/api/posts/create')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
