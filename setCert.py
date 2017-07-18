from utils import *
import uuid

#Numeros aleatorios
ecc.getRandom()
randomNum = getVar(32, 'randomN')
printData('random: ', randomNum)

#Llaves R
ecc.makeKeys()

publicKx = getVar(32, 'publicKx')
printData('Rx: ', publicKx)

publicKy = getVar(32, 'publicKy')
printData('Ry: ', publicKy)

#Get Id
id = getData(16)
printData('id: ', id)

rand = getData(32)
printData('rand: ', rand)

#Get Qx
pubKx = getData(32)
printData('Qx: ', pubKx)

#Get Qy
pubKy = getData(32)
printData('Qy: ', pubKy)

#Id+Qx
con = id+pubKx 
ecc.setData(con, 48)
data = getVar(32, 'data')
printData('id+Qx: ', data)

#Hash ID+Qx
ecc.getHash(48)
hash = getVar(32, 'hashN')
printData('hash(id+Qx): ', hash)

ecc.sign()

ere = getVar(32, 'ere')
printData('r: ', ere)
sendData(ere)

ese = getVar(32, 'ese')
printData('s: ', ese)
sendData(ese)

s.close()