import nmap
scanner = nmap.PortScanner()         

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
 
