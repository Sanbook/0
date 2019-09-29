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
