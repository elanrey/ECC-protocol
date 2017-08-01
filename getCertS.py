from utils import *

#Configura puerto serial
configSerial('/dev/cu.usbserial-4')

mainPubKx = rxData(32)
printData('mainPubKx:', mainPubKx)
mainPubKy = rxData(32)
printData('mainPubKy:', mainPubKy)

#Genera numeros aleatorios
ecc.getRandom()
random = getVar(32, 'randomNum')
printData('random: ', random)

#Genera llaves pública y privada
ecc.makeKeys(random)

privateK = getVar(32, 'privateK')
printData('privK:', privateK)

publicKx = getVar(32, 'publicKx')
printData('pubKx:', publicKx)
txData(publicKx)

publicKy = getVar(32, 'publicKy')
printData('pubKy:', publicKy)
txData(publicKy)

array = []
array.extend(publicKx)
array.extend(publicKy)
keyHash = arrayToBytes(array)
ecc.getHash(keyHash, 64)
keyHash = getVar(32, 'hashNum')
printData('hash:', keyHash)

ere = rxData(32)
printData('ere:', ere)
ese = rxData(32)
printData('ese:', ese)

file = open('CertServer','wb')
file.write(mainPubKx)
file.write(mainPubKy)
file.write(privateK)
file.write(publicKx)
file.write(publicKy)
file.write(keyHash)
file.write(ere)
file.write(ese)
file.close()