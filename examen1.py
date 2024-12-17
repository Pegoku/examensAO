import random

def llegir_llista_enters():
    l = []
    while True:
        a = int(input("introdueix un nombre"))
        if a == ".":
            break
        l.append(a)
    return l

def senars_llista(llista):
    l = []
    # print(llista)
    if type(llista) == str:
        llista = llista.split(',')
    for i in list(llista):
        if int(i) % 2 != 0:
            l.append(i)
    return l

def sumar_parells_llista(llista):
    s = 0
    print(llista)
    llista = llista.split(',')
        
    for i in llista:
        if i % 2 == 0:
            s = s + i
    return s

def cercar_numero_llista(llista, numero):
    # print(llista)
    if type(llista) == str:
        llista = llista.split(',')
    
    if numero not in llista:
        return -1
    else:
        for x, i in enumerate(llista):
            if i == numero:
                return x
    
def llegir_llista_paraules():
    l = []
    while True:
        a = input("introdueix una paraula")
        if a == ".":
            break
        l.append(a)
    return l

def crear_paraula_llista(llista):
    l = ""
    
    # print(llista)
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
    # print(llista)
    if type(llista1) == str:
        llista1 = llista1.split(',')
    # print(llista)
    if type(llista2) == str:
        llista2 = llista2.split(',')

    for a,b in llista1, llista2:
        if a == b:
            l.append(2)
        elif a in llista2:
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
    
# def ejecutar(func, nArgs):
#     args = []
#     for i in range(nArgs):
#         args.append(input("Introdueix argument n.{}".format(i+1)))
#     return func(*args)
        
def menu():
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
    while True:
        a = int(input("Introdueix una opcio: "))
        if a == 1:
            print(llegir_llista_enters())
        if a == 2:
            x = input("Introdueix argument 1: ")
            print(senars_llista(x))
        if a == 3:
            x = input("Introdueix argument 1: ")
            print(sumar_parells_llista(x))
        if a == 4:
            x = input("Introdueix argument 1: ")
            y = int(input("Introdueix argument 2: "))
            print(cercar_numero_llista(x, y))
        if a == 5:
            print(llegir_llista_paraules())
        if a == 6:
            x = input("Introdueix argument 1: ")
            print(crear_paraula_llista(x))
        if a == 7:
            print(crear_llista_num_aleatoris())
        if a == 8:
            x = input("Introdueix argument 1: ")
            y = input("Introdueix argument 2: ")
            print(comparar_llistes(x, y))
        if a == 9:
            x = int(input("Introdueix argument 1: "))
            y = int(input("Introdueix argument 2: "))
            majors_edat(x, y)
        if a == 10:
            print("Adeu!!!")
            break
            
        
                
                
# print(senars_llista())
menu()