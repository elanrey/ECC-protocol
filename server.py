from utils import *

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

