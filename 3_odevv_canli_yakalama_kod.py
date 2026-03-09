from scapy.all import Dot3, LLC, Padding, sendp, get_if_list

print("Arayuzler:")
for i in get_if_list():
    print(i)
                                                      #SUDE AY
dot3_frame = Dot3(
    dst='01:80:c2:00:00:01',
    src='ff:ff:ff:ff:ff:ff',
    len=3
) / LLC(dsap=0, ssap=1, ctrl=2) / Padding(b'\x00' * 43)

sendp(dot3_frame, iface="Wi-Fi", count=3, verbose=True)
