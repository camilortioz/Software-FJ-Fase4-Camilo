"""Punto de entrada y diez operaciones de demostración del sistema."""
import logging
from pathlib import Path
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva

# Configuración del registro de eventos y errores.
RUTA_LOG = Path(__file__).parent / "logs" / "sistema.log"
RUTA_LOG.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=str(RUTA_LOG),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

def ejecutar_prueba(numero, descripcion, operacion):
    """Ejecuta una operación y registra tanto éxitos como errores."""
    print("\n{}. {}".format(numero, descripcion))
    try:
        resultado = operacion()
    except Exception as error:
        logging.exception("Operación %s fallida", numero)
        print("Error controlado: {}".format(error))
    else:
        logging.info("Operación %s completada: %s", numero, descripcion)
        print(resultado)
    finally:
        # finally se ejecuta tanto si la operación funciona como si falla.
        print("Fin de la operación.")

def main():
    """Prepara datos de ejemplo y ejecuta diez pruebas."""
    clientes = []
    sala = ReservaSala("S01", "Sala de reuniones", 50000)
    equipo = AlquilerEquipo("S02", "Proyector", 30000)
    asesoria = Asesoria("S03", "Asesoría de software", 80000)

    # 1. Registro correcto de un cliente.
    ejecutar_prueba(1, "Registrar cliente válido",
        lambda: clientes.append(Cliente("C01", "Laura Pérez", "laura@example.com", "3001234567")) or clientes[-1])

    # 2. Validación de correo electrónico incorrecto.
    ejecutar_prueba(2, "Rechazar correo inválido",
        lambda: Cliente("C02", "Pedro Ruiz", "correo-invalido", "3001234568"))

    # 3. Registro correcto de un segundo cliente.
    ejecutar_prueba(3, "Registrar segundo cliente",
        lambda: clientes.append(Cliente("C03", "Andrés Gómez", "andres@example.com", "3101234567")) or clientes[-1])

    # 4. Mismo método, diferentes resultados: polimorfismo.
    ejecutar_prueba(4, "Describir servicios con polimorfismo",
        lambda: "\n".join(servicio.describir() for servicio in (sala, equipo, asesoria)))

    # 5. Cálculo usando argumentos opcionales.
    ejecutar_prueba(5, "Calcular costo con descuento e impuesto",
        lambda: "Costo final: {}".format(sala.calcular_costo(2, descuento=10, impuesto=19)))

    # 6. Prueba negativa: la cantidad cero no es válida.
    ejecutar_prueba(6, "Rechazar cantidad cero",
        lambda: equipo.calcular_costo(0))

    # 7. Crear y confirmar una reserva.
    ejecutar_prueba(7, "Crear y confirmar reserva",
        lambda: (lambda reserva: (reserva.confirmar(), str(reserva))[1])(
            Reserva("R01", clientes[0], sala, 2)))

    # 8. Prueba negativa: duración negativa.
    ejecutar_prueba(8, "Rechazar reserva con cantidad negativa",
        lambda: Reserva("R02", clientes[0], equipo, -1))

    # 9. Prueba negativa: servicio no disponible.
    ejecutar_prueba(9, "Rechazar servicio no disponible",
        lambda: Reserva("R03", clientes[1],
            Asesoria("S04", "Asesoría temporal", 60000, False), 1))

    # 10. Crear y cancelar una reserva.
    ejecutar_prueba(10, "Cancelar reserva",
        lambda: (lambda reserva: (reserva.cancelar(), str(reserva))[1])(
            Reserva("R04", clientes[1], asesoria, 1)))

    print("\nDemostración finalizada. Revise logs/sistema.log.")

if __name__ == "__main__":
    main()
