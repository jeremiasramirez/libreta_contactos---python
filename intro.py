#app number call list

# add number call
def addPhone(val, lists):
	k = 0
	adTrue = False

	while k < len(lists):
		if val == lists[k]:
			adTrue = True
		k += 1

	if adTrue == True:
		print("\n",val, "Ya se encuentra agregado.\n\n")
	else:
		listPhone.append(val);

def showPhone(list):
	for i in list:
		print(i);
	print("\n")
# remove number call
def removePhone(lists, val):
	for k in lists:
		if k == val:
			lists.remove(val)

# verified existence number call
def verifiedList(lists):
	iterators = 0
 
	while iterators < len(lists):
		iterators +=1

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

	while n < len(lists):
		if lists[n] == oldPhone:
			lists[n] = newPhone
			valid = True
		n += 1

	if valid == False:
		print("Ese numero no existe")

 
 
listPhone = ["8297510847", "8092221284", "8295466271"]

configs = {
	0: "salir",
	1: 0,
	2: "mostrar",
	3: "eliminar",
	4: "agregar",
	5: "actualizar"
}

resp = configs[3]

while resp != configs[0]:
	resp = input("MOSTRAR | ACTUALIZAR | ELIMINAR | AGREGAR: ")

	if resp == configs[2]:

		verifiedList(listPhone)
		showPhone(listPhone)

	elif resp == configs[4]:
		val = input("agregar numero: ")
		addPhone(val, listPhone)

	elif resp == configs[3]:
		if listPhone != []:
			delete = input("Numero a eliminar: ")
			removePhone(listPhone, delete);
		else:
			verifiedList(listPhone)

	elif resp == configs[5]:
		if listPhone != []:
			oldP = input("Numero viejo: ")
			oldNew = input("Numero nuevo: ")
			updatePhone(listPhone, oldP, oldNew)
		else:
			verifiedList(listPhone)
	configs[1]+= 1


showPhone(listPhone)
