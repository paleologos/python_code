import re

arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45     L"

ip_a = "2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000 link/ether 00:15:5d:43:e1:75 brd ff:ff:ff:ff:ff:ff inet 192.168.0.143/24 brd 192.168.0.255 scope global eth0 valid_lft forever preferred_lft forever inet6 fe80::215:5dff:fe43:e175/64 scope link valid_lft forever preferred_lft forever"

url = "URL addresses for extractions is http://someaddr.com ,  https://someaddr2.com"

print("\n========= REGEX PATTERN EXTRACTIONS ===========\n")

print("\n====== arp table regex exctract =====\n")
print("\n--extract ip--\n")
print("function match() - only fetch pattern tah string beggins with")
res_arp = re.match(r"[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}", arp)
print(f"Extracted IP: {res_arp.group()}")
print("\n--extract MAC--\n")
print("function search() can fetch pattern in any place in the string ")
res_arp = re.search(r"\s\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2}\s", arp)
print(f"Extracted MAC: {res_arp.group()}")
res_arp = re.findall(r"\s{1,}\w{1}", arp)
print(f"Extracted Last character: {res_arp[2]}")

print("\n========= ip a result extracting ===========\n")
print("\n--extract ip--\n")
res_ip_a = re.search(r"\s\w{1,11}", ip_a)
print(f"Interface Name: {res_ip_a.group()}")

res_ip_a = re.search(r"\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}\s", ip_a)
print(f"Extracted IPv4 address: {res_ip_a.group()}")

res_ip_a = re.search(r"\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s", ip_a)
print(f"Extracted IPv4 Broadcast address: {res_ip_a.group()}")

res_ip_a = re.search(
  r"\s\w{4}\:\:\w{1,4}\:\w{1,4}\:\w{1,4}\:\w{1,4}\/\d{1,2}\s", ip_a)
print(f"Extracted IPv6 address: {res_ip_a.group()}")

res_ip_a = re.findall(r"\s\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2}\s", ip_a)
print(f"Extracted MAC address: {res_ip_a[0]}")
print(f"Extracted MAC broadcast address: {res_ip_a[1]}")

res_ip_a = re.search(r"\s\w{3}\s\w{4}\s", ip_a)
print(f"Extracted Maximum Transmition Unit - MTU: {res_ip_a.group()}")

print("\n========= URL  extracting ===========\n")
print("\n--extract http(s) protocol--\n")

res_ip_a = re.findall(r"\w{4,}\:\/\/", url)
print(f"HTTP Protocol: {res_ip_a[0]}")
print(f"HTTPS Protocol: {res_ip_a[1]}")

print("\n--extract domains--\n")
res_ip_a = re.findall(r"\/\w{1,}\.", url)
print(f"Domain 1: {res_ip_a[0].replace('/','').replace('.','')}")
print(f"Domain 1: {res_ip_a[1].replace('/','').replace('.','')}")

print("\n--extract domain extensions--\n")
res_ip_a = re.findall(r"\.\w{2,}", url)
print(f"Domain extension 1: {res_ip_a[0].replace('.','')}")
print(f"Domain extension 2: {res_ip_a[1].replace('.','')}")
