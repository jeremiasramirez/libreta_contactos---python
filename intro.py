# val = "jeremiasiiee e"


# i = 0
# b = "i" 
# coun = []

# while i < len(val):
# 	if val[i] == b:
# 		coun.append(val[i])
# 	i += 1
# print(len(coun))

#import json

#with open('json.json') as f:
#	data = json.loads(f.read())

# arr = [11, 2, "n", "e"]
# arr.remove("n")
# print(arr)

# class users:
# 	def __init__(self, nombre=[]):
# 		self.nombre = nombre
 
# 	def eliminar(self, newName):
# 		notfound = False

# 		for i in self.nombre:

# 			if i == newName:
# 				self.nombre.remove(newName)

# 		if notfound == True:
# 			print("Elemento no encontrado")

# 	def mostrar(self):
# 		for i in self.nombre:
# 			print(i)

# arr = ["jeremias", "alfonso", "perez", "marino", "12", 22]

# n1 = users(arr);
# n1.eliminar("12")
# n1.mostrar()
# cars = [] 
# for i in range(0,3):
# 	name = input("Your cars favorite: ")
# 	cars.append(name)

# for c in cars:
# 	print("cars: ", c)
'''
number = 12.2
a = float(number)
print a
# '''
# class Account:

# 	def removes(self, elements):
# 		print elements, "es edad alta, se removera pronto..."
# 		elements = 12
# 		print elements, "se puso en orden."

# 	def add(self, val):

# 		val = int(val)
# 		if val > 20:
# 			self.removes(val);
# 		else:
# 			print val, "es edad acorde";


# instance = Account();
# instance.add(22)

# def validate(n1, n2):
# 	if n2 > n1:
# 		print "Imposible de obtener resultados positivos"
# 	else:
# 		print "Imposible de operar"
 

# def restar(n1="", n2=""):
# 	if n1 == "" or n2 == "":
# 		print "Imposible de operar"
# 	else:
# 		if n2 > n1:
# 			validate(n1, n2)
# 		else:
# 			print "resultado: ", (n1 - n2)
 
# import json
# def 
# with open("test.json") as f:
# 	data = json.loads(f.read())
	
# for i in data:
# 	print ("Nombre: ", i["name"], "Version: ", i["version"]);
  
# class Data:
# 	#private methods
# 	__name = 12

# 	def getter(self):
# 		print(self.__name)

# 	def setter(self, val_new):
# 		self.__name = val_new

# # instance of class Data
# n = Data()

# val2 = n.setter(22);
# val = n.getter();
# import json

# links = {"test": "test.json"}

# with open(links.values()[0]) as f:
# 	data = json.loads(f.read())

# for i in data:
# 	print i["name"]
# 	print i["description"]
# 	print i["main"]
# 	print i["version"], "\n";

#app number call list
def addPhone(val):
	listPhone.append(val);

def showPhone(list):
	for i in list:
		print(i);

def removePhone(lists, val):
	for k in lists:
		if k == val:
			lists.remove(val)

def verifiedList(lists):
	if lists != []:
		print("Listas de contactos..")
	else:
		print("La lista esta vacia")

def updatePhone(lists, oldPhone, newPhone):
	for n in lists:
		if n == oldPhone:
			lists.remove(n)
			lists.append(newPhone)





listPhone = ["8297510847"]
i = 0
val = 0
resp = "agregar"

while resp != "salir" :
	resp = input("MOSTRAR | ACTUALIZAR | ELIMINAR | AGREGAR: ")

	if resp == "mostrar":
		verifiedList(listPhone)
		showPhone(listPhone)

	elif resp == "agregar":
		val = input("agregar numero: ")
		addPhone(val)

	elif resp == "eliminar":
		if listPhone != []:
			delete = input("Numero a eliminar: ")
			removePhone(listPhone, delete);
		else:
			verifiedList(listPhone)
	elif resp == "actualizar":
		if listPhone != []:
			oldP = input("Numero viejo: ")
			oldNew = input("Numero nuevo: ")
			updatePhone(listPhone, oldP, oldNew)
		else:
			verifiedList(listPhone)

	i += 1


showPhone(listPhone)
