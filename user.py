from func import *

ecc.getRandom()
randomNum = getVar(32, 'randomN')
printData('random: ', randomNum)

ecc.makeKeys()
publicKx = getVar(32, 'publicKx')
printData('public key x: ', publicKx)
publicKy = getVar(32, 'publicKy')
printData('public key y: ', publicKy)

