import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def adicionar_ao_input(texto):
    st.session_state.expressao_usuario += texto

def limpar_input():
    st.session_state.expressao_usuario = ""

def renderizar_teclado():
    with st.expander("⌨️ Teclado Matemático"):
        # Linha 1: Operadores Básicos
        c1, c2, c3, c4 = st.columns(4)
        c1.button("x", on_click=adicionar_ao_input, args=("x",), use_container_width=True)
        c2.button("^", on_click=adicionar_ao_input, args=("^",), use_container_width=True)
        c3.button("(", on_click=adicionar_ao_input, args=("(",), use_container_width=True)
        c4.button(")", on_click=adicionar_ao_input, args=(")",), use_container_width=True)

        # Linha 2: Funções (Textos menores para caber)
        c5, c6, c7, c8 = st.columns(4)
        c5.button("sin", on_click=adicionar_ao_input, args=("sen(",), use_container_width=True)
        c6.button("cos", on_click=adicionar_ao_input, args=("cos(",), use_container_width=True)
        c7.button("tan", on_click=adicionar_ao_input, args=("tan(",), use_container_width=True)
        c8.button("√", on_click=adicionar_ao_input, args=("sqrt(",), use_container_width=True)

        # Linha 3: Outros
        c9, c10, c11, c12 = st.columns(4)
        c9.button("log", on_click=adicionar_ao_input, args=("log(",), use_container_width=True)
        c10.button("exp", on_click=adicionar_ao_input, args=("exp(",), use_container_width=True)
        c11.button("π", on_click=adicionar_ao_input, args=("π",), use_container_width=True)
        c12.button("AC", on_click=limpar_input, type="primary", use_container_width=True)


class VisualizadorGrafico:
    @staticmethod
    def renderizar_derivada(funcao_traduzida, x_alvo):
        st.divider()
        st.subheader(" Visualização Gráfica ")

        try:
            funcao_np = funcao_traduzida.replace("math.","np.")
            x_vals = np.linspace(x_alvo - 2, x_alvo + 2,400)
            y_vals = eval(funcao_np, {"np": np, "x": x_vals})
            y_ponto = eval(funcao_np, {"np": np, "x": x_alvo})
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, label=f"f(x)", color="#1f77b4", linewidth=2)
            ax.scatter([x_alvo], [y_ponto], color='red', zorder=5, label=f"Ponto x={x_alvo}")

            ax.set_title("Comportamento da Função")
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            ax.axhline(0, color='black',linewidth=0.5)
            ax.axvline(0, color='black',linewidth=0.5)
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.legend()

            st.pyplot(fig)
        except Exception as e:
            st.warning(f"Não foi possível gerar o gráfico para esta expressão: {e}")
