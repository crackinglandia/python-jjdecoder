import sys

from jjdecode import JJDecoder

if len(sys.argv) < 2:
	print "Usage: %s <jjencoded_file>" % __file__
	sys.exit(0)

kk = open(sys.argv[1],'rb').read()			
jotas = JJDecoder(kk)
outt = jotas.decode()
print outt
