"""
portsc.py scans ports from a specfied lower bound to a specified upper bound, inclusive.
portsc.py takes 3 command line arguments:
	1. ip address
	2. lower bound for ports to be scanned
	3. upper bound for ports to be scanned
author: noah michaels
"""

import socket #gives sockets
import sys #gives command line args

def main():
	ip = sys.argv[1]
	start = int(sys.argv[2])
	end = int(sys.argv[3]) + 1	
	for port in range(start, end):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(1)
			s.connect((ip, port))
			print('port ' + str(port) + ' is open')
			s.close()

		except socket.timeout:
			#If the connection times out, the port is filtered
			print('port ' + str(port) + ' is filtered')

		except socket.error:
			#If the connection is refused, the port is closed
			print('port ' + str(port) + ' is closed')


main()
