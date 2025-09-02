from viaje import Viaje

class RegistroViajes:
    def __init__(self):
        self.viajes = []
#Dato curioso, quisimos cambiar el nombre del metodo agregar_viaje a AgregarViaje pero no se pudo porque python no deja mayusculas en los metodos XD, asi que dejamos el nombre original.
    def agregar_viaje(self, ruta, costo, tiempo):
        nuevo_viaje = Viaje(ruta, costo, tiempo)
        self.viajes.append(nuevo_viaje)
#lo mismo con mostrar_viajes, quisimos cambiarlo a MostrarViajes pero no se pudo.
    def mostrar_viajes(self):
        print("\n Lista de viajes registrados:")
        for i, viaje in enumerate(self.viajes, start=1):
            print(f"{i}. {viaje}")
#Este si lo dejo 
    def resumen(self):
        total_costo = sum(v.costo for v in self.viajes)
        total_tiempo = sum(v.tiempo for v in self.viajes)
        print("\n Resumen semanal:")
        print(f"  Gasto total: ${total_costo:.2f}")
        print(f"  Tiempo total: {total_tiempo} minutos")
