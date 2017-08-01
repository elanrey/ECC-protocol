from utils import *

#Configura puerto serial
configSerial('/dev/cu.usbserial-A50285BI')

#Obtener llaves pública y privada
file = open('keys','rb')

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
privateK = arrayToBytes(array)
printData('privK:', privateK)

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
publicKx = arrayToBytes(array)
txData(publicKx)
printData('pubKx:', publicKx)

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
publicKy = arrayToBytes(array)
txData(publicKy)
printData('pubKy:', publicKy)

#Genera numeros aleatorios
ecc.getRandom()
random = getVar(32, 'randomNum')
printData('random:', random)

#Recibe llave pública
pubKx = rxData(32)
printData('exPubKx:', pubKx)
pubKy = rxData(32)
printData('exPubKy:', pubKy)

#Genera hash de la llave pública externa
array = []
array.extend(pubKx)
array.extend(pubKy)
keyHash = arrayToBytes(array)
ecc.getHash(keyHash, 64)
keyHash = getVar(32, 'hashNum')
printData('hash:', keyHash)

#Firma de llave pública externa
ecc.sign(privateK, random, keyHash)

ere = getVar(32, 'ere')
printData('ere:', ere)
txData(ere)

ese = getVar(32, 'ese')
printData('ese:', ese)
txData(ese)