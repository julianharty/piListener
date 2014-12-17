import subprocess, json, fcntl, socket, struct, sys, urllib2

def getHwAddr(ifname):
    try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
	return ':'.join(['%02x' % ord(char) for char in info[18:24]])
    except:
        return ''

data = {
        'boots': len(subprocess.check_output(['last','reboot']).split(b'\n')) -3,
        'uptime': subprocess.check_output('uptime').rstrip(),
        'cid': open('/sys/block/mmcblk0/device/cid').read().rstrip(),
        'MAC': {'eth0' : getHwAddr('eth0'),'wlan0': getHwAddr('wlan0')},
        'isBoot': True if len(sys.argv)>=3 else False
        }

req = urllib2.Request('http://'+(sys.argv[1] if len(sys.argv)>=2 else 'atslash.com:4000/'))
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

