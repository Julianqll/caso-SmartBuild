import sys
from pathlib import Path

import streamlit as st

# Garantiza que el paquete raíz esté en sys.path cuando se ejecuta con `streamlit run`.
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from app.services import estimar_tiempo_preparacion, registrar_reserva


def main():
    st.set_page_config(page_title="SmartBuild - Restaurante", page_icon="🍽", layout="centered")

    st.title("SmartBuild - Gestión de Reservas y Pedidos")
    st.write("Aplicación web para el restaurante con soporte de IA (prototipo).")

    st.sidebar.header("Panel")
    opcion = st.sidebar.radio("Selecciona una opción:", ["Reservas", "Pedidos"])

    if opcion == "Reservas":
        st.subheader("Registrar reserva")

        nombre = st.text_input("Nombre del cliente")
        mesa = st.number_input("Número de mesa", min_value=1, max_value=50, value=1)
        hora = st.time_input("Hora de la reserva")

        if st.button("Guardar reserva"):
            reserva = registrar_reserva(nombre, mesa, hora.strftime("%H:%M"))
            st.success(f"Reserva registrada para {reserva['cliente']} en la mesa {reserva['mesa']} a las {reserva['hora']}")

    if opcion == "Pedidos":
        st.subheader("Estimar tiempo de preparación")

        num_platos = st.number_input("Número de platos en el pedido", min_value=0, max_value=20, value=2)
        if st.button("Calcular tiempo estimado"):
            tiempo = estimar_tiempo_preparacion(num_platos)
            st.info(f"Tiempo estimado de preparación: {tiempo} minutos")


if __name__ == "__main__":
    main()
