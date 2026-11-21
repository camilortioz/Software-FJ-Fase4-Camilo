# Software FJ – Fase 4

Sistema de gestión de clientes, servicios y reservas desarrollado en Python como actividad de Programación Orientada a Objetos.

## Funcionalidades

- Registro y validación de datos de clientes.
- Administración de reservas de salas, alquiler de equipos y asesorías.
- Clases abstractas, herencia, encapsulamiento y polimorfismo.
- Cálculo de costos con cantidad, descuento e impuesto.
- Confirmación, cancelación y procesamiento de reservas.
- Excepciones personalizadas y encadenamiento de errores.
- Manejo de excepciones con `try/except/else/finally`.
- Registro de eventos y errores mediante `logging`.
- Once operaciones de demostración.

## Estructura

- `main.py`: ejecución del programa y operaciones de demostración.
- `entidad.py`: clase abstracta base.
- `cliente.py`: información y validaciones del cliente.
- `servicios.py`: clase abstracta y tipos de servicio.
- `reservas.py`: administración de las reservas.
- `excepciones.py`: excepciones del sistema.
- `logs/`: carpeta donde se genera el registro de ejecución.

## Requisitos

Python 3.10 o superior. No requiere instalar paquetes externos.

## Ejecución

Desde la carpeta del proyecto, ejecutar:

```bash
python main.py
```

El programa presenta las operaciones en consola y genera el archivo `logs/sistema.log` con los eventos y errores registrados durante la ejecución.
