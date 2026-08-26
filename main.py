# Importamos la clase Vehiculo desde el módulo vehiculoo
from vehiculoo import Vehiculo

# Inicializamos la lista con 3 vehículos predefinidos (marca, modelo, año, patente, tarifa_hora)
vehiculos = [
    # Instanciamos el primer vehículo: Toyota Yaris
    Vehiculo("Toyota", "Yaris", 2021, "AA-123-BB", 45),
    # Instanciamos el segundo vehículo: Chevrolet Sail
    Vehiculo("Chevrolet", "Sail", 2019, "KJ-456-ZX", 50),
    # Instanciamos el tercer vehículo: Nissan Versa
    Vehiculo("Nissan", "Versa", 2023, "PR-789-LM", 60)
]

# Imprimimos el encabezado para la sección de registro
print("=== INGRESO DE NUEVOS VEHÍCULOS AL SISTEMA ===")

# Iniciamos un bucle para permitir el ingreso continuo de vehículos
while True:
    # Solicitamos al usuario si desea agregar otro vehículo ('s' para sí, cualquier otra tecla para no)
    continuar = input("¿Desea ingresar un nuevo vehículo? (s/n): ").strip().lower()
    # Si la respuesta no es 's', salimos del bucle de registro
    if continuar != 's':
        break

    # Mostramos un separador visual
    print("\n--- Ingrese los datos del vehículo ---")
    # Solicitamos y limpiamos el texto de la marca
    marca = input("Marca: ").strip()
    # Solicitamos y limpiamos el texto del modelo
    modelo = input("Modelo: ").strip()
    
    # Bucle para validar que el año ingresado sea un número entero
    while True:
        try:
            # Convertimos la entrada a número entero
            anio = int(input("Año: ").strip())
            # Si la conversión fue exitosa, rompemos el bucle de validación
            break
        except ValueError:
            # Mostramos un mensaje de error si no se ingresó un número válido
            print("[ERROR] El año debe ser un número entero. Intente de nuevo.")
            
    # Solicitamos la patente y la convertimos a mayúsculas
    patente = input("Patente: ").strip().upper()
    
    # Bucle para validar que la tarifa ingresada sea un número entero
    while True:
        try:
            # Convertimos la tarifa a número entero
            tarifa = int(input("Tarifa por hora ($): ").strip())
            # Si la conversión fue exitosa, salimos del bucle de validación
            break
        except ValueError:
            # Mostramos mensaje de error en caso de entrada no numérica
            print("[ERROR] La tarifa debe ser un número entero. Intente de nuevo.")

    # Creamos la nueva instancia del objeto Vehiculo con los datos ingresados
    nuevo_vehiculo = Vehiculo(marca, modelo, anio, patente, tarifa)
    # Agregamos el nuevo vehículo a la lista general
    vehiculos.append(nuevo_vehiculo)
    # Mostramos mensaje de confirmación
    print(f"-> ¡Vehículo {marca} {modelo} [{patente}] agregado con éxito!\n")

# Imprimimos el encabezado del listado final
print("\n=== TODOS LOS VEHÍCULOS REGISTRADOS EN EL TALLER ===")
# Recorremos cada vehículo almacenado en la lista
for v in vehiculos:
    # Mostramos por consola los atributos obtenidos mediante sus métodos getters y tarifa_hora
    print(f"- {v.get_marca()} {v.get_modelo()} ({v.get_anio()}) | Patente: {v.get_matricula()} | Tarifa/Hora: ${v.tarifa_hora()} | Estado: {v.get_estado()}")
