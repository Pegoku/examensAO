import random

def llegir_llista_enters():
    l = []
    while True:
        a = input("introdueix un nombre: ")
        if a == ".":
            break
        l.append(int(a))
    return l

def senars_llista(llista):
    l = []
    # print(llista)
    if type(llista) == str:
        llista = llista.split(',')
    # print(llista)
    for i in list(llista):
        if int(i) % 2 != 0:
            l.append(int(i))
    return l

def sumar_parells_llista(llista):
    s = 0
    if type(llista) == str:
        llista = llista.split(',')    
    for i in llista:
        if int(i) % 2 == 0:
            s = s + int(i)
    return s

def cercar_numero_llista(llista, numero):
    # print(llista)
    l = []
    if type(llista) == str:
        llista = llista.split(',')
    for i in llista:
        l.append(int(i))
        
    if numero not in l:
        return -1
    else:
        for x, i in enumerate(l):
            if i == numero:
                return x+1
    
def llegir_llista_paraules():
    l = []
    while True:
        a = input("introdueix una paraula: ")
        if a == ".":
            break
        l.append(a)
    return l

def crear_paraula_llista(llista):
    l = ""
    
    if type(llista) == str:
        llista = llista.split(',')
        
    for i in llista:
        l = l + i[0]
    return l

def crear_llista_num_aleatoris():
    l = []
    for i in range(5):
        l.append(random.randint(1, 11))
    return l

def comparar_llistes(llista1, llista2):
    l = []
    if type(llista1) == str:
        llista1 = llista1.split(',')
    if type(llista2) == str:
        llista2 = llista2.split(',')

    for a, b in zip(llista1, llista2):
        if a == b:
            l.append(2)
        elif b in llista1:
            l.append(1)
        else:
            l.append(0)
    
    return l

def majors_edat(edat1, edat2):
    if edat1 > 17:
        print("Edat1 es major d'edat")
    else:
        print("Edat1 no es major d'edat")
    if edat2 > 17:
        print("Edat2 es major d'edat")
    else:
        print("Edat2 no es major d'edat")
        
def menu():
    start = True
    while True:
        if start:
            print("Quina funcio vols ejecutar:")
            print("1. Llegir llista d'enters")
            print("2. Senars llista")
            print("3. Sumar parells llista")
            print("4. Cercar numero llista")
            print("5. Llegir llista paraules")
            print("6. Crear paraula de llista")
            print("7. Crear llista de numeros aleatoris")
            print("8. Comparar valors llistes")
            print("9. Majors d'edat")
            print("10. Sortir")
            start = False
        a = input("Introdueix una opcio: ")
        if a == "1":
            start = True
            print(llegir_llista_enters())
        if a == "2":
            start = True
            x = input("Introdueix una llista de nombres (1,2,3,4...): ")
            print(senars_llista(x))
        if a == "3":
            start = True
            x = input("Introdueix una llista de nombres (1,2,3,4...): ")
            print(sumar_parells_llista(x))
        if a == "4":
            start = True
            x = input("Introdueix una llista de nombres (1,2,3,4...): ")
            y = int(input("Introdueix el numero a cercar: "))
            print(cercar_numero_llista(x, y))
        if a == "5":
            start = True
            print(llegir_llista_paraules())
        if a == "6":
            start = True
            x = input("Introdueix una llista de paraules (hola,sol,casa...): ")
            print(crear_paraula_llista(x))
        if a == "7":
            start = True
            print(crear_llista_num_aleatoris())
        if a == "8":
            start = True
            x = input("Introdueix una llista de nombres (1,2,3,4...): ")
            y = input("Introdueix un altre llista de nombres (1,2,3,4...): ")
            print(comparar_llistes(x, y))
        if a == "9":
            start = True
            x = int(input("Introdueix edat1: "))
            y = int(input("Introdueix edat2: "))
            majors_edat(x, y)
        if a == "10":
            start = True
            print("Adeu!!!")
            break
            
        
menu()