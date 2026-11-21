"""Clase abstracta base para las entidades del sistema."""
from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError


class Entidad(ABC):
    """Representa una entidad que debe tener identificador y descripción."""

    def __init__(self, identificador):
        # Se evita crear entidades sin un identificador útil.
        if not identificador or not str(identificador).strip():
            raise DatoInvalidoError("El identificador es obligatorio.")
        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        """Permite consultar el identificador sin modificarlo directamente."""
        return self._identificador

    @abstractmethod
    def describir(self):
        """Cada entidad concreta define su propia descripción."""
        raise NotImplementedError
