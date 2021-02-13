print ("calculadora")

print("menu opciones :\n")

print ("1.suma")
print ("2.resta")
print ("3.multiplicacion")
print ("4.division")
print ("5.division entera")
print ("6.exponente")
print ("7.modulo o resto\n")

numero = int (input("introduce la opcion deseada: "))

if numero==1:
    print("elijas los valores que requieres sumar.\n")

    numero = int (input("que valor quieres?: "))
    numero+= int (input("que valor requieres?: "))
    print ("el resultado es ", numero , "\n",)
    

elif numero==2:
    print ("elija los valores que requieres restar. \n")

    numero = int (input("que valor quieres?: "))
    numero-= int (input("que valor requieres?: "))
    print ("el resultado es", numero, "\n",)


elif numero==3:
    print("elija los valores que requieres multiplicar. \n")

    numero = int (input("que valor quieres?: "))
    numero*= int (input("que valor requieres?: "))
    print ("el resultado es", numero, "\n",)

elif numero==4:
    print ("elija los valores que requieres dividir. \n")

    numero = float (input("que valor quieres?: "))
    numero/= float (input("que valor requieres?: "))
    print ("el resultado es", numero, "\n",)

elif numero==5:
    print ("elija los valores que requieres dividir entero. \n")

    numero = int (input("que valor quieres?: "))
    numero//= int (input("que valor requieres?: "))
    print ("el resultado es", numero, "\n",)

elif numero==6:
    print ("elija los valores que requieres exponer. \n")

    numero = int (input("que valor quieres?: "))
    numero**= int (input("que valor requieres?: "))
    print ("el resultado es", numero, "\n",)

elif numero==7:
    print ("elija los valores que requieres del modulo o resto. \n")

    numero = int (input("que valor quieres?: "))
    numero %= int (input("que valor requieres?: "))
    print ("el resultado es", numero , "\n",)
       


else:
    print ("la opcion no es disponible.")


  









    
    

