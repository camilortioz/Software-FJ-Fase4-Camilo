"""Punto de entrada y once operaciones de demostración del sistema."""
import logging
from pathlib import Path

from cliente import Cliente
from excepciones import ReservaInvalidaError
from reservas import Reserva
from servicios import ReservaSala, AlquilerEquipo, Asesoria


# La carpeta y el archivo de registro se crean automáticamente si no existen.
RUTA_LOG = Path(__file__).parent / "logs" / "sistema.log"
RUTA_LOG.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(RUTA_LOG),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
)


def ejecutar_prueba(numero, descripcion, operacion):
    """Ejecuta una operación y registra el resultado en el archivo de log."""
    print("\n{}. {}".format(numero, descripcion))
    try:
        resultado = operacion()
    except Exception as error:
        # exception() guarda el mensaje y la traza técnica del error.
        logging.exception("Operación %s: %s", numero, descripcion)
        print("Error controlado: {}".format(error))
    else:
        logging.info("Operación %s completada: %s", numero, descripcion)
        print(resultado)
    finally:
        # Este bloque se ejecuta tanto si la operación funciona como si falla.
        print("Fin de la operación.")


def probar_encadenamiento(cliente, servicio):
    """Comprueba el procesamiento y que el error conserve su causa."""
    reserva = Reserva("R05", cliente, servicio, 1)
    primer_estado = reserva.procesar()

    try:
        # La segunda confirmación no es válida porque ya está confirmada.
        reserva.procesar()
    except ReservaInvalidaError as error:
        causa = type(error.__cause__).__name__
        return (
            "Primer procesamiento: {}. Segundo intento controlado: {}. "
            "Causa original: {}."
        ).format(primer_estado, error, causa)

    return "No se produjo el error esperado al procesar dos veces."


def main():
    """Prepara datos de ejemplo y ejecuta once operaciones."""
    clientes = []
    sala = ReservaSala("S01", "Sala de reuniones", 50000)
    equipo = AlquilerEquipo("S02", "Proyector", 30000)
    asesoria = Asesoria("S03", "Asesoría de software", 80000)

    # 1. Registro correcto de un cliente.
    ejecutar_prueba(
        1, "Registrar cliente válido",
        lambda: clientes.append(
            Cliente("C01", "Laura Pérez", "laura@example.com", "3001234567")
        ) or clientes[-1],
    )

    # 2. Validación de correo electrónico incorrecto.
    ejecutar_prueba(
        2, "Rechazar correo inválido",
        lambda: Cliente("C02", "Pedro Ruiz", "correo-invalido", "3001234568"),
    )

    # 3. Registro correcto de un segundo cliente.
    ejecutar_prueba(
        3, "Registrar segundo cliente",
        lambda: clientes.append(
            Cliente("C03", "Andrés Gómez", "andres@example.com", "3101234567")
        ) or clientes[-1],
    )

    # 4. Un mismo método produce descripciones según el tipo de servicio.
    ejecutar_prueba(
        4, "Describir servicios con polimorfismo",
        lambda: "\n".join(
            servicio.describir() for servicio in (sala, equipo, asesoria)
        ),
    )

    # 5. Se usan argumentos opcionales para cantidad, descuento e impuesto.
    ejecutar_prueba(
        5, "Calcular costo con descuento e impuesto",
        lambda: "Costo final: {}".format(
            sala.calcular_costo(2, descuento=10, impuesto=19)
        ),
    )

    # 6. La cantidad cero debe producir una excepción personalizada.
    ejecutar_prueba(
        6, "Rechazar cantidad cero",
        lambda: equipo.calcular_costo(0),
    )

    # 7. Crear y confirmar una reserva.
    ejecutar_prueba(
        7, "Crear y confirmar reserva",
        lambda: (lambda reserva: (reserva.confirmar(), str(reserva))[1])(
            Reserva("R01", clientes[0], sala, 2)
        ),
    )

    # 8. La cantidad negativa no es válida para una reserva.
    ejecutar_prueba(
        8, "Rechazar reserva con cantidad negativa",
        lambda: Reserva("R02", clientes[0], equipo, -1),
    )

    # 9. No se permite reservar un servicio no disponible.
    ejecutar_prueba(
        9, "Rechazar servicio no disponible",
        lambda: Reserva(
            "R03", clientes[1],
            Asesoria("S04", "Asesoría temporal", 60000, False), 1
        ),
    )

    # 10. Crear y cancelar una reserva.
    ejecutar_prueba(
        10, "Cancelar reserva",
        lambda: (lambda reserva: (reserva.cancelar(), str(reserva))[1])(
            Reserva("R04", clientes[1], asesoria, 1)
        ),
    )

    # 11. Procesar una reserva y comprobar el encadenamiento de excepciones.
    ejecutar_prueba(
        11, "Procesar reserva y comprobar la causa de una excepción",
        lambda: probar_encadenamiento(clientes[0], sala),
    )

    print("\nDemostración finalizada. Revise logs/sistema.log.")
    print("El archivo de log se encuentra en: {}".format(RUTA_LOG))


if __name__ == "__main__":
    main()
