#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import serial
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--tty", dest="tty", help="Gibt die zu verwendende tty an [/dev/ttyUSB0]", default ="/dev/ttyUSB0")
parser.add_option("-b", "--baud", dest="baud", help="Baudrate [9600]", default="9600")
parser.add_option("-o", "--out", dest="out", help="Ausgabedatei")
#parser.add_option("-a", "--auto", dest="auto", help="Bild automatisch anzeigen", action="store_true")
(options, args) = parser.parse_args()

if options.out == None :
        print ('We need an output file !')
        sys.exit(1)

print ('Listening at '+str(options.tty)+' for data for 4 seconds\n')
print ('start print command immediately\n')
#with open('/tmp/9k6Bd_out.pyprint', 'w') as File:
with open(str(options.out), 'w') as File:
	with serial.Serial(options.tty, int(options.baud), bytesize=8, parity='N', stopbits=1, timeout=4, xonxoff=False, rtscts=False, dsrdtr=False) as ser:
		while True:
			line = ser.readline()
			if len(line) != 0 :
				File.write(line)
			else:
				print ('4 sec without data - will end now !')
				break
