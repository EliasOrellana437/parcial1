## Integrantes
- Nombre: Ariel Adolfo Diaz Sosa
- Nombre: Elias Ernestro Orellana Vasquez

## Descripción
Este programa permite registrar los viajes en transporte público (ruta, costo y tiempo).
Al finalizar, el sistema muestra:
- La lista ordenada de viajes realizados.
- El gasto total semanal en transporte.
- El tiempo total invertido en los viajes.

## Archivos
- `viaje.py` = Contiene la clase `Viaje`.
- `registro.py` = Contiene la clase `RegistroViajes` para gestionar la lista de viajes.
- `main.py` = Clase principal que ejecuta el programa y permite la interacción con el usuario.
- `README.md` = Información general del proyecto y preguntas respondidas.

## Preguntas
### 1. ¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?
La ventaja principal es que el proyecto queda más ordenado y fácil de entender. Si hubiéramos metido todo en un solo archivo, se volvería un enredo enorme al querer buscar o modificar algo. En cambio, separando el código en clases y archivos distintos, cada parte cumple su función clara. Por ejemplo, la clase Viaje se encarga solo de los datos de un viaje, y la clase RegistroViajes administra todos los viajes. Así no nos perdemos entre tanto código y si algo falla sabemos exactamente dónde revisar.

### 2. ¿Cómo aplicaron la Programación Orientada a Objetos en su solución? Describan el papel de las clases creadas.
Lo aplicamos creando clases que representaban lo que necesitábamos para el programa. Por ejemplo:
Viaje: aquí definimos todo lo relacionado con un viaje en particular, como destino, precio, fechas, etc.
RegistroViajes: esta clase funciona como el “administrador” que guarda y organiza los viajes creados.
Además, en el main.py usamos esas clases para que el usuario pueda interactuar con el menú.
La idea fue que cada clase tuviera su propia responsabilidad, como se hace en la POO, y así mantener el código modular y reutilizable.

### 3. ¿De qué manera el uso de GitHub facilitó el trabajo colaborativo en equipo? Den un ejemplo concreto
GitHub nos facilito porque cada quien pudo trabajar a su ritmo sin chocar con lo del otro. Por ejemplo, uno se puso con la clase Viaje y el otro con RegistroViajes y el menú en main.py. Cada quien lo hizo en su propia rama y después, con un pull request, juntamos los cambios en la rama principal.
Un ejemplo concreto fue cuando ya estaba lista la clase Viaje y el otro agregó la de RegistroViajes en su archivo. Luego hizo un git pull y se mezclaron los cambios sin problema. Eso evitó que anduviéramos pasándonos archivos por WhatsApp o correo y que se perdieran avances.