import scapy.all as scapy

source_ip = input("Enter the source IP address: ")
interface = input("Enter the interface you aim to send the packet through: ")
destination_ip = input("Enter the destination IP address: ")
packet_number = int(input("How many packets? "))

if (source_ip.find(":") >= 0):
    scapy.send(scapy.IPv6(src=source_ip, dst=destination_ip)/scapy.TCP()/scapy.UDP(), iface = interface, count = packet_number)

else:
    scapy.send(scapy.IP(src=source_ip, dst=destination_ip)/scapy.TCP()/scapy.UDP(), iface = interface, count = packet_number)
