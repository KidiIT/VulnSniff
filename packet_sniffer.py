import subprocess
from scapy.all import sniff
tcpdump_process = subprocess.Popen(['tcpdump', '-i','eth0', '-w', 'capture.pcap'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# packet sniffing processing logic
def packet_callback(packet):
    print(packet.summary())
def start_sniffing(interface=None):
    sniff(iface=interface,prn=packet_callback, store=False)
start_sniffing()
tcpdump_process.terminate()
