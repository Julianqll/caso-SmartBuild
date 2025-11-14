from app.services import estimar_tiempo_preparacion, registrar_reserva


def test_estimacion_para_0_platos():
    assert estimar_tiempo_preparacion(0) == 0


def test_estimacion_para_3_platos():
    assert estimar_tiempo_preparacion(3) == 15


def test_estimacion_para_5_platos():
    assert estimar_tiempo_preparacion(5) == 25


def test_registrar_reserva_devuelve_diccionario():
    reserva = registrar_reserva("Juan", 5, "20:00")
    assert reserva["cliente"] == "Juan"
    assert reserva["mesa"] == 5
    assert "registrado_en" in reserva
