from scapy.all import Ether, LLC, SNAP, IP, ICMP, wrpcap

DEFAULT_SOURCE_IP = "10.0.0.2"
DEFAULT_DEST_IP = "8.8.8.8"

def ping_packet(seq=0, src=DEFAULT_SOURCE_IP, dst=DEFAULT_DEST_IP, length=-1):
    icmp_packet = ICMP(seq=seq, type=8, code=0) / "XXXXXX"
    icmp_packet = ICMP(icmp_packet.do_build())

    icmp_length = length
    if length == -1:
        icmp_length = len(icmp_packet)
                                                               #SUDE AY
    ping = (
        Ether(dst="ff:ff:ff:ff:ff:ff")
        / LLC(dsap=0xaa, ssap=0xaa, ctrl=0x03)
        / SNAP(OUI=0x000000, code=0x0800)
        / IP(src=src, dst=dst, len=(20 + icmp_length))
        / icmp_packet
    )

    return ping

packet = ping_packet()
packet.show()
wrpcap("dsap_ssap_demo.pcap", [packet])

print("Oluşturuldu: dsap_ssap_demo.pcap")
