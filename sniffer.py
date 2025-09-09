from scapy.all import sniff, IP, TCP, UDP
import sqlite3
from datetime import datetime

def log_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        length = len(packet)

        src_port = None
        dst_port = None
        flags = None

        if TCP in packet:
            tcp_layer = packet[TCP]
            src_port = tcp_layer.sport
            dst_port = tcp_layer.dport
            flags = tcp_layer.flags

        elif UDP in packet:
            udp_layer = packet[UDP]
            src_port = udp_layer.sport
            dst_port = udp_layer.dport

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect('packets.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO packets (timestamp, src_ip, dst_ip, src_port, dst_port, length, flags)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (timestamp, src_ip, dst_ip, src_port, dst_port, length, str(flags)))
        conn.commit()
        conn.close()

        print(f"Logged packet: {src_ip} -> {dst_ip} | Length: {length} | Flags: {flags}")

print("Starting packet sniffing...")
sniff(prn=log_packet)
