#!/usr/bin/env python

"""
Insert custom messages into HP printer displays

Works for most network-enabled HP printers.
"""

import socket
import sys
import os.path

# Default configuration
host = '10.1.54.6'
port = 9100 #9100 is the default port.

sock = socket.socket()
try:
    sock.connect((host, port))
except socket.error, e:
    sys.exit('Connection error %s: %s.' % (e[0], e[1]))

print 'Connected'

message ="I wanted to be a fruit machine, but insted i print :-( "
print 'Setting ready message to "%s" on %s' % (message, host)
command = "\x1B%%-12345X@PJL RDYMSG DISPLAY = \"%s\"\r\n\x1B%%-12345X\r\n" % message
sock.sendall(command)

