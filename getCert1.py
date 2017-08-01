from utils import *
import uuid

#ID
id = uuid.uuid1()
printData('id: ', id.bytes)
sendData(id.bytes)

#Genera numeros aleatorios
ecc.getRandom()
randomNum = getVar(32, 'randomN')
printData('random: ', randomNum)
sendData(randomNum)

#Genera llaves Q
ecc.makeKeys()

publicKx = getVar(32, 'publicKx')
printData('public key x: ', publicKx)
sendData(publicKx)

publicKy = getVar(32, 'publicKy')
printData('public key y: ', publicKy)
sendData(publicKy)

#Genera r
ere = getData(32)
printData('r: ', ere)

#Genera s
ese = getData(32)
printData('s: ', ese)

s.close()

clave = id.bytes+randomNum+publicKx+publicKy+ere+ese
ecc.setData(clave, 176)
ecc.getHash(176)
hash = getVar(32, 'hashN')
printData('hash: ', hash)

file = open('testfile.txt','wb')
file.write(clave)
file.close()

file = open('testfile.txt','rb')
byte = file.read(1)
while byte != b'':
	print(int.from_bytes(byte, byteorder='big'),end=' ')
	byte = file.read(1)