# Network DSAP SSAP Odevi

Bu projede GitHub’dan alınan Python örnekleri temel alınarak LLC katmanında DSAP ve SSAP alanlarını içeren paketler incelenmiştir.

## Yapilan islemler
- Python ile DSAP ve SSAP iceren paket olusturuldu.
- Paket `.pcap` dosyasina kaydedilip Wireshark ile analiz edildi.
- Daha sonra canli paket gonderimi denenerek Wireshark uzerinde yakalama yapildi.
- Yakalanan paketler LLC protokolunde goruldu.
- Ozel olusturulmus paketler Wireshark tarafindan `Malformed Packet` olarak isaretlendi.

## Kullanilan araclar
- Python
- Scapy
- Wireshark
- GitHub

## Dosyalar
- `odev.py` : Ilk asama, paket olusturma ve `.pcap` dosyasina kaydetme
- `odevv.py` : Canli paket gonderimi ve Wireshark ile yakalama denemesi
- `dsap_ssap_demo.pcap` : Olusturulan paket dosyasi
- ekran goruntuleri : PyCharm, Wireshark ciktilari ve yardımcı gitten bulunan kodlar

## Sonuc
Bu calismada DSAP ve SSAP alanlarini iceren LLC paketlerinin Python ile olusturulup Wireshark ile analiz edilebildigi gosterilmistir. Ayrica canli yakalama asamasinda Python ile gonderilen paketlerin Wireshark tarafindan yakalanabildigi gorulmustur.
