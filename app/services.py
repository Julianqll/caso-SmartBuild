import os
from datetime import datetime


# MALA PRÁCTICA INTENCIONAL (para que Sonar la detecte primero)
DB_PASSWORD = "SuperSecreta123"  # luego lo cambiaremos a variable de entorno


def estimar_tiempo_preparacion(num_platos: int) -> int:
    """
    Devuelve el tiempo estimado de preparación (minutos) según la cantidad de platos.
    Sirve para pruebas unitarias y para la lógica de negocio.
    """
    if num_platos <= 0:
        return 0
    if num_platos <= 3:
        return 15
    if num_platos <= 6:
        return 25
    return 40


def registrar_reserva(nombre: str, mesa: int, hora: str) -> dict:
    """
    Simula el registro de una reserva y devuelve un diccionario con los datos.
    """
    return {
        "cliente": nombre,
        "mesa": mesa,
        "hora": hora,
        "registrado_en": datetime.utcnow().isoformat()
    }


def obtener_password_segura() -> str:
    """
    Versión correcta: luego usaremos esta función en vez del hardcode.
    """
    return os.getenv("DB_PASSWORD", "")
