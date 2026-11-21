from enum import Enum
from excepciones import ReservaInvalidaError

class EstadoReserva(Enum):
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"

class Reserva:
    def __init__(self, codigo, cliente, servicio, cantidad):
        if not codigo or cliente is None or servicio is None:
            raise ReservaInvalidaError("Código, cliente y servicio son obligatorios.")
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ReservaInvalidaError("La cantidad debe ser positiva.")
        servicio.validar_disponibilidad()
        self.codigo, self.cliente, self.servicio = str(codigo), cliente, servicio
        self.cantidad = cantidad
        self.estado = EstadoReserva.PENDIENTE
        self.costo = servicio.calcular_costo(cantidad)

    def confirmar(self):
        if self.estado is not EstadoReserva.PENDIENTE:
            raise ReservaInvalidaError("Solo se confirman reservas pendientes.")
        self.estado = EstadoReserva.CONFIRMADA
        return self.estado.value

    def cancelar(self):
        if self.estado is EstadoReserva.CANCELADA:
            raise ReservaInvalidaError("La reserva ya está cancelada.")
        self.estado = EstadoReserva.CANCELADA
        return self.estado.value

    def procesar(self):
        try:
            self.servicio.validar_disponibilidad()
            return self.confirmar()
        except Exception as error:
            raise ReservaInvalidaError("No fue posible procesar la reserva.") from error

    def __str__(self):
        return "Reserva {} | {} | {} | {} | {}".format(
            self.codigo, self.cliente.nombre, self.servicio.nombre,
            self.estado.value, self.costo)
