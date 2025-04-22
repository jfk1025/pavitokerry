import streamlit as st

st.image("QUIMI4.jpg")

st.title("🔁 Calculadora de Gases: Ecuación Combinada")
st.write(r"La ecuación usada es: $\frac{P_i \cdot V_i}{T_i} = \frac{P_f \cdot V_f}{T_f}$")

variable = st.selectbox(
    "Selecciona la variable que deseas calcular:",
    ["Presión inicial (Pi)", "Volumen inicial (Vi)", "Temperatura inicial (Ti)",
     "Presión final (Pf)", "Volumen final (Vf)", "Temperatura final (Tf)"]
)

def safe_input(label):
    return st.number_input(label, min_value=0.01, format="%.4f")

if variable == "Presión inicial (Pi)":
    Vi = safe_input("Volumen inicial (L)")
    Ti = safe_input("Temperatura inicial (K)")
    Pf = safe_input("Presión final (atm)")
    Vf = safe_input("Volumen final (L)")
    Tf = safe_input("Temperatura final (K)")
    if st.button("Calcular Pi"):
        Pi = (Pf * Vf * Ti) / (Vi * Tf)
        st.success(f"Presión inicial = {Pi:.3f} atm")

elif variable == "Volumen inicial (Vi)":
    Pi = safe_input("Presión inicial (atm)")
    Ti = safe_input("Temperatura inicial (K)")
    Pf = safe_input("Presión final (atm)")
    Vf = safe_input("Volumen final (L)")
    Tf = safe_input("Temperatura final (K)")
    if st.button("Calcular Vi"):
        Vi = (Pf * Vf * Ti) / (Pi * Tf)
        st.success(f"Volumen inicial = {Vi:.3f} L")

elif variable == "Temperatura inicial (Ti)":
    Pi = safe_input("Presión inicial (atm)")
    Vi = safe_input("Volumen inicial (L)")
    Pf = safe_input("Presión final (atm)")
    Vf = safe_input("Volumen final (L)")
    Tf = safe_input("Temperatura final (K)")
    if st.button("Calcular Ti"):
        Ti = (Pi * Vi * Tf) / (Pf * Vf)
        st.success(f"Temperatura inicial = {Ti:.3f} K")

elif variable == "Presión final (Pf)":
    Pi = safe_input("Presión inicial (atm)")
    Vi = safe_input("Volumen inicial (L)")
    Ti = safe_input("Temperatura inicial (K)")
    Vf = safe_input("Volumen final (L)")
    Tf = safe_input("Temperatura final (K)")
    if st.button("Calcular Pf"):
        Pf = (Pi * Vi * Tf) / (Vf * Ti)
        st.success(f"Presión final = {Pf:.3f} atm")

elif variable == "Volumen final (Vf)":
    Pi = safe_input("Presión inicial (atm)")
    Vi = safe_input("Volumen inicial (L)")
    Ti = safe_input("Temperatura inicial (K)")
    Pf = safe_input("Presión final (atm)")
    Tf = safe_input("Temperatura final (K)")
    if st.button("Calcular Vf"):
        Vf = (Pi * Vi * Tf) / (Pf * Ti)
        st.success(f"Volumen final = {Vf:.3f} L")

elif variable == "Temperatura final (Tf)":
    Pi = safe_input("Presión inicial (atm)")
    Vi = safe_input("Volumen inicial (L)")
    Ti = safe_input("Temperatura inicial (K)")
    Pf = safe_input("Presión final (atm)")
    Vf = safe_input("Volumen final (L)")
    if st.button("Calcular Tf"):
        Tf = (Pf * Vf * Ti) / (Pi * Vi)
        st.success(f"Temperatura final = {Tf:.3f} K")
