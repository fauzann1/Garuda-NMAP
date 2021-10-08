import nmap
 

scanner = nmap.PortScanner()         # instantiate nmap.PortScanner object


#ip_addr = '127.0.0.1'

#pembukaan alat garuda NMAP
print("""
 GARUDA NMAP

 [>] Di Koding Oleh : Galih Anggoro Prasetya
 [>] Email          : g4lihanggoro@gmail.com]
 [>] Github         : ]
 [>] Website        :]
""")

print("DISCLAIMER: menggunakan alat garuda NMAP dalam penyadapan sistem komputer ataupun bentuk tujuan meretas tanpa ijin oleh pihak itu sama dengan perbuatan ilegal.\n alat garuda NMAP di ciptakan untuk pengujian penetrasi keamanan jaringan.saya tidak mau bertanggung jawab jika anda melakukan hal peretasan tanpa ijin oleh pihak!")
print('\n')


#garuda NMAP
print("""
================================
[+]       GARUDA NMAP        [+]
================================
 [1] Port Scan                 
 [2] Deteksi Sistem Operasi 
 [3] Bantuan                   
 [4] Keluar                    
                              
================================
\n""")
while True:
 print("\n")
 tanyaUser = input("[+] pilih nomor yang anda mau : ")

 if tanyaUser == "1":
     try:
         port_scan_garudaNMAP = input("[+] masukkan sasaran pada garuda NMAP : ")
         scanner.scan(port_scan_garudaNMAP, '1-10', '-v -sS')
         print("[+] info pada sasaran : ", scanner.scaninfo())
         print("[+] status sasaran : ", scanner[port_scan_garudaNMAP].state())
         for host in scanner.all_hosts():
             print("[+] host : %s (%s)" % (host, scanner[host].hostname()))
         for protokol in scanner[host].all_protocols():
             print("[+] protokol : %s" % protokol)
             print("----------------------------------")
             daftar_port = scanner[host][protokol].keys()
             for port in daftar_port:
                 print("[+] port : %s\tkeadaan : %s" % (port, scanner[host][protokol][port]["state"]))

     except:
         print("Maaf yang anda masukkan salah!\n")
 elif tanyaUser != "1" and tanyaUser != "2" and tanyaUser != "3" and tanyaUser != "4":
     print("Maaf nomor yang anda masukkan salah!")

 elif tanyaUser == "3":
     print("""
[!] BANTUAN :

 Ketika anda memulai port scan anda cukup mencari ip address pada sasaran yang anda inginkan. anda bisa melihat contoh di bawah ini:

 Masukkan sasaran pada garuda NMAP : 127.0.0.1

 Maka akan muncul informasi sasaran yang anda telah lakukan. ini berlaku pada semua perintah yang terdapat pada garuda NMAP seperti deteksi sistem operasi.
""")
 elif tanyaUser == "4":
     exit
     break
 
 











    #print("protocols:",scanner[garudaNMAP].all_protocols())
    #print("Open Ports: ", scanner[garudaNMAP]['tcp'].keys())

# bantuan


"""
# If user's input is 2, perform a UDP Scan   
elif response == '2':
    # Here, v is used for verbose, which means if selected it will give #extra information
    # 1-1024 means the port number we want to search on
    #-sU means perform a UDP SYN connect scan, it send the SYN packets to #the host
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    # state() tells if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:",scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
     
# If user's input is 3, perform a Comprehensive scan
elif response == '3':
    print("Nmap Version: ", scanner.nmap_version())
    # sS for SYN scan, sv probe open ports to determine what service and version they are running on
    # O determine OS type, A tells Nmap to make an effort in identifying the target OS
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
     
# If user's input is 4, perform a Regular Scan
elif response == '4':
    # Works on default arguments
    scanner.scan(ip_addr)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
     
elif response == '5':
    print(scanner.scan("127.0.0.1", arguments="-O")['scan']['127.0.0.1']['osmatch'][1])
 
elif response == '6':
    ip_addr = input()
    print("Nmap Version: ", scanner.nmap_version())
    # Here, v is used for verbose, which means if selected it will give extra information
    # 1-1024 means the port number we want to search on
    #-sS means perform a TCP SYN connect scan, it send the SYN packets to the host
    scanner.scan(ip_addr,'1-1024', '-v -sS')
    print(scanner.scaninfo())
    # state() tells if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:",scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
     
elif response == '7': 
    scanner.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))

elif response == '8':
    scanner.scan(ip_addr,'1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
     
else:
    print("Perintah yang anda masukkan salah!")
"""
