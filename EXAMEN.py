#Cree una aplicacion de cajero automatico para el banco FDP INVERSMENTS. El Cajero tendra un limite de billes descritos a continuacion:

#18 billetes de 1,000
#19 billetes de 500
#23 billetes de 200
#50 billetes de 100

#El cajero debe solicitar banco y monto a retirar. Si el banco es FDP INVERSMENTES el limite es 20,000 y 10,000 pesos por transaccion en caso contrario.

#El cajero debe informar si el monto solicitado no puedo ser dispensaco o si excede el limite de transaccion. Y debe hacer la distribucion de los billetes de acuerdo al monto.

#ejemplo si el usario solicita 10,900 y hay disponibilidad en todas los billetes, el cajero debe dispensar 10 billetes de mil, 1 de quinienteos y 2 dociento.



def volver ():
  input('Precione [Enter] para volver.')
  banco_INVERSMENTES()
def banco_INVERSMENTES ():
  print('-------------------------')
  print('--Banco FDP INVERSMENTS--')
  print('-------------------------')
  print('1: Banco FDP INVERSMENTES')
  print('2: Otro banco')

  FDP  = int(input('Introduzca su banco:\n->'))

  if FDP == 1:
    cantidad = int(input('Dijite un monto:\n ->'))
    if cantidad > 20000:
      print('No puede retirar esta cantida.')
      volver()
    else: 
      if cantidad <= 20000:
        bi1000 = cantidad // 1000
        print('Hay' + str (bi1000) + 'billetes de 1,000')
        cantidad = cantidad % 1000

        bi500 = cantidad // 500
        print('Hay' + str (bi500) + 'billetes de 500')
        cantidad = cantidad % 500

        bi200 = cantidad // 200
        print('Hay'+str (bi200)+ 'Billetes de 200')
        cantidad=cantidad % 200

        bi100 = cantidad // 100
        print('Hay'+str (bi100)+ 'Billetes de 100')
        cantidad=cantidad % 100
        volver()

  elif FDP == 2:
    cantidad1 = int(input('Digite un monto:\n ->'))
    if cantidad1 > 10000:
      print('No puede retirar esta cantidad')
      volver()
    else:
      if cantidad1 <= 10000:
        bi1000 = cantidad // 1000
        print('Hay' + str (bi1000) + 'billetes de 1,000')
        cantidad = cantidad % 1000

        bi500 = cantidad // 500
        print('Hay' + str (bi500) + 'billetes de 500')
        cantidad = cantidad % 500

        bi200 = cantidad // 200
        print('Hay'+str (bi200)+ 'Billetes de 200')
        cantidad=cantidad % 200

        bi100 = cantidad // 100
        print('Hay'+str (bi100)+ 'Billetes de 00')
        cantidad=cantidad % 100
        volver()
  else:
      volver()

  

banco_INVERSMENTES()