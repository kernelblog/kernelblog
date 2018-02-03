#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib2 import *

print """
                           _   ___    __             
  /\ /\___ _ __ _ __   ___| | / __\  / /  ___   __ _ 
 / //_/ _ \ '__| '_ \ / _ \ |/__\// / /  / _ \ / _` |
/ __ \  __/ |  | | | |  __/ / \/  \/ /__| (_) | (_| |
\/  \/\___|_|  |_| |_|\___|_\_____/\____/\___/ \__, |
  KernelBlog.org developer team | delosemre    |___/ 
                                               """
print "\n\033[97m1. Whoıs Arama\033[1;m"
print "\033[97m2. DNS Arama + Cloudflare Dedektörü\033[1;m"
print "\033[97m3. Bölge(zone) Aktarımı\033[1;m"
print "\033[97m4. Port Tarama\033[1;m"
print "\033[97m5. HTTP Üstbilgi Tutucu\033[1;m"
print "\033[97m6. Honeypot Detektörü\033[1;m"
print "\033[97m7. Robots.txt Tarayıcı\033[1;m"
print "\033[97m8. Link Yakalayıcı\033[1;m"
print "\033[97m9. IP Yer Bulucu\033[1;m"
print "\033[97m10. Gidiş Yolu\033[1;m"
print "\033[97m11. Başlangıç'a Dön\033[1;m"
print "\033[97m12. Çık\033[1;m"

print ""

choice = input('\033[1;91mSeçiminizi girin:\033[1;m ')
if choice == 1:
    domip = raw_input('\033[1;91mAlan Adı Veya IP Adres: \033[1;m')
    who = "http://api.hackertarget.com/whois/?q=" + domip
    pwho = urlopen(who).read()
    print (pwho)


if choice == 2:
    domain = raw_input('\033[1;91mAlan Adı Girin: \033[1;m')
    ns = "http://api.hackertarget.com/dnslookup/?q=" + domain
    pns = urlopen(ns).read()
    print (pns)
    if 'cloudflare' in pns:
        print "\033[1;31mCloudflare Tespit!\033[1;m"
    else:
        print "\033[1;33mKorumalı değil cloudflare\033[1;m"


if choice == 3:
        domain = raw_input('\033[1;91mAlan adı girin: \033[1;m')
        zone = "http://api.hackertarget.com/zonetransfer/?q=" + domain
        try:
            domain = raw_input('\033[1;91mAlan Adı Girin: \033[1;m')
            pzone = urlopen(zone).read()
            print (pzone)
        except 'failed' in pzone:
        	print "\033[1;31mBölge aktarımı başarısız oldu\033[1;m"


if choice == 4:
    domip = raw_input('\033[1;91mAlan Adı veya Ip Adresi Girin: \033[1;m')
    port = "http://api.hackertarget.com/nmap/?q=" + domip
    pport = urlopen(port).read()
    print (pport)


if choice == 5:
    domip = raw_input('\033[1;91mAlan Adı veya Ip Adresi Girin: \033[1;m')
    header = "http://api.hackertarget.com/httpheaders/?q=" + domip
    pheader = urlopen(header).read()
    print (pheader)


if choice == 6:
    ip = raw_input('\033[1;91mIP Adres Giriniz: \033[1;m')
    honey = "https://api.shodan.io/labs/honeyscore/" + ip + "?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by"
    phoney = urlopen(honey).read()
    if '0.0' in phoney:
        print "\033[1;32mOlasılık: 0%\033[1;m"
    if '0.1' in phoney:
        print "\033[1;32mOlasılık: 10%\033[1;m"
    if '0.2' in phoney:
        print "\033[1;32mOlasılık: 20%\033[1;m"
    if '0.3' in phoney:
        print "\033[1;32mOlasılık: 30%\033[1;m"
    if '0.4' in phoney:
        print "\033[1;32mOlasılık: 40%\033[1;m"
    if '0.5' in phoney:
        print "\033[1;33mOlasılık: 50%\033[1;m"
    if '0.6' in phoney:
        print "\033[1;33mOlasılık: 60%\033[1;m"
    if '0.7' in phoney:
        print "\033[1;33mOlasılık: 70%\033[1;m"
    if '0.8' in phoney:
        print "\033[1;33mOlasılık: 80%\033[1;m"
    if '0.9' in phoney:
        print "\033[1;33mOlasılık: 90%\033[1;m"
    if '1.0' in phoney:
        print "\033[1;33mOlasılık: 100%\033[1;m"


if choice == 7:
    domain = raw_input('\033[1;91mAlan Adı Giriniz. (Ör. http(s)://): \033[1;m')
    robot = domain + "/robots.txt"
    probot = urlopen(robot).read()
    print (probot)


if choice == 8:
    page = raw_input('\033[1;91mURL Giriniz: \033[1;m')
    crawl = "https://api.hackertarget.com/pagelinks/?q=" + page
    pcrawl = urlopen(crawl).read()
    print (pcrawl)


if choice == 9:
    ip = raw_input('\033[1;91mIP Adres Giriniz: \033[1;m')
    geo = "http://ipinfo.io/" + ip + "/geo"
    pgeo = urlopen(geo).read()
    print (pgeo)

if choice == 10:
    domip = raw_input('\033[1;91mAlan Adı Veya IP adres: \033[1;m')
    trace = "https://api.hackertarget.com/mtr/?q=" + domip
    ptrace = urlopen(trace).read()
    print (ptrace)


if choice==11:
    print ("    Başlatılıyor...")
    time.sleep(1)
    cmd1=os.system("clear")
    cmd1=os.system("python kernelblog.py")

if choice==12:
    print ("    ---------")
    print ("    Güle Güle")
    print ("    ---------")
    time.sleep(0.5)
    sys.exit()
