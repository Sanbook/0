import json , sys , hashlib , os , time , marshal, getpass
import requests
def id():
	print '[*] login to your facebook account         ';
	id = raw_input('[?] Username : ');
	pwd = getpass.getpass('[?] Password : ');
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';
	params = {"url":"https://graph.facebook.com/oauth/access_token%0A%20%20%20","raw_url":"https://graph.facebook.com/oauth/access_token\n   ?client_id={6628568379}\n   &client_secret={c1e620fa708a1d5696fb991c1bde5662}\n   &grant_type=client_credentials\n   &method=auth.login\n   &credentials_type=email='+id+'\n   &password=pwd\n   &format=JSON\n   &generate_machine_id=1\n   &generate_session_cookies=1\n   &locale=en_US\n   &return_ssl_resources=0\n   &v=1.0+c1e620fa708a1d5696fb991c1bde5662","method":"get","queries":{"client_id":"{6628568379}\n   ","client_secret":"{c1e620fa708a1d5696fb991c1bde5662}\n   ","grant_type":"client_credentials\n   ","method":"auth.login\n   ","credentials_type":"email=' id '\n   ","password":"pwd\n   ","format":"JSON\n   ","generate_machine_id":"1\n   ","generate_session_cookies":"1\n   ","locale":"en_US\n   ","return_ssl_resources":"0\n   ","v":"1.0 c1e620fa708a1d5696fb991c1bde5662"}}
	sig = (
    ('client_id', '{6628568379}\n   '),
    ('client_secret', '{c1e620fa708a1d5696fb991c1bde5662}\n   '),
    ('grant_type', 'client_credentials\n   '),
    ('method', 'auth.login\n   '),
    ('credentials_type', 'email=\' id \'\n   '),
    ('password', 'pwd\n   '),
    ('format', 'JSON\n   '),
    ('generate_machine_id', '1\n   '),
    ('generate_session_cookies', '1\n   '),
    ('locale', 'en_US\n   '),
    ('return_ssl_resources', '0\n   '),
    ('v'),
             )	
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
def get(data):
	print '[*] membuat kode masuk... '

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
		print '[*] successfully membuat kode masuk...'
		print '[*] Your access token is stored in cookie/token.log'
		halaman_utaman()
	except KeyError:
		print '[!] Failed to membuat kode masuk...'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to membuat kode masuk...'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		id()

def getdata():
	global a , token

	print '[*] Load Access Token'

	try:
		token = open("cookie/token.log","r").read()
		print '[*] Success load access token '
	except IOError:
		print '[!] failed to open cookie/token.log'
		print "[!] type 'token' to membuat kode masuk..."
		main()

	print '[*] fetching all friends data'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print '[!] Your access token is expired'
		print "[!] type 'token' to membuat kode masuk..."
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
