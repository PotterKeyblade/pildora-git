import random;

random = random.randint(1,20);

nombre=  input("¿Como te llamas?\n")
print("Hola ", nombre , ", he pensado en jugar a algo. ¿Te parece bien?\n¡Empecemos!")
print("\n\rEstoy pensando en un número entre 1 y 20.")
try:
    num=int(input("¿Cual es?\n"))
    contador=5

    while num != random and contador>0:
        if num < random:
            contador = contador -1
            print("Te quedan ", contador, " intentos")
            print("El número que he pensado es más alto");
            num=int(input("¿Cual es?\n"));
            
        if num > random:
            contador = contador -1
            print("Te quedan ", contador, " intentos")
            print("El número que he pensado es más bajo");
            num=int(input("¿Cual es?\n"));

    if contador==0:
        print(nombre," eres un perdedor")
        print("El número era: ", random)

    if num == random:
        print("¡Bien hecho, ", nombre, "!")
        print("Nº de intentos: ", 5-contador)
except :
    print("Algo ha ido mal")



