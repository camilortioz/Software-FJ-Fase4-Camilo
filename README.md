# Software FJ – Fase 4

Proyecto académico de Programación Orientada a Objetos – UNAD. El sistema representa la gestión básica de clientes, servicios y reservas.

## Funcionalidades
- Clase abstracta `Entidad` y clase `Cliente` con atributos encapsulados y validados.
- Clase abstracta `Servicio` y tres especializaciones: `ReservaSala`, `AlquilerEquipo` y `Asesoria`.
- Herencia y polimorfismo mediante el método `describir()`.
- Cálculo de costos con cantidad, descuento e impuesto opcionales.
- Creación, confirmación, cancelación y procesamiento de reservas.
- Excepciones personalizadas y encadenamiento con `raise ... from error`.
- Manejo de `try/except/else/finally`.
- Registro de operaciones y errores mediante el módulo `logging`.
- Once operaciones de demostración, con escenarios correctos e incorrectos.

## Estructura del proyecto
- `main.py`: punto de entrada y once pruebas de demostración.
- `entidad.py`: clase abstracta base de las entidades.
- `cliente.py`: datos y validaciones del cliente.
- `servicios.py`: clase abstracta y servicios concretos.
- `reservas.py`: estados y operaciones de reserva.
- `excepciones.py`: excepciones personalizadas.
- `logs/sistema.log`: archivo generado durante la ejecución para registrar eventos y errores.

## Requisitos y ejecución
Se requiere Python 3.10 o superior. No se necesitan paquetes externos.

Desde la carpeta del proyecto, ejecutar:

    python main.py

Las once operaciones se muestran en consola. El programa crea la carpeta `logs` y el archivo `sistema.log` si todavía no existen. Los registros incluyen fecha, hora, nivel del evento y mensaje. Cuando ocurre un error, se almacena también la información técnica de la excepción.

## Relación con los referentes bibliográficos
El desarrollo toma como apoyo los contenidos de programación, clases, herencia y manejo de excepciones de los siguientes recursos:

- Van Rossum y Drake Jr. (2024): tutorial de Python, especialmente los apartados 8 (errores y excepciones) y 9 (clases).
- Cuevas Álvarez (2016): capítulo 7, especialmente la sección 7.2 sobre excepciones y su manejo, incluidas las estructuras `try-except-else-finally`, las excepciones personalizadas y el encadenamiento.
- Mishra (2024): fundamentos de Git y GitHub para el control de versiones y el trabajo colaborativo.

## Referencias
Cuevas Álvarez, A. (2016). *Python 3: curso práctico*. RA-MA Editorial. https://elibro-net.bibliotecavirtual.unad.edu.co/es/ereader/unad/106404?page=373

Mishra, P. (2024). *Ultimate Git and GitHub for Modern Software Development*. Orange Education Pvt Ltd. https://research-ebsco-com.bibliotecavirtual.unad.edu.co/c/qcagk4/ebookviewer/pdf/fhmr6uslr5/section/lp_4

Van Rossum, G., & Drake Jr., F. L. (2024). *El tutorial de Python*. Python Software Foundation. https://docs.python.org/es/3.12/tutorial/index.html

Silva, F. D. (2025). *Basics of using GitHub* [Objeto virtual de información]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/75882

Zambrano, J. P. (2025). *Introducción al uso de GitHub* [Objeto virtual de información]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/75876

## Consideraciones para la entrega
Este repositorio contiene el código fuente del proyecto. Antes de entregar, se debe ejecutar y revisar el programa, conservar evidencia de las pruebas y completar el documento PDF y el notebook solicitados por la guía de la actividad. El estudiante debe comprender el código y verificar que las evidencias correspondan a su propio trabajo.
