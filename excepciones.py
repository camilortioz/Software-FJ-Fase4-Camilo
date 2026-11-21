"""Excepciones personalizadas del sistema Software FJ."""

class ErrorSistema(Exception):
    """Clase base para los errores controlados de la aplicación."""

class DatoInvalidoError(ErrorSistema):
    """Se genera cuando un dato no cumple las validaciones."""

class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""

class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una operación de reserva no es válida."""
