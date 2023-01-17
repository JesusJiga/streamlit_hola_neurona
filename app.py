import streamlit as st

def CalcNeuronas(entrada, pesos, sesgo):
  if(len(entrada) == len(pesos)):
    i = y = 0
    for x in entrada:
      y = y + x * pesos[i]
      i = i + 1
    return y + sesgo
  else:
    return None

st.title("Hola, Neurona!")
st.image('neurona.png', width= 200)

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Con sesgo"])

with tab1:
    st.header("Una entrada")
    wtab1 = st.slider('Selecciona un peso', -100.0, 100.0, 0.0)
    xtab1 = st.number_input('Elija una entrada')
    if st.button("Calcula la neurona"):
        ytab1 = xtab1 * wtab1
        st.write("La salida es: ", ytab1)

with tab2:
    st.header("Dos entradas")
    col21, col22 = st.columns(2)
    with col21:
        w0 = st.slider('Selecciona el peso w0', -100.0, 100.0, 0.0)
        x0 = st.number_input('Elija la entrada x0')
    with col22:
        w1 = st.slider('Selecciona el peso w1', -100.0, 100.0, 0.0)
        x1 = st.number_input('Elija la entrada x1')
    if st.button("Calcula las dos neuronas"):
        ytab2 = x0 * w0 + x1 * w1
        st.write("La salida es: ", ytab2)

with tab3:
    i = 0
    if 'w' not in st.session_state:
        st.session_state['w'] = []
    if 'x' not in st.session_state:
        st.session_state['x'] = []
    if 'i' not in st.session_state:
        st.session_state['i'] = 0

    st.header("Con sesgo")
    st.text(f"Selecciona el peso {st.session_state['i']}")
    w = st.slider("slider_peso", -100.0, 100.0, 0.0, label_visibility='collapsed', key="slider_tab3")
    x = st.number_input('Elija una entrada para el peso', key="number_tab3")
    if st.button("Añade entrada"):
        st.session_state['i'] += 1
        st.session_state['w'].append(w)
        st.session_state['x'].append(x)
    if len(st.session_state['w']) > 0:
        st.text("Los pesos añadidos son: ")
        s = ""
        for j in range (len(st.session_state['w'])):
            s = s + str(st.session_state['w'][j]) + " "
        st.text(s)
    if len(st.session_state['x']) > 0:
        st.text("Las entradas añadidas son: ")
        s = ""
        for j in range (len(st.session_state['x'])):
            s = s + str(st.session_state['x'][j]) + " "
        st.text(s)
    b = st.number_input('Seleccione el sesgo')
    if st.button("Calcular"):
        ytab3 = CalcNeuronas(st.session_state['x'],st.session_state['w'],b)
        st.write("La salida es: ", ytab3)