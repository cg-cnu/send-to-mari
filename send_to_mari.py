#!/usr/bin/python

from telnetlib import Telnet
import sys

try:
	connection = Telnet('localhost', 6100)
	images = sys.argv[1:]

	for image in images:
		message = "mari.images.load('" + image + "')"
		connection.write(message)
		connection.write("\x04")
except:	
	import Tkinter
	import tkMessageBox
	
	window = Tkinter.Tk()
	window.wm_withdraw()
	tkMessageBox.showerror(title = 'Mari Error',
				message = 'Enable command port in mari')