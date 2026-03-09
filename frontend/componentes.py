import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def adicionar_ao_input(texto):
    st.session_state.expressao_usuario += texto

def limpar_input():
    st.session_state.expressao_usuario = ""

def renderizar_teclado():
    with st.expander("⌨️ Mostrar Teclado Matemático"):
        c1, c2, c3, c4 = st.columns(4)
        c1.button(" e ", on_click=adicionar_ao_input, args=("e",), width="stretch")
        c2.button("x²", on_click=adicionar_ao_input, args=("x^2",), width="stretch")
        c3.button("xⁿ", on_click=adicionar_ao_input, args=("x^",), width="stretch")
        c4.button("√x", on_click=adicionar_ao_input, args=("sqrt(x)",), width="stretch")

        c5, c6, c7, c8 = st.columns(4)
        c5.button("sen(x)", on_click=adicionar_ao_input, args=("sen(x)",), width="stretch")
        c6.button("cos(x)", on_click=adicionar_ao_input, args=("cos(x)",), width="stretch")
        c7.button("tan(x)", on_click=adicionar_ao_input, args=("tan(x)",), width="stretch")
        c8.button("log(x)", on_click=adicionar_ao_input, args=("log(x)",), width="stretch")

        c9, c10, c11, c12 = st.columns(4)
        c9.button(" ( ", on_click=adicionar_ao_input, args=("(",), width="stretch")
        c10.button(" ) ", on_click=adicionar_ao_input, args=(")",), width="stretch")
        c11.button(" + ", on_click=adicionar_ao_input, args=("+",), width="stretch")
        c12.button(" - ", on_click=adicionar_ao_input, args=("-",), width="stretch")

        # Linha 4: Operadores e Exponencial
        c13, c14, c15, c16 = st.columns(4)
        c13.button(" * ", on_click=adicionar_ao_input, args=("*",), width="stretch")
        c14.button(" / ", on_click=adicionar_ao_input, args=("/",), width="stretch")
        c15.button("eˣ", on_click=adicionar_ao_input, args=("exp(x)",), width="stretch")
        c16.button(" . ", on_click=adicionar_ao_input, args=(".",), width="stretch")


class VisualizadorGrafico:
    @staticmethod
    def renderizar_derivada(funcao_traduzida, x_alvo):
        st.divider()
        st.subheader(" Visualização Gráfica ")

        try:
            funcao_np = funcao_traduzida.replace("math.","np.")
            x_vals = np.linspace(x_alvo - 5, x_alvo + 5,400)
            y_vals = eval(funcao_np, {"np": np, "x": x_vals})
            y_ponto = eval(funcao_np, {"np": np, "x": x_alvo})
            fig, ax = plt.subplots(figsize=(6, 3.5))
            ax.plot(x_vals, y_vals, label=f"f(x)", color="#1f77b4", linewidth=2)
            ax.scatter([x_alvo], [y_ponto], color='red', zorder=5, label=f"Ponto x={x_alvo}")

            ax.set_title("Comportamento da Função")
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            ax.axhline(0, color='black',linewidth=0.5)
            ax.axvline(0, color='black',linewidth=0.5)
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.legend()

            st.pyplot(fig,width="content")
        except Exception as e:
            st.warning(f"Não foi possível gerar o gráfico para esta expressão: {e}")
