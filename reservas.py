"""Gestión del ciclo de vida de las reservas."""
from enum import Enum
from excepciones import ReservaInvalidaError

class EstadoReserva(Enum):
    """Estados posibles de una reserva."""
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"

class Reserva:
    """Relaciona un cliente con un servicio y controla su estado."""

    def __init__(self, codigo, cliente, servicio, cantidad):
        if not codigo or cliente is None or servicio is None:
            raise ReservaInvalidaError("Código, cliente y servicio son obligatorios.")
        if not isinstance(cantidad, (int, float)) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ReservaInvalidaError("La cantidad debe ser un número positivo.")

        # Se valida el tipo de unidad que exige el servicio concreto.
        servicio.validar_parametros(cantidad)
        servicio.validar_disponibilidad()

        self.codigo = str(codigo)
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = EstadoReserva.PENDIENTE
        self.costo = servicio.calcular_costo(cantidad)

    def confirmar(self):
        """Confirma únicamente las reservas que siguen pendientes."""
        if self.estado is not EstadoReserva.PENDIENTE:
            raise ReservaInvalidaError("Solo se pueden confirmar reservas pendientes.")
        self.estado = EstadoReserva.CONFIRMADA
        return self.estado.value

    def cancelar(self):
        """Cancela una reserva que todavía no haya sido cancelada."""
        if self.estado is EstadoReserva.CANCELADA:
            raise ReservaInvalidaError("La reserva ya está cancelada.")
        self.estado = EstadoReserva.CANCELADA
        return self.estado.value

    def procesar(self):
        """Ejemplo de encadenamiento: conserva la causa del error original."""
        try:
            self.servicio.validar_disponibilidad()
            return self.confirmar()
        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible procesar la reserva.") from error

    def __str__(self):
        return "Reserva {} | {} | {} | {} | {}".format(
            self.codigo, self.cliente.nombre, self.servicio.nombre,
            self.estado.value, self.costo)
