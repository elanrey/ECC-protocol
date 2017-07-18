import ctypes
num = 32

ecc = ctypes.cdll.LoadLibrary('./functions.so')
ecc.getRandom()
ecc.getHash()
ecc.makeKeys()
ecc.getRandom()
ecc.sign()
ecc.verify()
ecc.encrypt()
ecc.decrypt()
ere = (ctypes.c_uint8 * num).in_dll(ecc,'ere')
print('r:', end=' ')
for x in ere:
	print(x, end=' ')
print()
ese = (ctypes.c_uint8 * num).in_dll(ecc,'ese')
print('s:', end=' ')
for x in ese:
	print(x, end=' ')
print()
publicKx = (ctypes.c_uint8 * num).in_dll(ecc,'publicKx')
print('public key x:', end=' ')
for x in publicKx:
	print(x, end=' ')
print()
publicKy = (ctypes.c_uint8 * num).in_dll(ecc,'publicKy')
print('public key y:', end=' ')
for x in publicKy:
	print(x, end=' ')
print()
privateK = (ctypes.c_uint8 * num).in_dll(ecc,'privateK')
print('private key:', end=' ')
for x in privateK:
	print(x, end=' ')
print()
randomNum = (ctypes.c_uint8 * num).in_dll(ecc,'randomN')
print('random:', end=' ')
for x in randomNum:
	print(x, end=' ')
print()
hashNum = (ctypes.c_uint8 * num).in_dll(ecc,'hashN')
print('hash:', end=' ')
for x in hashNum:
	print(x, end=' ')
print()