#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Date    : 2020-04-27 10:00:03
# @Author  : Awrrays 
# @Link    : http://cnblogs.com/Awrrays
# @Version : 1.0

import fofa
import time
from colorama import init, Fore
import sys


usage = r'''
  	  __        __           _                       
   / _| ___  / _| __ _  __| |_   _ _ __ ___  _ __  
  | |_ / _ \| |_ / _` |/ _` | | | | '_ ` _ \| '_ \ 
  |  _| (_) |  _| (_| | (_| | |_| | | | | | | |_) |
  |_|  \___/|_|  \__,_|\__,_|\__,_|_| |_| |_| .__/ 
                                            |_|    
'''
helps = 'Please modify "EMAIL,KEY,query_string" before use...'

EMAIL = 'djyunwei03@gmail.com'
KEY = 'a5791f410ee810ec7421e1c2983f9344'
query_string = ''

result = []

init()
print(Fore.CYAN + usage)

if query_string == '' or EMAIL == '' or KEY == '':
	print(Fore.RED + '  ' + helps)
	sys.exit()

client = fofa.Client(EMAIL, KEY)

print(Fore.CYAN + "[+] Start to get the result of " + Fore.YELLOW + query_string + Fore.CYAN + " to {0}.txt".format(time.strftime("%Y-%m-%d")))
for page in range(1, 101):
	
	data = client.get_data(query_string, page=page, fields="domain, ip, port, city")

	if data['results'] == []:
		break
	else:
		print(Fore.CYAN + "[+] Crawling page {0}...".format(page))
		for domain, ip, port , city in data['results']:
			if domain == '':
				if port == '80' or port == '443':
					result.append("http://" + ip)
				else:
					result.append("http://" + ip + ":" + port)
			else:
				result.append("http://" + domain)
print(Fore.CYAN + "[+] Writing file...")
try:
	with open(time.strftime("%Y-%m-%d") + '.txt', 'w') as fa:
		for res in set(result):
			fa.write(res + '\n')
except Exception as err:
	print(Fore.RED + "[!] " + err)
finally:
	fa.close()

