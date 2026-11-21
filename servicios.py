from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError, ServicioNoDisponibleError

class Servicio(ABC):
    def __init__(self, codigo, nombre, tarifa, disponible=True):
        if not codigo or not nombre:
            raise DatoInvalidoError("Código y nombre son obligatorios.")
        if not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise DatoInvalidoError("La tarifa debe ser positiva.")
        self.codigo, self.nombre = str(codigo), str(nombre)
        self.tarifa, self.disponible = float(tarifa), bool(disponible)

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError("El servicio {} no está disponible.".format(self.nombre))

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        self.validar_disponibilidad()
        if cantidad <= 0 or not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatoInvalidoError("Cantidad, descuento o impuesto fuera de rango.")
        subtotal = self.tarifa * cantidad
        return round(subtotal * (1 - descuento / 100) * (1 + impuesto / 100), 2)

    @abstractmethod
    def describir(self):
        raise NotImplementedError

    @abstractmethod
    def validar_parametros(self, **kwargs):
        raise NotImplementedError

class ReservaSala(Servicio):
    def describir(self):
        return "Reserva de sala: {} ({} por hora)".format(self.nombre, self.tarifa)
    def validar_parametros(self, **kwargs):
        if kwargs.get("horas", 0) <= 0:
            raise DatoInvalidoError("Las horas deben ser mayores que cero.")

class AlquilerEquipo(Servicio):
    def describir(self):
        return "Alquiler de equipo: {} ({} por día)".format(self.nombre, self.tarifa)
    def validar_parametros(self, **kwargs):
        if kwargs.get("dias", 0) <= 0:
            raise DatoInvalidoError("Los días deben ser mayores que cero.")

class Asesoria(Servicio):
    def describir(self):
        return "Asesoría: {} ({} por sesión)".format(self.nombre, self.tarifa)
    def validar_parametros(self, **kwargs):
        if kwargs.get("sesiones", 0) <= 0:
            raise DatoInvalidoError("Las sesiones deben ser mayores que cero.")
