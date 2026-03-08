import streamlit as st
from views.derivada_view import renderizar_tela_derivada

st.set_page_config(page_title="Métodos Numéricos II", layout="centered")


if "expressao_usuario" not in st.session_state:
    st.session_state.expressao_usuario = "x^2"
if "tela_atual" not in st.session_state:
    st.session_state.tela_atual = "menu"

def mudar_tela(nova_tela):
    st.session_state.tela_atual = nova_tela


if st.session_state.tela_atual == "menu":
    st.title("Métodos Numéricos II")
    st.markdown("Selecione o método que deseja utilizar")
    st.divider()

    if st.button("Derivação Numérica", use_container_width=True):
        mudar_tela("Derivada")
        st.rerun()

    st.button("Integração Numérica (Em breve)", use_container_width=True, disabled=True)
    st.button("Resolução de EDOs (Em breve)", use_container_width=True, disabled=True)

elif st.session_state.tela_atual == "Derivada":
    renderizar_tela_derivada(mudar_tela)