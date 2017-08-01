import serial, time, ctypes, pathlib

ecc = ctypes.cdll.LoadLibrary('./functions.so')

s = serial.Serial()

def configSerial(path):
	s.port = path
	s.baudrate = 9600
	s.bytesize = serial.EIGHTBITS
	s.parity = serial.PARITY_NONE	
	s.stopbits = serial.STOPBITS_ONE
	s.timeout = 1
	s.rtscts = 1

def printData(nom, dat):
	print(nom, end=' ')
	for x in dat:
		print(x, end=' ')
	print()

def txData(data):
	resp = b''
	s.open()
	while resp == b'':
		s.flushOutput()
		s.write(data)
		time.sleep(0.1)
		s.flushInput()
		resp = s.read(2)
	s.close()

def rxData(num):
	resp = b''
	s.open()
	while resp == b'':
		s.flushInput()
		resp = s.read(num)
		time.sleep(0.1)
		s.flushOutput()
		s.write(b'ok')
	s.close()
	return resp

def getVar(num, name):
	return (ctypes.c_uint8 * num).in_dll(ecc, name)

def arrayToBytes(array):
	byte_arr = bytearray(array)
	return (ctypes.c_ubyte*len(byte_arr))(*(byte_arr))