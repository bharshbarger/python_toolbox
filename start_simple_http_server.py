import subprocess
import sys
import urllib2
from time import sleep

def serv():
	null = open('/dev/null', 'w')

	p = subprocess.Popen(
		[sys.executable, '-m', 'SimpleHTTPServer', '8124'], 
		cwd='/tmp',
		stdout=null,
		stderr=null,		
	)
	sleep(1)

	return p

def print_url():

	try:
		print bool(urllib2.urlopen('http://127.0.0.1:8124').read())
	except Exception as e:
		print e

print_url()
p = serv()
print_url()
p.terminate()
print_url()
p = serv()
print_url()
p.terminate()
print_url()
p = serv()
print_url()
