"""Clases de servicios: abstracción, herencia y polimorfismo."""
from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError, ServicioNoDisponibleError

class Servicio(ABC):
    """Clase abstracta que define el comportamiento común de un servicio."""

    def __init__(self, codigo, nombre, tarifa, disponible=True):
        if not codigo or not nombre:
            raise DatoInvalidoError("Código y nombre son obligatorios.")
        if not isinstance(tarifa, (int, float)) or isinstance(tarifa, bool) or tarifa <= 0:
            raise DatoInvalidoError("La tarifa debe ser un número positivo.")
        self.codigo = str(codigo)
        self.nombre = str(nombre)
        self.tarifa = float(tarifa)
        self.disponible = bool(disponible)

    def validar_disponibilidad(self):
        """Impide contratar servicios marcados como no disponibles."""
        if not self.disponible:
            raise ServicioNoDisponibleError(
                "El servicio {} no está disponible.".format(self.nombre))

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        """Calcula el costo; permite variar cantidad, descuento e impuesto."""
        self.validar_disponibilidad()
        if not isinstance(cantidad, (int, float)) or isinstance(cantidad, bool) or cantidad <= 0:
            raise DatoInvalidoError("La cantidad debe ser positiva.")
        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatoInvalidoError("Descuento e impuesto deben estar entre 0 y 100.")
        subtotal = self.tarifa * cantidad
        total = subtotal * (1 - descuento / 100) * (1 + impuesto / 100)
        return round(total, 2)

    @abstractmethod
    def describir(self):
        """Cada servicio concreto implementa su propia descripción."""
        raise NotImplementedError

    @abstractmethod
    def validar_parametros(self, cantidad):
        """Cada servicio valida su unidad de contratación."""
        raise NotImplementedError

class ReservaSala(Servicio):
    """Servicio de alquiler de salas por hora."""
    def describir(self):
        return "Reserva de sala: {} ({} por hora)".format(self.nombre, self.tarifa)

    def validar_parametros(self, cantidad):
        if cantidad <= 0:
            raise DatoInvalidoError("Las horas deben ser mayores que cero.")

class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos por día."""
    def describir(self):
        return "Alquiler de equipo: {} ({} por día)".format(self.nombre, self.tarifa)

    def validar_parametros(self, cantidad):
        if cantidad <= 0:
            raise DatoInvalidoError("Los días deben ser mayores que cero.")

class Asesoria(Servicio):
    """Servicio de asesoría por sesión."""
    def describir(self):
        return "Asesoría: {} ({} por sesión)".format(self.nombre, self.tarifa)

    def validar_parametros(self, cantidad):
        if cantidad <= 0:
            raise DatoInvalidoError("Las sesiones deben ser mayores que cero.")
