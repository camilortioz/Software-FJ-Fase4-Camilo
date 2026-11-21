from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, identificador):
        if not identificador or not str(identificador).strip():
            raise ValueError("El identificador es obligatorio.")
        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def describir(self):
        raise NotImplementedError
