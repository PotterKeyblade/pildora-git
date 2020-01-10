import random

contador=0;
centinela="hola";
nombre = input("¿Cuál es tu nombre?\n");

print("Bueno ", nombre ," estoy pensando en un número entre el 1 y el 20");

numeroaleatorio = random.randint(1, 20);
try: 
    for i in range(5):
        if(centinela):
            num = int(input("Introduce el número: "));

            if(num < numeroaleatorio):
                print("El número escogido está por debajo");
                contador = contador+1;
                print("Numero de intentos: ", contador);
            else:
                if(num>numeroaleatorio):
                    print("El número escogido está por encima");
                    contador = contador + 1;
                    print("Numero de intentos: ", contador);
                else:
                    print("El número es el correcto");
                    centinela = "";
    if(centinela):                
        print("Adiós");
except ValueError:
    print("F");

