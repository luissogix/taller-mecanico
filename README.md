# Taller Mecánico - Sistema de Gestión

Repositorio para la asignatura de **Programación Orientada a Objetos Seguro**.

- **Institución:** Inacap
- **Profesor:** Michael Arjel

---

## 🛠️ Descripción del Proyecto

Este sistema administra las operaciones de un taller mecánico mediante una arquitectura basada en **Programación Orientada a Objetos (POO)** y el patrón de diseño **Data Access Object (DAO)**. Utiliza una base de datos relacional **SQLite** con control de integridad referencial.

---

## 📁 Estructura del Proyecto

```text
taller mecanico/
├── conectar.py           # Gestión de la conexión a SQLite (taller.db) y activación de Foreign Keys
├── main.py               # Punto de entrada principal e inicialización de tablas mediante los DAOs
├── PROMPTS_MAESTROS.md   # Registro de prompts y guías utilizadas en el desarrollo
├── README.md             # Documentación del proyecto
├── dao/                  # Capa de Acceso a Datos (Data Access Object)
│   ├── dao.py            # Clase base DAO (Manejo de conexión y cursor)
│   ├── marca_dao.py      # DAO para la gestión de Marcas
│   ├── modelo_dao.py     # DAO para la gestión de Modelos
│   ├── vehiculo_dao.py   # DAO para la gestión de Vehículos
│   └── auto_dao.py       # DAO para la gestión de Autos (Herencia relacional)
└── model/                # Capa de Dominio / Modelos
    ├── persona.py        # Clase base Persona
    ├── cliente.py        # Modelo Cliente (Hereda de Persona)
    ├── usuario.py        # Modelo Usuario (Hereda de Persona)
    ├── rol.py            # Modelo Rol
    ├── marca.py          # Modelo Marca
    ├── modelo.py         # Modelo Modelo
    ├── vehiculo.py       # Clase base Vehículo
    ├── auto.py           # Modelo Auto (Hereda de Vehículo)
    ├── moto.py           # Modelo Moto (Hereda de Vehículo)
    ├── camion.py         # Modelo Camión (Hereda de Vehículo)
    ├── ordentrabajo.py   # Modelo OrdenTrabajo
    ├── lineadetalle.py   # Modelo LineaDetalle
    └── repuesto.py       # Modelo Repuesto
```

---

## 🚀 Tecnologías y Conceptos Aplicados

- **Lenguaje:** Python 3
- **Base de Datos:** SQLite (`taller.db`)
- **Paradigmas y Patrones:**
  - **POO:** Encapsulamiento, Herencia, Polimorfismo.
  - **Patrón DAO:** Separación de la lógica de acceso a datos de la lógica de dominio.
  - **Herencia Relacional:** Estrategia *Table-per-type* (por ejemplo, la tabla `autos` relaciona su llave primaria con la llave foránea de `vehiculos`).

---

## 📋 Bitácora de Avances

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (`gh auth`).
- **Clase Base `Vehiculo`:** Implementación de atributos privados (`__patente`, `__anio`, `__en_taller`), encapsulamiento y métodos `ingresar()`, `entregar()` y `tarifa_hora()`.
- **Script de Pruebas Inicial:** Creación del punto de entrada `main.py` para instanciación y validación inicial.

### 31 de Agosto de 2026
- **Implementación de Herencia (Subclases):**
  - **`Auto`:** Atributo de capacidad de maletero.
  - **`Moto`:** Estructura base heredada.
  - **`Camion`:** Atributo de capacidad de carga.
- **Actualización de Script Principal:** Pruebas de polimorfismo y consumo de métodos heredados.

### 15 de Septiembre de 2026
- **Integración con SQLite (`conectar.py`):** Configuración de la base de datos `taller.db` y activación de `PRAGMA foreign_keys = ON`.
- **Arquitectura en Capas (Paquetes `model` y `dao`):** Modularización completa del código.
- **Implementación del Patrón DAO:**
  - Clase base `Dao` en `dao.py`.
  - Implementación de `MarcaDao`, `ModeloDao`, `VehiculoDao` y `AutoDao` para creación de tablas y gestión relacional.
- **Refactorización de `main.py`:** Configuración orientada a la inicialización y verificación de la estructura de tablas.
