# Sistema de Gestión de Taller Mecánico

Proyecto desarrollado en **Python** aplicando los principios de la **Programación Orientada a Objetos (POO)** para la gestión y control de vehículos en un taller mecánico.

---

## 📌 Resumen de lo realizado hoy

1. **Creación del Repositorio y Entorno Local:**
   - Inicialización del repositorio remoto en GitHub: [`taller-mecanico`](https://github.com/luissogix/taller-mecanico).
   - Estructuración del espacio de trabajo local con soporte para Visual Studio Code.

2. **Diseño de la Clase Base `Vehiculo` (`vehiculoo.py`):**
   - **Encapsulamiento estricto:** Atributos privados (`__marca`, `__modelo`, `__anio`, `__matricula`, `__tarifa_hora`, `__estado`).
   - **Constructor (`__init__`):** Inicialización de todos los datos del vehículo.
   - **Métodos principales:**
     - `ingresar()`: Cambia el estado del vehículo a *"Ingresado al taller"*.
     - `entregar()`: Cambia el estado a *"Entregado al cliente"*.
     - `tarifa_hora()`: Retorna el valor por hora de servicio.
   - **Getters y Setters clásicos:** Métodos de acceso y modificación para cada atributo privado.

3. **Herencia y Polimorfismo:**
   - Creación de subclases (`Auto`, `Moto`, `Camion`) que heredan de `Vehiculo` con tarifas diferenciadas.

4. **Clase `Taller`:**
   - Métodos de gestión: `buscar_vehiculo()`, `ingresar_vehiculo()` y `entregar_vehiculo()`.
   - Implementación de un bucle interactivo (`while`) que valida la existencia del vehículo y repite la solicitud si la matrícula no coincide.

5. **Módulo Principal (`main.py`):**
   - Importación de la clase `Vehiculo`.
   - Creación e instanciación de 3 vehículos base con marcas, modelos, años, patentes y tarifas por hora.
   - Implementación de un sistema interactivo por consola para registrar nuevos vehículos con validación de tipos (`try/except`).
   - Comentarios explicativos línea por línea de todo el flujo de ejecución.

---

## 📂 Estructura del Proyecto

```
taller-mecanico/
│
├── README.md        # Documentación general del proyecto (en la raíz)
├── vehiculoo.py     # Clases Vehiculo, subclases y Taller con lógica POO
└── main.py          # Script principal con ejecución, registro y listado
```

---

## 🚀 Cómo ejecutar el proyecto

1. Abrir una terminal en la raíz del proyecto.
2. Ejecutar el archivo principal:
   ```bash
   python main.py
   ```
3. Seguir las instrucciones en pantalla para ingresar nuevos vehículos o visualizar el listado final.
