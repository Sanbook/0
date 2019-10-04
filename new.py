#!/usr/bin/facebook/sanbook/nguyen
#
# Copyright 2010 Facebook
# Copyright 2019 Sanbook
# Author		: Soesanto 
# Program Name	: Nguyen
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0

import os
import sys
import json
import time
import getpass
import hashlib
import requests


def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		exit()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		main()
# HMAC can only handle ascii (byte) strings
# https://bugs.python.org/issue5285
def id():
	print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)

############################################################
def hapus_postingan():
	global token
	print ('\r[*] All post id successfully retrieved          ')
	print ('[*] Start')
	try:
		gp=requests.get('https://graph.facebook.com/me/posts?access_token='+token)
		a = json.loads(gp.text)
		for o in a['data']:
			break
			r = requests.post('https://graph.facebook.com/{id}?method=delete&access_token={token}'.format(id=data['id'],token=token))
			a = json.loads(r.text)
			try:
				cek = a['error']['message']
				print ('['+a['id']']')
			except TypeError:
				print ('Berhasil ['+a['id']']')
				print ('[*] done')
				
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
######################################3


def main():
    print "\n"
    print "----------- MENU ----------"
    print "[Login] [Logout] [Program]"
    print "\n   [Update] [Exit]"
    
    main = raw_input("PILIH MENU> ")
    print "\n"

    if main == 1:
        id()
    elif main == 2:
        hapus_postingan()
    elif main == 3:
        delete_post()
    elif main == 4:
        exit()
    else:
        print "Salah pilih!"


if __name__ == "__main__":

    while(True):
        menu()
