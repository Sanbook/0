import requests , json , sys , hashlib , os , time , getpass

jml = []

reload (sys)
sys . setdefaultencoding ( 'utf8' )

def cssmenu():

	print '''
  COMMAND	      DESCRIPTION
  -------------       -------------------------------------

   LOGIN 		Masuk facebook
   TOKEN 		Membuat Acces Token
   UNFRIENDS 		Menghapus Daftar Teman
'''

def main():
	print (cssmenu)
	cek = raw_input("MENU :")

	if cek.lower() == 'LOGIN':
			login()
		else:
			print '[*] Mencoba login ke token'
			token()
	elif cek.lower() == 'TOKEN':
		token()
	elif cek.lower() == 'UNFRIENDS':
		unfriend()
		main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()

def login():
	print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})

def token(data):
	print '[*] Generate access token '
	try:
		os.mkdir('cookie')
	except OSError:
		pass
	b = open('cookie/token.log','w')
	try:
		ok = requests.get('https://api.facebook.com/restserver.php',params=data)
		oj = json.loads(r.text)
		b.write(oj['access_token'])
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

def unfriend():
	global oj , token
	os.system('clear')
	try:
		token = open('cookie/token.log','r').read()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		login()

	ko = requests.get('https://graph.facebook.com/me?access_token='+token)
	oj = json.loads(r.text)
	os.system('clear')
	print(logo)
	print('Menggunakan akun'+ko['name'] 'untuk menghapus daftar  '+ko['id'])
	print(80*'_'+'\n')

	ok = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
	oj = json.loads(r.text)
	for o in ok['data']:

		jo = requests.delete('https://graph.facebook.com/me/friends?uid='+o['id']+'&access_token='+token)
		oj = json.loads(r.text)

		try:
			jok = jo['error']['message']
			print('[×] Failed')
		except KeyError:
			pass
		try:
			jml.append(o['id'])
			print '\r[*] Menghapus %s dari daftar teman.'% (len(jml)),;sys.stdout.flush();time.sleep(0.0001)

		except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()


if __name__ == '__main__':

	main()
