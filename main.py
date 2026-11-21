import logging
from pathlib import Path
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva

RUTA_LOG = Path(__file__).parent / "logs" / "sistema.log"
RUTA_LOG.parent.mkdir(exist_ok=True)
logging.basicConfig(filename=RUTA_LOG, level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s", encoding="utf-8")

def ejecutar_prueba(numero, descripcion, operacion):
    print("\\n{}. {}".format(numero, descripcion))
    try:
        resultado = operacion()
    except Exception as error:
        logging.exception("Operación %s fallida", numero)
        print("Error controlado: {}".format(error))
    else:
        logging.info("Operación %s completada", numero)
        print(resultado)
    finally:
        print("Fin de la operación.")

def main():
    clientes = []
    sala = ReservaSala("S01", "Sala de reuniones", 50000)
    equipo = AlquilerEquipo("S02", "Proyector", 30000)
    asesoria = Asesoria("S03", "Asesoría de software", 80000)

    ejecutar_prueba(1, "Registrar cliente válido",
        lambda: clientes.append(Cliente("C01", "Laura Pérez", "laura@example.com", "3001234567")) or clientes[-1])
    ejecutar_prueba(2, "Rechazar correo inválido",
        lambda: Cliente("C02", "Pedro Ruiz", "correo-invalido", "3001234568"))
    ejecutar_prueba(3, "Registrar segundo cliente",
        lambda: clientes.append(Cliente("C03", "Andrés Gómez", "andres@example.com", "3101234567")) or clientes[-1])
    ejecutar_prueba(4, "Describir servicios con polimorfismo",
        lambda: "\\n".join(s.describir() for s in (sala, equipo, asesoria)))
    ejecutar_prueba(5, "Calcular costo con descuento e impuesto",
        lambda: "Costo final: {}".format(sala.calcular_costo(2, descuento=10, impuesto=19)))
    ejecutar_prueba(6, "Rechazar cantidad cero",
        lambda: equipo.calcular_costo(0))
    ejecutar_prueba(7, "Crear y confirmar reserva",
        lambda: (lambda r: (r.confirmar(), str(r))[1])(Reserva("R01", clientes[0], sala, 2)))
    ejecutar_prueba(8, "Rechazar reserva con cantidad negativa",
        lambda: Reserva("R02", clientes[0], equipo, -1))
    ejecutar_prueba(9, "Rechazar servicio no disponible",
        lambda: Reserva("R03", clientes[1], Asesoria("S04", "Asesoría temporal", 60000, False), 1))
    ejecutar_prueba(10, "Cancelar reserva",
        lambda: (lambda r: (r.cancelar(), str(r))[1])(Reserva("R04", clientes[1], asesoria, 1)))

    print("\\nDemostración finalizada. Revise logs/sistema.log.")

if __name__ == "__main__":
    main()
