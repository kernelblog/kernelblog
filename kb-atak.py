# -*- coding: utf-8 -*-

#-----------------------------#
#   	delosemre.xyz		  #
#	   kernelblog.org		  #
#	   t.me/delosemre		  #
#-----------------------------#




import os
import sys, traceback
import argparse
import time
import httplib
import subprocess
import re, urllib2
import socket
import urllib,sys,json
import telnetlib
import glob
import random
import Queue 
import threading
import requests
import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep


#İş Burada Başlıyor

print ("")

menu = """


\033[1;91m
     )                          (                
  ( /(                   (   (  )\ )             
  )\()) (  (           ( )\( )\(()/(      (  (   
 ((_)\ ))\ )(   (     ))((_)((_)/(_)) (   )\))(  
(_ ((_)((_|()\  )\ ) /((_)((_)_(_))   )\ ((_))\  
| |/ (_))  ((_)_(_/((_))| || _ ) |   ((_) (()(_) 
| ' </ -_)| '_| ' \)) -_) || _ \ |__/ _ \/ _` |  
|_|\_\___||_| |_||_|\___|_||___/____\___/\__, |  
KernelBlog.org developer team |delosemre |___/ .org   
                                     \033[1;m
		
		Tarama Araçları

	1-) Uniscan İle Site Tarama
	2-) Wapiti İle Site Tarama
	3-) Nikto İle Site Tarama
	4-) Wpscan ile Wordpress Siteyi Tarama
	5-) Joomscan İle Joomla Sisteyi Tarama
	6-) Başlangıç'a Dön
	7-) Çık

"""

print (menu)

#komut girdisi

time.sleep(0.3)
print("")
secim = raw_input("    " + "KernelBlog" + "" "\033[1;91m@KernelBlog:~$\033[1;m ")
print("")


#Seçeneklerin Başlatılması

if secim == "1":
	print ("	Uniscan Başlatılıyor...")
	time.sleep(0.5)
	print ("")
	url = raw_input("	Tarama Yapılacak Site: ")
	cmd1=os.system("uniscan -u"+url+" -qweds")


if secim == "2":
	print ("	Wapiti Başlatılıyor...")
	time.sleep(0.5)
	print ("")
	url = raw_input("	Tarama Yapılacak Site: ")
	cmd1=os.system("wapiti http://"+url)


if secim =="3":
	print ("	Nikto Başlatılıyor...")
	time.sleep(0.5)
	print ("")
	url = raw_input("	Tarama Yapılacak Site: ")
	port = raw_input("	Port Yazınız: ")
	cmd1=os.system("nikto "+url+" -p"+port)


if secim =="4":
	print ("	Wpscan Başlatılıyor...")
	time.sleep(0.5)
	print ("")
	url = raw_input("Toplamaarama Yapılacak Wordpress Sitesi: ")
	cmd1=os.system("wpscan --url "+url+"--enumerate ptu")


if secim =="5":
	print ("	Joomscan Başlatılıyor...")
	time.sleep(0.5)
	print ("")
	url = raw_input("	Tarama Yapılacak Joomla Sitesi: ")
	cmd1=os.system("joomscan -u "+url)


if secim =="6":
	print ("	Başlatılıyor...")
	time.sleep(1)
	cmd1=os.system("clear")
	cmd1=os.system("python kernelblog.py")


if secim=="7":
	print ("	---------")
	print ("	Güle Güle")
	print ("	---------")
	time.sleep(0.5)
	sys.exit()



if secim == "":
	print ("SQLI Enjektör Başlatılıyor...")
	time.sleep(0.5)
	url = raw_input("Tarama Yapılacak Site: ")
	cmd1=os.system("sqlmap -u "+url+" --tor --tor-type=SOCKS5 --check-tor --tor-port=9050 --random-agent --level=3 --risk=3 --threads=2")

	