import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('EMPLEATRONIX')
st.write("Todos los datos sobre los empleados en una aplicación.")


empleados = pd.read_csv("csv/employees.csv")

st.write(empleados)

st.markdown("---")

x = empleados["full name"]
y = empleados["salary"]

col1,col2,col3 = st.columns(3)

with col1:
    color = st.color_picker("Elige un color para las barras", value="#3E82D2")

with col2:
	mostrar_nombres = st.toggle("Mostrar el nombre", value=True)

with col3:
    mostrar_sueldo = st.toggle("Mostrar sueldo en la barra", value=True)

fig, ax = plt.subplots(figsize=(15, 8))
bars = ax.barh(x, y, color=color)

if not mostrar_nombres:
	 plt.yticks([])

if mostrar_sueldo:
    ax.bar_label(bars, fmt='%d €', padding=3)
else:
    ax.bar_label(bars, labels=['']*len(bars))

plt.xticks(rotation=90)
st.pyplot(plt)



st.markdown("© Andrés García Domínguez - CPIFP Alan Turing")