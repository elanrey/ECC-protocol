from utils import *

file = open('CertUser','rb')

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
keyHash = arrayToBytes(array)
printData('keyHash:', keyHash)

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
#Cifra publicKx
ecc.setData(publicKx, 0, 16)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
ecc.setData(publicKx, 16, 32)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
#Cifra publicKx
ecc.setData(publicKy, 0, 16)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
ecc.setData(publicKy, 16, 32)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
#Cifra hash
ecc.setData(keyHash, 0, 16)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
ecc.setData(keyHash, 16, 32)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
#Cifra ere
ecc.setData(ere, 0, 16)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
ecc.setData(ere, 16, 32)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
#Cifra ere
ecc.setData(ese, 0, 16)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
ecc.setData(ese, 16, 32)
ecc.encryptData(privateK)
array.extend(getVar(16, 'data'))
encData = arrayToBytes(array)

printData('encryptedData:', encData)
