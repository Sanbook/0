#Python 3.7.X
#Author				: Soesanto
#Program Name		: Nguyen
#Program Language	: Python
#Manage Program Using Sanbook With SAN-Brother Team




import json , sys , hashlib , os , time , marshal
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
	eror
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

def cssLoginWarning():
	
	print '''
%s------------
⚠WARNING!!
------------%s
 			Masukan user name facebook kamu, bisa ID,
 			bisa Email, bisa Nomor Telpon diterminal!
 			Untuk kata sandi  seusai  ENTER  Username
 			harap hati-hati, karena TEXT tidak tampil.%s

* mohon hubungi kami jika terjadi eror atau program
  tidak bekerja dengan sempurna!
'''%(R,W,G)

def UserValidation():
	
	print '''
	%s-----------------------
	Tulis Username disini :
'''%(R)

def UserValidati0n()
	print '''
	%sTulis Password disini :
	-----------------------
'''%(R)
def cssEror()
	print '''
eror
                         
'''%(R)                                    
         
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
def id():
	print (cssLoginWarning);id = raw_input(UserValidation);pwd = getpass.getpass(UserValidati0n);API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
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
		menghitung.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(menghitung)),;sys.stdout.flush();time.sleep(0.0001)

	print '\r[*] '+str(len(menghitung))+' data of friends successfully retrieved'
	main()

def search():

	if len(menghitung) == 0:
                print "[!] no friend data in the database"
                print '[!] type "get_data" to collect friends data'
                main()
        else:
                pass

	getElement = raw_input("[!] Search Name or Id : ")

	if getElement == '':
		print "[!] name or id can't be empty !!"
		search()
	else:
		profileInformationMenu(getElement)



def cssMain():
	print '''
	%so %so %so %s═══════════════╗    ╔════════╗   ╔════╗ 
    ╔═╗ ╔═╗ ╔═╗╔═╗%sPROGRAM║╔╗  ║ %sNGUYEN%s ║   ║%sV.01%s║   ╔══╗
    ╚═╗ ╠═╣ ║ ║╠═╩╗╔═╗╔═╗╠╣   ╚════════╝   ╚════╝   ╚══╝
    ╚═╝%sSOESANTO%s╚══╝╚═╝╚═╝╝╚╝ 

    %s╔═%sSanBook%s══════════════════════════════════════════╗
    ║  ╔════════╗        ╔════════╗        ╔════════╗  ║
    ║  ║  %sMasuk%s ║        ║ %sKeluar%s ║        ║ %sUpdate%s ║  ║
    ║  ╚════════╝        ╚════════╝        ╚════════╝  ║
    ╚══════════════════════════════════════════════════╝

'''%(R,W,G,)  

def main():
  global target_id

  try:
	cek = raw_input(R + 'D3b2y' + W +' >> ')

	if cek.lower() == 'get_data':
		if len(menghitung) == 0:
			getdata()
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
def cssMenu():
	print '''
o o o ═══════════════╗    ╔════════╗   ╔════╗ 
╔═╗ ╔═╗ ╔═╗╔═╗PROGRAM║╔╗  ║RECYCLE ║   ║    ║   ╔══╗   ╔═╗
╚═╗ ╠═╣ ║ ║╠═╩╗╔═╗╔═╗╠╣   ╚════════╝   ╚════╝   ╚══╝   ╚═╝
╚═╝SOESANTO╚══╝╚═╝╚═╝╝╚╝ [⚠] Tolong matikan VPNnya yah!!!

    %s╔═%sSanBook%s══════════════════════════════════════════╗
    ║  ╔════════╗        ╔════════╗        ╔════════╗  ║
    ║  ║ Profil ║        ║Toolkit ║        ║Recycle ║  ║
    ║  ╚════════╝        ╚════════╝        ╚════════╝  ║
    ╚══════════════════════════════════════════════════╝

'''%(R,W,G,)  
def menu():

  	global getElement_id

  	try:
	cek = raw_input(R + 'D3b2y' + W +' >> ')

	if cek.lower() == 'Profil':
		if len(menghitung) == 0:
			menuProfile()
		else:
			print '[*] You have retrieved %s friends data'%(len(menghitung))
			main()

		elif cek.lower() == 'Toolkit':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		menuToolkit()


		elif cek.lower() == 'Recycle':
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
			menuRecycle()












def cssMenuProfile():
	print '''
[1.] Profil Guard
[2.] Profil Information

'''%(R,W,G,)  
def menuProfile():
  	global getElement_id

  	try:
	cek = raw_input(R + 'D3b2y' + W +' >> ')

	if cek.lower() == 'get_data':
		if len(menghitung) == 0:
			getdata()
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
				bot()
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
def profileGuardActivation(getElement):
def profileInformationMenu(getElement):
        global a , token

        print '[*] Searching'
	for i in a['data']:

	  if getElement in  i['name'] or getElement in i['id']:

		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		y = json.loads(x.text)

		print ' '
		print G + '[-------- INFORMATION --------]'.center(44)
		print W

		try:
			print '\n[*] Id : '+i['id']
		except KeyError:
			pass
		try:
			print '[*] Username : '+y['username']
		except KeyError:
			pass
		try:
			print '[*] Email : '+y['email']
		except KeyError:
			pass
		try:
			print '[*] Mobile Phone : '+y['mobile_phone']
		except KeyError:
			pass
		try:
			print '[*] Name : '+y['name']
		except KeyError:
			pass
		try:
			print '[*] First name : '+y['first_name']
		except KeyError:
			pass
		try:
			print '[*] Midle name : '+y['middle_name']
		except KeyError:
			pass
		try:
			print '[*] Last name : '+y['last_name']
		except KeyError:
			pass
		try:
			print '[*] Locale : '+y['locale'].split('_')[0]
		except KeyError:
			pass
		try:
			print '[*] location : '+y['location']['name']
		except KeyError:
			pass
		try:
			print '[*] hometown : '+y['hometown']['name']
		except KeyError:
			pass
		try:
			print '[*] gender : '+y['gender']
		except KeyError:
			pass
		try:
			print '[*] religion : '+y['religion']
		except KeyError:
			pass
		try:
			print '[*] relationship status : '+y['relationship_status']
		except KeyError:
			pass
		try:
			print '[*] political : '+y['political']
		except KeyError:
			pass
		try:
			print '[*] Work :'

			for i in y['work']:
				try:
					print '   [-] position : '+i['position']['name']
				except KeyError:
					pass
				try:
					print '   [-] employer : '+i['employer']['name']
				except KeyError:
					pass
				try:
					if i['start_date'] == "0000-00":
						print '   [-] start date : ---'
					else:
						print '   [-] start date : '+i['start_date']
				except KeyError:
					pass
				try:
					if i['end_date'] == "0000-00":
						print '   [-] end date : ---'
					else:
						print '   [-] end date : '+i['end_date']
				except KeyError:
					pass
				try:
					print '   [-] location : '+i['location']['name']
				except KeyError:
					pass
				print ' '
		except KeyError:
			pass
		try:
			print '[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]
		except KeyError:
			pass
		try:
			print '[*] Languages : '
			for i in y['languages']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] Bio : '+y['bio']
		except KeyError:
			pass
		try:
			print '[*] quotes : '+y['quotes']
		except KeyError:
			pass
		try:
			print '[*] birthday : '+y['birthday'].replace('/','-')
		except KeyError:
			pass
		try:
			print '[*] link : '+y['link']
		except KeyError:
			pass
		try:
			print '[*] Favourite teams : '
			for i in y['favorite_teams']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] School : '
			for i in y['education']:
				try:
					print ' ~  '+i['school']['name']
				except KeyError:
					pass
		except KeyError:
			pass
	  else:
		pass

        else:
		print W + ' '
		print '[*] Done '
		main()













def cssMenuToolkit():
	print '''
	[1.] Dump Email Member Group
	[2.] Auto Report  Fake Account
	[3.] Brute Force  Group  Member
	[4.] Auto  Brute  Force  Friends
	[5.] Group  Comment  Auto  Spammer
	[6.] Claim   Group    Administration
'''%(R,W,G,)
def menuToolkit():


def cssMenuRecycle():
	print '''
	[1] Delete All  Post
    [2] Delete All Messages 
    [3] Unfriend All Friends
    [4] Delete All Album Photo
    [5] Delete All Photo In Album
    [6] Declane All Friends Request
    '''%(R,R,R)
def menuRecycle():





def toolkitEmail():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
                print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all emails'
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_mails.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
                        z = json.loads(x.text)

			try:
                                out.write(z['email'] + '\n')
			        print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['email']
			except KeyError:
				pass
		out.close()

                print '[*] done'
                print "[*] all emails successfuly retrieved"
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_mails.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all emails"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def toolkitReport():

def toolkitBruteGM():

def toolkitBruteFriends():

def toolkitComment():

	global message , token

	print '\r[*] All posts id successfuly retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= amount:
				break
			else:
				counter += 1

			parameters = {'access_token' : token, 'message' : message}
			url = "https://graph.facebook.com/{0}/comments".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print W + '[' + G + id + W + '] ' +post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print W + '[' + G + id + W + '] successfully commented'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
                print '\r[!] Stopped'
		bot()

def toolkitClaim():





def recyclePost():

	global token , WT

	print '\r[*] All post id successfully retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/{id}?method=delete&access_token={token}'.format(id=post['id'],token=token))
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['id'] + W +'] Failed'
			except TypeError:
				print W + '[' + G + post['id'] + W + '] Removed'
				counter += 1
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()

def recycleMessages():

def recycleFriends():

def recycleAlbum():
	global token , WT

	print '\r[*] all id successfully retrieved                 '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/'+post['id']+'?method=delete&access_token='+token)
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['name'] + W + '] Failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] femoved'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped  '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] connection error'
		bot()

def recyclePhoto():

def recycleRequest():



if __name__ == '__main__':

	banner()
	main()
	menu()
