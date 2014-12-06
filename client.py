import subprocess, json, urllib2, fcntl, socket, struct

def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])


data = {
        'boots': len(subprocess.check_output(['last','reboot']).split(b'\n')) -3,
        'uptime': subprocess.check_output('uptime').rstrip(),
        'cid': open('/sys/block/mmcblk0/device/cid').read().rstrip(),
        'MAC': getHwAddr('wlan0')
        }

req = urllib2.Request('http://atslash.com:4000/')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

