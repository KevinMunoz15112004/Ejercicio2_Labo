#ejercicio 1 
def usuario_contraseña():
    usuario= input("ingrese usuario: ")
    password=input("ingrese contraseña: ")
    while usuario!="Admin" or password!="Secret*":
        usuario= input("ingrese usuario: ")
        password=input("ingrese contraseña: ")
def menu_opciones():
        opcion=0
        while opcion!= 3 :
             print("-----Opciones------")
             print("1. Grados centígrados a grados Fahrenheit.")    
             print("2. Grados kelvins a grados centígrados.")
             print("3. Salir del programa.")
             opcion=int(input("seleccione una opcion: "))
             if opcion==1 :
                print("1. Grados centígrados a grados Fahrenheit.") 
                centigrados=float(input("ingrese grados centigrados: "))
                print("------------------------------------------------")
                fahrenheit=((1.8 * centigrados)+32 )
                print(f" De Grados centígrados {centigrados} a grados Fahrenheit  son : {fahrenheit:.2f}")
             elif opcion==2:
                print("2. Grados kelvins a grados centígrados.")
                kelvin=float(input("ingrese grados kelvins: "))
                print("------------------------------------------------")
                centigrados=((kelvin - 273.15 ))
                print(f"De Grados kelvins {kelvin} a grados centígrados son:  {centigrados:.2f}")
                
             else: 
               opcion==3
               print("Gracias por utilizar este programa")

def main():
    usuario_contraseña()
    menu_opciones()
main ()

    






