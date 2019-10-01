import json , sys , hashlib , os , time , marshal, getpass
import requests

reload (sys)
sys . setdefaultencoding ( 'utf8' )

jml = []
jmlgetdata = []
n = []


#CSS
logo=(B+'''OK''')

csm=('''
      COMMAND                      DESCRIPTION
  -------------       -------------------------------------

   Login 	          fetching all friends data
   acces_token        show information about your friend

   cat_token          fetching all friends data
   delete_post        show information about your friend

''')



def main():
  global target_id
  print(logo)
  print(csm)
  try:
	cek = raw_input('MENU  ')
	if cek.lower() == 'acces_token':
		if len(jml) == 0:
			getdata()
		else:
			print '[*] You have retrieved %s friends data'%(len(jml))
			main()
	elif cek.lower() == 'Login':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				main()
		except IOError:
			pass
		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		login()
	elif cek.lower() == "cat_token":
		try:
			o = open('cookie/token.log','r').read()
			print '[*] Your access token !!\n\n' + o + '\n'
			main()
		except IOError:
			print '[!] failed to open cookie/token.log'
			print "[!] type 'token' to generate access token"
			main()
	elif cek.lower() == 'delete_post':
		print '\n'+'[*] Information Gathering [*]'.center(44) + '\n'
		hapusStatus()
	elif cek.lower() == 'clear':
		if sys.platform == 'win32':
			os.system('cls')
			logo()
			main()
		else:
			os.system('clear')
			logo()
			main()

def login():
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
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		login()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		login()
		
	print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)

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
		jml.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(jml)),;sys.stdout.flush();time.sleep(0.0001)

	print '\r[*] '+str(len(jml))+' data of friends successfully retrieved'
	main()

def hapusStatus():
	import requests
	print 'Mengambil token...'
	try:
		token = open("cookie/token.log",'r').read()
		print 'Token berhasil diambil...'
	except IOError:
		print '[!] Token hilang mendadak...'
		print "[*] Ketik login untuk masuk kembali..."
		main()
	status = (
    ('fields', 'feed.limit(49)'),
    ('access_token', ''), )
	mengambil = requests.get('https://graph.facebook.com/me', status=params)
#curl -i -X GET \
#"https://graph.facebook.com/me?fields=feed.limit(49)&access_token="
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://graph.facebook.com/me?fields=feed.limit(49)&access_token=')
	data = (
    ('access_token', 'token'),)
	response = requests.delete('https://graph.facebook.com/{}', data=params).format(status['id'])
#curl -i -X DELETE \
#"https://graph.facebook.com/{post}?access_token={token}"
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.delete('https://graph.facebook.com/{post}?access_token={token}')
		try:
			ror=data['error']['message']
			print('[×] Gagal')
		except IOError:
			print(data['id'])
		except requests.exceptions.ConnectionError:
			print('Tidak ada koneksi...')
	print('Program Berhenti')

if __name__ == '__main__':

	logo()
	main()
