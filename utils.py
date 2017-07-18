import serial
import time
import ctypes

ecc = ctypes.cdll.LoadLibrary('./functions.so')

s = serial.Serial(
	port = '/dev/ttyUSB0',
	baudrate = 9600,
	bytesize = serial.EIGHTBITS,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	timeout = 1,
	rtscts = 1
)

def printData(nom, dat):
	print(nom, end=' ')
	for x in dat:
		print(x, end=' ')
	print()

def sendData(data):
	resp = b''
	while resp == b'':
		s.flushOutput()
		s.write(data)
		time.sleep(0.1)
		s.flushInput()
		resp = s.read(2)

def getData(num):
	resp = b''
	while resp == b'':
		s.flushInput()
		resp = s.read(num)
		time.sleep(0.1)
		s.flushOutput()
		s.write(b'ok')
	return resp

def getVar(num, name):
	return (ctypes.c_uint8 * num).in_dll(ecc, name)