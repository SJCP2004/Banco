import os
from datetime import datetime
from io import open

def feho():
	nowx = datetime.now()
	mome = nowx.strftime("%d/%m/%Y %H:%M:%S")
	return mome

def limpiar():
	os.system('cls')

def imp(texto, forma='p', tab=8):
	mens = "\t"*tab + texto
	if forma == 'p':
		print(mens)
	else:
		return mens

def salto(salt=2):
	print("\n"*salt)

#===========================================================
#						MENU
#===========================================================
def menu():
	limpiar()
	salto()
	imp("Bienvenido al menu")
	salto(1)
	imp("1 Consulta")
	imp("2 Retiro")
	imp("3 Deposito")
	imp("4 Transferencias") 
	imp("5 Salir\n")
	salto(1)
	opc1=int(input(imp("Elija una opcion: ", 'i')))
	return opc1

#===========================================================
#						SALDO
#===========================================================
def saldo(sala, salc, tran):
	limpiar()
	salto()
	saldo=open("Saldo.dat", "r")
	sald=saldo.readlines()
	saldo.close()
	sala=float(sald[0])
	salc=float(sald[1])

	arch=open("Trans.dat", "r")
	trans=arch.readlines()
	for i in range(0, len(trans)):
		x=trans[i].replace('\n','').split("|")
		tran.append(x)
	arch.close()
	return [sala, salc]

#===========================================================
#						CONSULTA
#===========================================================
def consulta(sala, salc, tran):
	limpiar()
	salto()
	imp("Consulta")
	salto(1)
	imp("¿Que desea consultar?")
	imp("0 Saldo")
	imp("1 Transacciones")
	salto(1)
	opc2=int(input(imp("Inserte la opcion deseada: ", 'i')))
	if opc2 == 0:
		imp("Su saldo en la cuenta de ahorro es de: " + str(sala))
		tran.append([feho(), " consulta ", str(sala), " ahorro ", str(sala) ,"SI"])
		imp("Su saldo en la cuenta corriente es de: " + str(salc))
		tran.append([feho(), " consulta ", str(salc), " corriente ", str(salc), "SI"])
	else:
		salto()
		imp("Acontinuacion se mostraran sus transacciones")
		salto(1)
		imp("{0:<20} {1:<15} {2:>8} {3:^15} {4:>8} {5:^7}".format("Fecha", "Operacion", "Monto", "Tipo", "Saldo", "Estatus"), tab=6)
		for i in range(0, len(tran)):
			fech=tran[i][0]
			oper=tran[i][1]
			mont=tran[i][2]
			tipo=tran[i][3]
			sald=tran[i][4]
			esta=tran[i][5]
			imp("{0:<20} {1:<15} {2:>8} {3:^15} {4:>8} {5:^7}".format(fech, oper, mont, tipo, sald, esta), tab=6)
	input()
#===========================================================
#						RETIRO
#===========================================================
def retiro(sala, salc, tran):
	limpiar()
	salto()
	imp("Retiro")
	salto(1)
	imp("0 ahorro")
	imp("1 corriente")
	salto(1)
	opc3=int(input(imp("De que cuenta desea retirar el dinero: ", 'i')))
	if opc3 == 0:
		imp("Su saldo en la cuenta de ahorro es: " + str(sala))
		cant1 = float(input(imp("Cual es el monto que desea retirar: ", 'i')))
		if cant1 <= sala:
			sala -= cant1
			imp("Retiro exitoso")
			tran.append([feho(), " Retiro ", str(cant1), " ahorro ", str(sala), "SI"])
		else:
			imp("Saldo insuficiente")
			tran.append([feho(), " Retiro ", str(cant1), " ahorro ", str(sala), "NO"])

	else:
		imp("Su saldo en la cuenta corriente es: " + str(salc))
		cant2 = float(input(imp("Cual es el monto que desea retirar: ", 'i')))
		if cant2 <= salc:
			salc -= cant2
			imp("Retiro exitoso")
			tran.append([feho(), " Retiro ", str(cant2), " corriente ", str(salc), "SI"])
		else:
			imp("Saldo insuficiente")
			tran.append([feho(), " Retiro ", str(cant2), " corriente ", str(salc), "NO"])
	input()
	return [sala, salc]

#===========================================================
#						DEPOSITO
#===========================================================
def deposito(sala, salc, tran):
	limpiar()
	salto()
	imp("Deposito")
	salto(1)
	imp("0 ahorro")	
	imp("1 corriente")
	salto(1)
	opc4 = int(input(imp("De que cuenta quiere hacer el deposito: ", 'i')))
	if opc4 == 0:
		imp("Su saldo en la cuenta de ahorro es: " + str(sala))
		cant3 = float(input(imp("Cual es el monto que desea depositar: ", 'i')))
		if cant3 != 0:
			sala += cant3
			imp("Deposito exitoso")
			tran.append([feho(), " deposito ", str(cant3), " ahorro ", str(sala), "SI"])
		else:
			imp("Deposito fallido")
			tran.append([feho(), " deposito ", str(cant3), " ahorro ", str(sala), "NO"])

	else:
		imp("Su saldo en la cuenta corriente es: " + str(sala))
		cant4 = float(input(imp("Cual es el monto que desea depositar: ", 'i')))
		if cant4 != 0:
			salc += cant4
			imp("Deposito exitoso")
			tran.append([feho(), " deposito ", str(cant4), " corriente ", str(salc), "SI"])
		else:
			imp("Deposito fallido")
			tran.append([feho(), " deposito ", str(cant4), " corriente ", str(salc), "NO"])
	input()
	return [sala, salc]

#===========================================================
#					TRANSFERENCIA
#===========================================================
def tranferencia(sala, salc, tran):
	limpiar()
	salto()
	imp("transferencia")
	salto(1)
	imp("0 ahorro")
	imp("1 corriente")
	salto(1)
	opc4 = int(input(imp("De que cuenta quiere hacer la transferencia: ", '1')))
	if opc4 == 0:
		imp("Su saldo en la cuenta de ahorro es: " + str(sala))
		cant3 = float(input(imp("Cual es el monto que desea transferir: ", 'i')))
		if cant3 <= sala:
			salc += cant3
			sala -= cant3
			imp("Transferencia exitosa")
			tran.append([feho(), " Transferencia ", str(cant3), " ahorro ", str(salc), "SI"])
		else:
			imp("Saldo insuficiente")
			tran.append([feho(), " Transferencia ", str(cant3), " ahorro ", str(sala), "NO"])

	else:
		imp("Su saldo en la cuenta corriente es: " + str(salc))
		cant4 = float(input(imp("Cual es el monto que desea transferir: ", 'i')))
		if cant4 <= salc:
			sala += cant4
			salc -= cant4
			imp("Transferencia exitosa")
			tran.append([feho(), " Transferencia ", str(cant4), " corriente ", str(salc), "SI"])
		else:
			imp("Saldo insuficiente")
			tran.append([feho(), " Transferencia ", str(cant4), " corriente ", str(salc), "NO"])
	input()
	return [sala, salc]

#===========================================================
#						SALIR
#===========================================================
def salir():
	limpiar()
	salto()
	imp("Gracias por usar nuestro servicio")
	saldo=open("Saldo.dat","w")
	saldo.write(str(sala) + "\n")
	saldo.write(str(salc) + "\n")
	saldo.close()

	arc2=open("Trans.dat", "a")
	tran2=arc2.readlines()
	for i in range(0, len(tran)):
		"|".join(tran)
	arc2.close()

#===========================================================
#					PROGRAMA PRINCIPAL
#===========================================================
salc=0
sala=0
cons=0
tran=[]
sala, salc = saldo(sala, salc, tran)
opc1=1
while opc1 <= 4:
	opc1 = menu()
	if opc1 == 1:
		consulta(sala, salc, tran)
	elif opc1 == 2:
		sala, salc = retiro(sala, salc, tran)
	elif opc1 == 3:  
 		sala, salc = deposito(sala, salc, tran)
	elif opc1 == 4:  
 		sala, salc = tranferencia(sala, salc, tran)
	else:
		salir()
		break