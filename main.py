#En El Salvador, muchas personas dependen del transporte público para ir
#a su trabajo, estudio o actividades diarias. Cada día realizan distintos viajes
#en rutas urbanas o rurales, con tiempos y costos variables. Sin un registro,
#es difícil saber cuánto se gasta en transporte semanalmente ni cuáles rutas
#consumen más tiempo o dinero.
#Se busca un sistema que permita registrar los viajes realizados, y generar
#una salida en pantalla al final que muestre los datos ordenados de cada
#viaje realizado. Además, el sistema debe mostrar un resumen con el gasto
#total semanal y el tiempo total invertido.

from registro import RegistroViajes

def menu():
    print("\n Registro de viajes - El Salvador")
    print("1. Agregar viaje")
    print("2. Mostrar viajes")
    print("3. Mostrar resumen")
    print("4. Salir")
# registros de viajes nuevos aunque creo que son redundantes porque ya estan en registro.py XD
def main():
    registro = RegistroViajes()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ruta = input("Ingrese la ruta del viaje: ")
            costo = float(input("Ingrese el costo del viaje ($): "))
            tiempo = int(input("Ingrese el tiempo del viaje (minutos): "))
            registro.agregar_viaje(ruta, costo, tiempo)
            print(" Viaje registrado con éxito.")

        elif opcion == "2":
            registro.mostrar_viajes()

        elif opcion == "3":
            registro.resumen()

        elif opcion == "4":
            print(" ¡Gracias por usar el sistema de registro de viajes!")
            break

        else:
            print(" Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()

