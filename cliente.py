"""Clase Cliente: datos encapsulados y validados."""
import re
from entidad import Entidad
from excepciones import DatoInvalidoError

class Cliente(Entidad):
    """Almacena la información básica de un cliente."""

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatoInvalidoError("El nombre debe tener al menos dos caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        patron = r"[^@\s]+@[^@\s]+\.[^@\s]+"
        if not isinstance(valor, str) or not re.fullmatch(patron, valor.strip()):
            raise DatoInvalidoError("El correo electrónico no tiene un formato válido.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        digitos = re.sub(r"\D", "", str(valor))
        if not 7 <= len(digitos) <= 15:
            raise DatoInvalidoError("El teléfono debe tener entre 7 y 15 dígitos.")
        self._telefono = digitos

    def describir(self):
        return "Cliente {}: {} ({})".format(
            self.identificador, self.nombre, self.correo)

    def __str__(self):
        return self.describir()
