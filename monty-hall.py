import random
 #1 representa un carro/premio
 #0 representa una cabra
 
stay = 0  # el numero de veces que que ganaste cuando no se cambio la desicion.
switch = 0 # el numero deveces que ganaste cuando se cambio la desicion.
 
for i in range(1000):
    lst = [1,0,0]           # una lista que contiene 1 carro y dos cabras
    random.shuffle(lst)     # se barajea la lista de manera aleatoria
 
    ran = random.randrange(3) # numero random que simula una decision
 
    user = lst[ran] # se obtiene el resultado de la desicion simulada
 
    del(lst[ran]) # se elimina ese elemento de la lista original
 
    huh = 0
    for i in lst: # getting a value 0 and deleting it
        if i ==0:
            del(lst[huh]) # deletes a goat when it finds it
            break
        huh+=1
 
    if user ==1: # if the original choice is 1 then stay adds 1
        stay+=1
 
    if lst[0] == 1: # if the switched value is 1 then switch adds 1
        switch+=1
 
print("Stay =",stay)
print("Switch = ",switch)
#Done by Sam Witton 09/04/2014