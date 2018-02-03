#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

print """
                           _   ___    __             
  /\ /\___ _ __ _ __   ___| | / __\  / /  ___   __ _ 
 / //_/ _ \ '__| '_ \ / _ \ |/__\// / /  / _ \ / _` |
/ __ \  __/ |  | | | |  __/ / \/  \/ /__| (_) | (_| |
\/  \/\___|_|  |_| |_|\___|_\_____/\____/\___/ \__, |
  KernelBlog.org developer team | delosemre    |___/ 
                                               """

print """
		Hata ve Düzeltmeler için iletişime geçiniz.

		\033[1;91mTelegram: @delosemre
		Twitter: @delosemre
		---
		www.kernelblog.org
		www.forum.kernelblog.org
		info@kernelblog.org
		delosemre@outlook.com
		delosemre@delosemre.xyz\033[1;m


		1-) Geri Dön
		2-) Çıkış
"""

print("")
secim = raw_input("    " + "KernelBlog" + "" "\033[1;91m@KernelBlog:~$\033[1;m ")
print("")


#Seçeneklerin Başlatılması

if secim=="1":
	print ("kernelblog.py Başlatılıyor...")
	cmd1=os.system("clear")
	cmd1=os.system("python kernelblog.py")


if secim=="2":
	cmd1=os.system("clear")
	print ("	---------")
	print ("	Güle Güle")
	print ("	---------")
	sys.exit()