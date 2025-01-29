Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import os
import sys
from scapy.all import *

print("------------------------ Packet Sniffer Tool Disclaimer ---------------------------")
print("This packet sniffer tool is intended for educational and ethical purposes only.")
print("Unauthorized use, distribution, or modification of this tool is strictly prohibited.")
print("By using this tool, you agree to the following terms and conditions:")
print("\n1. You will only use this tool on networks and systems for which you have explicit permission.")
print("2. You will not use this tool to violate any laws, regulations, or terms of service.")
print("3. You will not use this tool to harm, disrupt, or exploit any networks or systems.")
print("4. You will not use this tool to intercept, collect, or store any sensitive or confidential information.")
print("5. You will not redistribute or sell this tool without the express permission of the author.")
... print("6. The author is not responsible for any damages or losses incurred as a result of using this tool.")
... print("7. You will respect the privacy and security of all networks and systems you interact with using this tool.")
... 
... accept_terms = input("\nDo you accept these terms and conditions? (y/n): ")
... 
... if accept_terms.lower() != 'y':
...     print("You must accept the terms and conditions before using this tool.")
...     sys.exit()
... 
... print("\n--------------- Packet Sniffing Tool ---------------")
... 
... def packet_sniff(packet):
...     if packet.haslayer(TCP):
...         src_ip = packet[IP].src
...         dst_ip = packet[IP].dst
...         src_port = packet[TCP].sport
...         dst_port = packet[TCP].dport
...         protocol = packet[IP].proto
...         payload = str(packet[TCP].payload)
... 
...         output_string = f"Source IP: {src_ip}\n"
...         output_string += f"Destination IP: {dst_ip}\n"
...         output_string += f"Source Port: {src_port}\n"
...         output_string += f"Destination Port: {dst_port}\n"
...         output_string += f"Protocol: {protocol}\n"
...         output_string += f"Payload: {payload[:50]}...\n"
... 
...         print(output_string, end='')
...         with open('packet_sniffer_results.txt', 'a') as f:
...             f.write(output_string)
... 
... output_file = "packet_sniffer_results.txt"
... 
... sniff(filter="tcp", prn=packet_sniff, store=0, count=10)
... 
... # Displays the output file's name and location after successful sniffing
