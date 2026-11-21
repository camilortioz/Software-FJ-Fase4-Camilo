class ErrorSistema(Exception):
    """Error base controlado por la aplicación."""

class DatoInvalidoError(ErrorSistema):
    """Dato que no cumple las validaciones."""

class ServicioNoDisponibleError(ErrorSistema):
    """Servicio temporalmente no disponible."""

class ReservaInvalidaError(ErrorSistema):
    """Operación de reserva no permitida."""
