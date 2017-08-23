
#!/usr/bin/python

from threading import Thread, Timer, Event
from ExpanderPi import ADC
import MySQLdb

class ADCInput():
	def __init__(self, name, time, hfunction):
		self.name = name
		self.t = time
		self.hfunction = hfunction
		self.thread = Timer(self.t, self.handle_function)

	def handle_function(self):
		self.hfunction(self)
		self.thread = Timer(self.t, self.handle_function)
		self.thread.start()

	def start(self):
		try:
			self.thread.start()
		except:
			print("Unable to start thread - " + name)
		else:
			print(self.name + " - Thread started.")


	def cancel(self):
		self.thread.cancel()

def scan(self):
	print(self.name + " - ACTIVATED")

def Greeting():
	print("EDC SMU - " + g_version)

def Setup():
	for x in range(0, MAXINPUT):	# 0 to 3
		name = "Input" + str(x)
		Y = ADCInput(name, g_timerinterval, scan)
		g_InputList.append(Y)
		Y.start()


# Start of main loop
g_version = "0.1a";
MAXINPUT = 4
g_mainloop = 1
g_timerinterval = 5
g_InputList = []

Greeting()

try:
	connection = MySQLdb.connect(host="localhost", user="root", passwd="EnEr5y1997", db="SMU")
except:
	print("FATAL - Unable to make database connection.")
else:
	Setup()
	g_exitflag = 1
	while g_exitflag:
		g_exitflag = True
	connection.commit()
	connection.close()
