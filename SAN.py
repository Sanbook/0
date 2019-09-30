#Python 3.7.X
#Author				: Soesanto 
#Program Name		: Nguyen
#Program Language	: Python
#Manage Program Using Sanbook With SAN-Brother Team



import json,sys,hashlib,os,time
from requests import requests
from getpass import getpass

if sys.platform in ["linux","linux2"]:

	W = "\033[0m"
    G = '\033[32;1m'
    R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''

try:
	import requests
except ImportError:
	print '''
	404                      
'''%(R)
	sys.exit()
reload (sys)
sys . setdefaultencoding ( 'utf8' )

menghitung = []
jmlgetdata = []
n = []

def baliho():
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])

		print R + '   USER  '
		print ' ' + W
		print ('[*] ' + name + ' [*]')
		print ' '

	except (KeyError,IOError):
		print R + 'USER'
		print ' ' + W
		print ('OFFLINE')
		print (W + '     [' + G +'Mohon login'+ W + ']')
		print ' '

def cssMain():
	print '''
	[0.] getEmail
	[1.] Masuk
	[2.] Keluar
	[3.] Update
'''%(R,W,G,)  

def cssLoginWarning():
	print '''
%s[WARNING!!]%s
 			Masukan user name facebook kamu, bisa ID,
 			bisa Email, bisa Nomor Telpon diterminal!
 			Untuk kata sandi  seusai  ENTER  Username
 			harap hati-hati, karena TEXT tidak tampil.%s

* mohon hubungi kami jika terjadi eror atau program
  tidak bekerja dengan sempurna!
'''%(R,W,G)

def UserValidation():
	print '''
	%sTulis Username disini :
'''%(R)

def UserValidati0n():
	print '''
	%sTulis Password disini :
'''%(R)

def cssMenu():
	print '''
	[1.] Profil
	[2.] Toolkit
	[3.] Recycle
'''%(R,W,G,)  

def cssMenuProfile():
	print '''
	[1.] Profil Guard
	[2.] Profil Information
'''%(R,W,G,) 

def cssMenuToolkit():
	print '''
	[1.] Dump Email Member Group
	[2.] Auto Report  Fake Account
	[3.] Brute Force  Group  Member
	[4.] Auto  Brute  Force  Friends
	[5.] Group  Comment  Auto  Spammer
	[6.] Claim   Group    Administration
'''%(R,W,G,)

def cssMenuRecycle():
	print '''
	[1] Delete All  Post
    [2] Delete All Messages 
    [3] Unfriend All Friends
    [4] Delete All Album Photo
    [5] Delete All Photo In Album
    [6] Declane All Friends Request
    '''%(R,R,R)

def id():
	print (cssLoginWarning);id = raw_input(UserValidation);pwd = getpass.getpass(UserValidati0n);API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';
	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};
	sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
         
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
def getdata():
	global a , token

	print '[*] Load Access Token'

	try:
		token = open("cookie/token.log","r").read()
		print '[*] Success load access token '
	except IOError:
		print '[!] failed to open cookie/token.log'
		print "[!] type 'token' to generate access token"
		main()

	print '[*] fetching all friends data'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print '[!] Your access token is expired'
		print "[!] type 'token' to generate access token"
		main()

	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

	for i in a['data']:
		menghitung.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(menghitung)),;sys.stdout.flush();time.sleep(0.0001)

	print '\r[*] '+str(len(menghitung))+' data of friends successfully retrieved'
	main()

def main():
  global target_id

  try:
	cek = raw_input(R + 'Nguyen' + W +' : ')

	if cek.lower() == 'getEmail':
		if len(menghitung) == 0:
			getEmail()
		else:
			print '[*] You have retrieved %s friends data'%(len(menghitung))
			main()



	elif cek.lower() == 'Masuk':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				cssMenu()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()


	elif cek.lower() == 'Keluar':
		print '''
[Warn] you must create access token again if 
       your access token is deleted
'''
		a = raw_input("[!] type 'delete' to continue : ")
		if a.lower() == 'delete':
			try:
				os.system('rm -rf cookie/token.log')
				print '[*] Success delete cookie/token.log'
				main()
			except OSError:
				print '[*] failed to delete cookie/token.log'
				main()
		else:
			print '[*] failed to delete cookie/token.log'
			main()

def getEmail():
	os.system('clear')
	try:
		token=open('cookie/token.log','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(0.1)
		os.system('rm -rf cookie/token.log')
		login()


	ajaxResponseEmail=requests.get('https://graph.facebook.com/me?access_token={token}')
	result = json.loads(r.text)

	os.system('clear')
	print(p+40*'_')
	print(m+'['+p+'+'+m+']'+h+' From '+p+': '+ajaxResponseEmail['name'])
	print(p+40*'_'+'\n')

	ResponseEmail=requests.get('https://graph.facebook.com/me/friends?access_token={token}')
	result = json.loads(r.text)
	mail=open('result/mail.txt','w')
	for s in ResponseEmail['data']:
		vt=requests.get('https://graph.facebook.com/+s['id']+?access_token={token}')
		result = json.loads(r.text)


		try:
			print(+vt['email'])
			email.append(vt['email'])
			mail.write(vt['email']+'\n')

		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
		except KeyError:
			pass
	mail.close()
	print('\nProgram Selesai')
	print('Total email : 'str(len(email)))
	print(' File saved : ','result/mail.txt')



if __name__ == '__main__':

	banner()
	main()
