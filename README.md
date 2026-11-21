# Software FJ – Fase 4

Proyecto académico de Programación Orientada a Objetos – UNAD. El sistema representa la gestión básica de clientes, servicios y reservas.

## Funcionalidades implementadas
- Clase abstracta Entidad y clase Cliente con atributos encapsulados y validaciones.
- Clase abstracta Servicio y tres especializaciones: ReservaSala, AlquilerEquipo y Asesoria.
- Herencia y polimorfismo mediante el método describir.
- Cálculo de costos con cantidad, descuento e impuesto opcionales.
- Creación, confirmación, cancelación y procesamiento de reservas.
- Excepciones personalizadas y encadenamiento de errores.
- Manejo de try/except/else/finally y registro de eventos y errores.
- Diez operaciones de demostración, con escenarios correctos e incorrectos.

## Estructura del proyecto
- main.py: punto de entrada y pruebas.
- entidad.py: clase abstracta base.
- cliente.py: datos y validaciones del cliente.
- servicios.py: clase abstracta y servicios concretos.
- reservas.py: estados y operaciones de reserva.
- excepciones.py: excepciones propias.
- logs/sistema.log: registro de ejecución.

## Requisitos y ejecución
Se requiere Python 3.10 o superior. No se necesitan paquetes externos.

Desde la carpeta del proyecto, ejecutar:

    python main.py

Las diez operaciones se muestran en consola. Los eventos y errores se registran en logs/sistema.log.

## Consideraciones para la entrega
Este repositorio contiene el código fuente del proyecto. Antes de entregar, se debe ejecutar y revisar el programa, conservar evidencia de las pruebas y completar el documento PDF y el notebook solicitados por la guía de la actividad. El estudiante debe comprender el código y verificar que las evidencias correspondan a su propio trabajo.
