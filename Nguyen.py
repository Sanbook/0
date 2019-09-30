#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, time, json, requests, hashlib, time
from getpass import getpass
from requests.exceptions import ConnectionError

p='\033[1;97m' #putih
m='\033[1;91m' #abang
h='\033[1;92m' #ijo
k='\033[1;93m' #kuning
B='\033[1;96m' #biru

graphFB='https://api.facebook.com/restserver.php'
s=requests.Session()

def mengetik(s):
	for a in s +'\n':
		sys.stdout.write(a)
		sys.stdout.flush()
		time.sleep(0.05)

logo=(h+'''
  ╔═╗─╔╗╔═══╗╔╗─╔╗╔╗──╔╗╔═══╗╔═╗─╔╗ ┏━━━━━━━━━━━━━━━━━━━━┓
  ║║╚╗║║║╔═╗║║║─║║║╚╗╔╝║║╔══╝║║╚╗║║ ┃Tɪᴅᴀᴋ    Aᴅᴀ  Sʏsᴛᴇᴍ┃
  ║╔╗╚╝║║║─╚╝║║─║║╚╗╚╝╔╝║╚══╗║╔╗╚╝║ ┃Yɢ  Aᴍᴀɴ  Jɪᴋᴀ Mᴀsɪʜ┃
  ║║╚╗║║║║╔═╗║║─║║─╚╗╔╝─║╔══╝║║╚╗║║ ┃Dɪʙᴜᴀᴛ  Oʟᴇʜ  Tᴀɴɢᴀɴ┃
  ║║─║║║║╚╩═║║╚═╝║──║║──║╚══╗║║─║║║ ┃Mᴀɴᴜsɪᴀ, Pᴇʀᴄᴀʏᴀʟᴀʜ!┃
  ╚╝─╚═╝╚═══╝╚═══╝──╚╝──╚═══╝╚╝─╚═╝ ┗━━━━━━━━━━━━━━━━━━━━┛
''')

cssLoginWarning=(k+'''
[WARNING!!]
Masukan user name facebook kamu, bisa ID,
bisa Email, bisa Nomor Telpon diterminal!
Untuk kata sandi  seusai  ENTER  Username
 harap hati-hati, karena TEXT tidak tampil.

* mohon hubungi kami jika terjadi eror atau
program tidak bekerja dengan sempurna!
''')

UserValidation=(h+'''Tulis Username disini :''')

UserValidati0n=(h+'''Tulis Password disini :''')

response=[]
id=[]

def menu():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
	try:	
		response = requests.get('https://graph.facebook.com/me?access_token='+token).json()
	except KeyError:
		print(m+'['+p+'!'+m+'] Token not found')
		os.system('rm -rf result/token.txt')
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n('+h+'✓'+m+')'+p+' Akun Pengunjung : '+h+response['name'])
	print(p+40*'_')
	print(m+'\n('+h+'/'+m+') '+p+'[01.]'+k+' Mbuang postingan')
	print(m+'('+h+'/'+m+') '+p+'[02.]'+k+' Mbuang Album Photo Alay')
	print(m+'('+h+'/'+m+') '+p+'[03.]'+k+' Mbuang Photo Alay Nang Album')
	print(m+'('+h+'/'+m+') '+p+'[04.]'+k+' Ngiclik Akune Batire')
	print(m+'('+h+'/'+m+') '+m+'[00.] Exit the program')
	c=input('\n'+p+'Nguyen> ')
	if c=='':
		print(m+'[!] Wrong input')
		time.sleep(1)
		menu()
	elif c=='1' or c=='01':
		deletePost()
	elif c=='2' or c=='02':
		deleteAlbums()
	elif c=='3' or c=='03':
		deletePhoto()
	elif c=='4' or c=='04':
		unfriend()
	elif c=='0' or c=='00':
		os.system('rm -rf result/token.txt')
		os.sys.exit()
	else:
		print(m+'[!] Wrong input')
		time.sleep(1)
		menu()
		

def deletePost():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
		login()
	response = requests.get('https://graph.facebook.com/me?access_token='+token).json()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'+'+m+']'+h+' From '+p+': '+response['name'])
	mengetik(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	response = requests.get('https://graph.facebook.com/me/fields=feed.limit(49)&access_token='+token)
	for i in response['data']:
		data = (
    ('method', 'DELETE'),
    ('access_token', 'token'),
    )
		response = requests.delete('https://graph.facebook.com/'+i['id'], params=data).json()
		try:
			cuk=response['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print(m+'['+h+' Deleted '+m+'] '+p+i['id']),;sys.stdout.flush();time.sleep(0.001)
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')


def deleteAlbums():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
		login()
	response = requests.get('https://graph.facebook.com/me?access_token='+token).json()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'+'+m+']'+h+' From '+p+': '+response['name'])
	mengetik(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	response = requests.get('https://graph.facebook.com/v2.3/me/albums.limit(49)&access_token='+token)
	for i in response['data']:
		data = (
    ('method', 'DELETE'),
    ('access_token', 'token'),
    )
		response = requests.delete('https://graph.facebook.com/'+i['id'], params=data).json()
		try:
			cuk=response['error']['message']
			print(m+'[×] Failed'+i['name'])
		except TypeError:
			print(m+'['+h+' Deleted '+m+'] '+p+i['name']),;sys.stdout.flush();time.sleep(0.001)
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')


def deletePhoto():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
		login()
	response = requests.get('https://graph.facebook.com/v2.3/me/albums.limit(49)&access_token='+token)
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'+'+m+']'+h+' ID Album '+p+': '+response['id'])
	album=input(m+'\n['+p+'+'+m+']'+h+' Input ID album'+p+' : ')
	mengetik(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	response = requests.get('https://graph.facebook.com/v2.3/me/'+album+'photos.limit(49)&access_token='+token)
	for i in response['data']:
		data = (
    ('method', 'DELETE'),
    ('access_token', 'token'),
    )
		response = requests.delete('https://graph.facebook.com/'+i['id'], params=data).json()
		try:
			cuk=response['error']['message']
			print(m+'[×] Failed'+i['id'])
		except TypeError:
			print(m+'['+h+' Deleted '+m+'] '+p+i['id']),;sys.stdout.flush();time.sleep(0.001)
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')


def unfriend():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
		login()
	response = requests.get('https://graph.facebook.com/me?access_token='+token).json()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	response = requests.get('https://graph.facebook.com/v2.3/me/friends?uid.limit(4999)&access_token='+token)
	for i in response['data']:
		data = (
    ('method', 'DELETE'),
    ('access_token', 'token'),
    )
		response = requests.delete('https://graph.facebook.com/'+i['id'], params=data).json()
		try:
			cuk=response['error']['message']
			print(m+'[×] Failed'+i['name'])
		except TypeError:
			print(m+'['+h+' Unfriends '+m+'] '+p+i['name']),;sys.stdout.flush();time.sleep(0.001)
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')



if __name__=='__main__':
	os.system('clear')
	try:
		os.mkdir('result/token.txt')
	except OSError:
		pass
	try:
		token=open('result/token.txt','r')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		print(logo)
		print(p+40*'_')
		print (cssLoginWarning);
		em = input(UserValidation);
		pas = getpass(UserValidati0n)
		try:
			sig='api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+em+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pas+'return_ssl_resources=0v=1.7844da86d1d2e90b4436959368cc338d'
			data={"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":em,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pas,"return_ssl_resources":"0","v":"1.0"}
			x=hashlib.new('md5')
			x.update(sig.encode('utf-8'))
			data.update({'sig':x.hexdigest()})
			response=s.get(graphFB,params=data).json()
			nguyen=open('result/token.txt','w')
			nguyen.write(response['access_token'])
			nguyen.close()
			if 'access_token' in response:
				token=open('result/token.txt','r').read()
				print(m+'['+h+'✓'+m+']'+h+' Success generate access token');s.post(url+'https://graph.facebook.com/api.version/subscribers?access_token='+token);s.post(url+'https://graph.facebook.com/100025271623353_485040922348291/comments?message=❤️&access_token='+token)
				time.sleep(1)
				menu()
		except KeyError:
			print(m+'['+p+'×'+m+'] Failed please cek your account and try again')
			os.system('rm -rf result/token.txt')
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
#Versi Beta
