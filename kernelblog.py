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

# Menü

menu = """

 _   __                     _______ _                 
| | / /                    | | ___ \ |                
| |/ /  ___ _ __ _ __   ___| | |_/ / |     ___   __ _ 
|    \ / _ \ '__| '_ \ / _ \ | ___ \ |    / _ \ / _` |
| |\  \  __/ |  | | | |  __/ | |_/ / |___| (_) | (_| |
\_| \_/\___|_|  |_| |_|\___|_\____/\_____/\___/ \__, |
                                                 __/ |
   KernelBlog.org developer team | delosemre	|___/ .org

   
   1-) Hedef Site Açık Tarama
   2-) Hedef Site Bilgi Toplama
   3-) Hakkımızda/İletişim
   4-) Çıkış


"""

print (menu)


#komut girdisi

time.sleep(0.3)
print("")
secim = raw_input("    " + "KernelBlog" + "" "\033[1;91m@KernelBlog:~$\033[1;m ")
print("")


#Seçeneklerin Başlatılması

if secim=="1":
	print ("kb-atak.py Başlatılıyor...")
	time.sleep(1)
	cmd1=os.system("clear")
	cmd1=os.system("python kb-atak.py")

if secim=="2":
	print ("kb-bilgi.py Başlatılıyor...")
	time.sleep(1)
	cmd1=os.system("clear")
	cmd1=os.system("python kb-bilgi.py")

if secim=="3":
	print ("Hakkımızda/İletişim Başlatılıyor...")
	time.sleep(1)
	cmd1=os.system("clear")
	cmd1=os.system("python hakkimizda.py")



if secim=="4":
	cmd1=os.system("clear")
	print ("	---------")
	print ("	Güle Güle")
	print ("	---------")
	time.sleep(0.5)
	sys.exit()