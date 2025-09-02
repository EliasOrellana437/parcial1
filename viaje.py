
class Viaje:
    def __init__(self, ruta, costo, tiempo):
        self.ruta = ruta
        self.costo = costo
        self.tiempo = tiempo
# Esta linea la agregue para que al mostrar los viajes se vea mejor el formato, por que si lo dejaba asi nomas se veia feo.
    def __str__(self):
        return f"Ruta: {self.ruta} | Costo: ${self.costo:.2f} | Tiempo: {self.tiempo} min"
