from time import sleep

#app number call list

# add number call
def addPhone(val, lists):
	k = 0
	adTrue = False
	ref = {0: True, 1: False}
	while k < len(lists):

		if val == lists[k]:
			adTrue = ref[0]
		k += 1

	if adTrue == True:
		print("\n", val, "Ya se encuentra agregado.\n\n")
	else:
		print("agregando..")
		sleep(1)
		listPhone.append(val)
		print(val, "agregado")

# show contacts
def showPhone(listss):
	print("Mostrado..\n")
	sleep(1)
	for lists in listss:
		print(lists)
		texts = ""
	print("\n")

# remove number call
def removePhone(lists, val):
	ref = False
	for k in lists:
		if k == val:
			ref = True
	if ref == True:
		print("eliminando..")
		sleep(1)
		lists.remove(val)
		print(val, "Eliminado\n")
	else:
		print(val, "No encontrado.\n")

# verified existence number call
def verifiedList(lists):
	iterators = 0

	while iterators < len(lists):
		iterators += 1

	if lists != []:
		if iterators <= 1:
			print("\n\tListas de contactos:\n", iterators, "contacto\n")

		else:
			print("\n\tListas de contactos:\n", iterators, "contactos\n")

	else:
		print("La lista esta vacia")

# update number call
def updatePhone(lists, oldPhone, newPhone):
	n = 0
	valid = False
	ref = {0: True, 1: False}
	print("Verificando..")
	sleep(1)
	while n < len(lists):

		if lists[n] == oldPhone:
			lists[n] = newPhone
			valid = ref[1]

		n += 1

	if valid == ref[0]:
		print("Ese numero no existe")
	else:
		print("Actualizado correctamente")

listPhone = ["8297510847", "8092221284", "8295466271"]

configs = {
	0: "salir",
	1: 0,
	2: "mostrar",
	3: "eliminar",
	4: "agregar",
	5: "actualizar",
	6: "Agregar numero: "
}
resp = configs[3]

while resp != configs[0]:
	resp = input("MOSTRAR | ACTUALIZAR | ELIMINAR | AGREGAR: ")

	if resp == configs[2]:

		verifiedList(listPhone)
		showPhone(listPhone)

	elif resp == configs[4]:
		val = input(configs[6])
		addPhone(val, listPhone)

	elif resp == configs[3]:
		if listPhone != []:
			delete = input("Numero a eliminar: ")
			removePhone(listPhone, delete)
		else:
			verifiedList(listPhone)

	elif resp == configs[5]:

		if listPhone != []:
			oldP = input("Numero viejo: ")
			oldNew = input("Numero nuevo: ")

			updatePhone(listPhone, oldP, oldNew)

		else:
			verifiedList(listPhone)
	elif resp == configs[0]:
		exit(0)
		
	configs[1]+= 1


showPhone(listPhone)
