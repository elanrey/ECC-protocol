from utils import *

#Configura puerto serial
configSerial('/dev/cu.usbserial-A50285BI')
file = open('CertServer','rb')

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
mainPubKx = arrayToBytes(array)
printData('mainPubKx:', mainPubKx)

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
mainPubKy = arrayToBytes(array)
printData('mainPubKy:', mainPubKy)

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
privateK = arrayToBytes(array)
printData('privateK:', privateK)

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
publicKx = arrayToBytes(array)
printData('pubKx:', publicKx)

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
publicKy = arrayToBytes(array)
printData('pubKy:', publicKy)

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
ere = arrayToBytes(array)
printData('ere:', ere)

array = []
byte = file.read(32)
for x in byte:
    array.append(x)
ese = arrayToBytes(array)
printData('ese:', ese)

array = []
encDataS = rxData(32)
ecc.setData(encDataS, 0, 16)
ecc.decryptData(mainPubKx)
array.extend(getVar(16, 'data'))
ecc.setData(encDataS, 16, 32)
ecc.decryptData(mainPubKx)
array.extend(getVar(16, 'data'))
UpubKx = arrayToBytes(array)
printData('UpubKx:', UpubKx)

array = []
encDataS = rxData(32)
ecc.setData(encDataS, 0, 16)
ecc.decryptData(mainPubKx)
array.extend(getVar(16, 'data'))
ecc.setData(encDataS, 16, 32)
ecc.decryptData(mainPubKx)
array.extend(getVar(16, 'data'))
UpubKy = arrayToBytes(array)
printData('UpubKy:', UpubKy)

array = []
encDataS = rxData(32)
ecc.setData(encDataS, 0, 16)
ecc.decryptData(mainPubKx)
array.extend(getVar(16, 'data'))
ecc.setData(encDataS, 16, 32)
ecc.decryptData(mainPubKx)
array.extend(getVar(16, 'data'))
Uere = arrayToBytes(array)
printData('Uere:', Uere)

array = []
encDataS = rxData(32)
ecc.setData(encDataS, 0, 16)
ecc.decryptData(mainPubKx)
array.extend(getVar(16, 'data'))
ecc.setData(encDataS, 16, 32)
ecc.decryptData(mainPubKx)
array.extend(getVar(16, 'data'))
Uese = arrayToBytes(array)
printData('Uese:', Uese)

#Cifra publicKx
array = []
ecc.setData(publicKx, 0, 16)
ecc.encryptData(mainPubKx)
array.extend(getVar(16, 'data'))
ecc.setData(publicKx, 16, 32)
ecc.encryptData(mainPubKx)
array.extend(getVar(16, 'data'))
encData = arrayToBytes(array)
txData(encData)

#Cifra publicKy
array = []
ecc.setData(publicKy, 0, 16)
ecc.encryptData(mainPubKx)
array.extend(getVar(16, 'data'))
ecc.setData(publicKy, 16, 32)
ecc.encryptData(mainPubKx)
array.extend(getVar(16, 'data'))
encData = arrayToBytes(array)
txData(encData)

#Cifra ere
array = []
ecc.setData(ere, 0, 16)
ecc.encryptData(mainPubKx)
array.extend(getVar(16, 'data'))
ecc.setData(ere, 16, 32)
ecc.encryptData(mainPubKx)
array.extend(getVar(16, 'data'))
encData = arrayToBytes(array)
txData(encData)

#Cifra ese
array = []
ecc.setData(ese, 0, 16)
ecc.encryptData(mainPubKx)
array.extend(getVar(16, 'data'))
ecc.setData(ese, 16, 32)
ecc.encryptData(mainPubKx)
array.extend(getVar(16, 'data'))
encData = arrayToBytes(array)
txData(encData)

#Genera hash de la llave pública externa
array = []
array.extend(UpubKx)
array.extend(UpubKy)
keyHash = arrayToBytes(array)
ecc.getHash(keyHash, 64)
keyHash = getVar(32, 'hashNum')
printData('hash:', keyHash)

if ecc.verify(mainPubKx, mainPubKy, keyHash, Uere, Uese):
    ecc.getSharedKey(UpubKx, UpubKy, privateK)
    sharedKey = getVar(32, 'sharedK')
    printData('Shared Key:', sharedKey)