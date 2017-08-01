from utils import *

#Genera numeros aleatorios
ecc.getRandom()
random = getVar(32, 'randomNum')

#Genera llaves R,k
ecc.makeKeys(random)

privateK = getVar(32, 'privateK')
printData('privK:', privateK)
publicKx = getVar(32, 'publicKx')
printData('pubKx:', publicKx)
publicKy = getVar(32, 'publicKy')
printData('pubKy:', publicKy)

#Guarda llaves R,k
file = open('Keys','wb')
file.write(privateK)
file.write(publicKx)
file.write(publicKy)
file.close()