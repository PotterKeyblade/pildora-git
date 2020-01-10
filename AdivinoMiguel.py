from random import randint, uniform,random;

nombre=input("¿Cuál es tu nombre?\n");
numeroaleatorio=int(randint(1,20));
intentos=1;
correcto=False;
try:
    valor=int(input("Bueno, "+ nombre +" estoy pensando en un número entre 1 y 20. Tienes 5 intentos para adivinar el número.\n"));

    while (intentos<5):
        print("",numeroaleatorio)
        if valor == numeroaleatorio:
            intentos=5;
            correcto=True;
        else:
            if numeroaleatorio>valor:
                valor=int(input("El número que estoy pensando es mayor\n"));
                intentos+=1;
            else:
                valor=int(input("El número que estoy pensando es menor\n"));
                intentos+=1;

    if correcto==True:
        print("Buen trabajo "+nombre+" adivinaste el número en ",intentos," intentos");
    else:
        print("Fin el número era ",numeroaleatorio);
except ValueError:
   print("Eso no es un número entero.");