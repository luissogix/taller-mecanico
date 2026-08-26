class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int, matricula: str):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__matricula = matricula
        self.__estado = "En espera"

    # --- Métodos del vehículo ---
    def ingresar(self):
        self.__estado = "Ingresado al taller"
        print(f"-> El vehículo {self.__marca} {self.__modelo} [{self.__matricula}] ha ingresado.")

    def entregar(self):
        self.__estado = "Entregado al cliente"
        print(f"-> El vehículo {self.__marca} {self.__modelo} [{self.__matricula}] ha sido entregado.")

    def tarifa_hora(self) -> int:
        return 50

    # --- Getters y Setters ---
    def get_marca(self) -> str:
        return self.__marca

    def get_modelo(self) -> str:
        return self.__modelo

    def get_anio(self) -> int:
        return self.__anio

    def get_matricula(self) -> str:
        return self.__matricula

    def get_estado(self) -> str:
        return self.__estado

    def set_estado(self, estado: str):
        self.__estado = estado


# ==========================================
# Clases Hijas con polimorfismo en tarifa
# ==========================================
class Auto(Vehiculo):
    def tarifa_hora(self) -> int:
        return 60


class Moto(Vehiculo):
    def tarifa_hora(self) -> int:
        return 40


class Camion(Vehiculo):
    def tarifa_hora(self) -> int:
        return 90


# ==========================================
# Clase Taller con los 3 métodos solicitados
# ==========================================
class Taller:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__vehiculos = []  # Lista privada de vehículos registrados

    def registrar_vehiculo(self, vehiculo: Vehiculo):
        self.__vehiculos.append(vehiculo)

    # 1. Buscar vehículo (con bucle hasta encontrarlo o escribir 'salir')
    def buscar_vehiculo(self) -> Vehiculo:
        while True:
            matricula = input("Ingrese la matrícula del vehículo a buscar (o 'salir'): ").strip().upper()
            if matricula == "SALIR":
                return None
            
            for v in self.__vehiculos:
                if v.get_matricula().upper() == matricula:
                    print(f"¡Vehículo encontrado! -> {v.get_marca()} {v.get_modelo()} ({v.get_estado()})")
                    return v
            
            print(f"[ERROR] Vehículo con matrícula '{matricula}' no encontrado. Intente nuevamente.\n")

    # 2. Ingresar vehículo
    def ingresar_vehiculo(self):
        print("\n--- INGRESO DE VEHÍCULO ---")
        vehiculo = self.buscar_vehiculo()
        if vehiculo:
            vehiculo.ingresar()

    # 3. Entregar vehículo
    def entregar_vehiculo(self):
        print("\n--- ENTREGA DE VEHÍCULO ---")
        vehiculo = self.buscar_vehiculo()
        if vehiculo:
            vehiculo.entregar()
            print(f"Tarifa por hora aplicada: ${vehiculo.tarifa_hora()}/h")
