Generación de Certificados

                             Usuario/Servidor       Tx/Rx       Autoridad certificadora
                 Generar números aleatorios d                   Generar números aleatorios c
                     Generar llaves Q = d X P                   Obtener llaves (R, k)
                       Enviar llave pública Q       >>>>>       Recibir llave pública Q
                        Generar hash e = H(Q)                   Generar hash e = H(Q)
                                                                Generar firma (r, s)
                      Recibir llave pública R       <<<<<       Enviar llave pública (R)
                         Recibir firma (r, s)       <<<<<       Enviar firma (r, s)
                 Guardar (d, Q, R, e, (r, s))
______________________________________________________________________________________________________________________________

Autenticación Mutua y Acuerdo de Llaves

                                      Usuario       Tx/Rx       Servidor
            Obtener (du, Qu, R, eu, (ru, su))                   Obtener (ds, Qs, R, es, (rs, ss))
        Cifrar datos Cu = E(Qu, eu, (ru, su))                   Cifrar datos Cs = E(Qs, es, (rs, ss))
                    Recibir datos cifrados Cs       <<<<<       Enviar datos cifrados Cs
                     Enviar datos cifrados Cu       >>>>>       Recibir datos cifrados Cu 
                     Descifrar datos D(R, Cs)                   Descifrar datos D(R, Cu)
               Verificar firma (es, (rs, ss))                   Verificar firma (eu, (ru, su))
    Si firma OK => continua, si no => termina                   Si firma OK => continua, si no => termina
           Generar llave mutua (Qk = du X Qs)                   Generar llave mutua (Qk = ds X Qu)
           
