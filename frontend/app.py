import streamlit as st
import requests
import re

st.set_page_config(page_title="Métodos Numéricos II",layout="centered")

def traduzir_para_python(expressao: str) -> str:
    expr = expressao.replace(" ", "")
    expr = expr.replace("^","**")
    expr = expr.replace("π", "math.pi")
    expr = expr.replace("pi", "math.pi")
    expr = re.sub(r'(?<![a-zA-Z])e(?![a-zA-Z])', 'math.e', expr)
    
    funcoes_math = {
        "sen": "math.sin",
        "sin": "math.sin",
        "cos": "math.cos",
        "tan": "math.tan",
        "sqrt": "math.sqrt",
        "log": "math.log",
        "exp": "math.exp"
    }

    for humano, python in funcoes_math.items():
        expr = expr.replace(humano, python)

    expr = expr.replace("math.math.", "math.")
    
    return expr

if "expressao_usuario" not in st.session_state:
    st.session_state.expressao_usuario = "x^2"

if "tela_atual" not in st.session_state:
    st.session_state.tela_atual = "menu"

def adicionar_ao_input(texto):
    st.session_state.expressao_usuario += texto

def limpar_input():
    st.session_state.expressao_usuario = ""

def mudar_tela(nova_tela):
    st.session_state.tela_atual = nova_tela

#Tela principal
if st.session_state.tela_atual == "menu":
    st.title("Métodos Numéricos II")
    st.markdown("Selecione o método que deseja atilizar")
    st.divider()

    if st.button("Derivação Numérica", use_container_width=True):
        mudar_tela("Derivada")
        st.rerun()

    st.button("Integração Numérica (Em breve)",use_container_width=True,disabled=True)
    st.button("Resolução de EDOs (Em breve)",use_container_width=True,disabled=True)

#tela de derivada
elif st.session_state.tela_atual == "Derivada":
    if st.button("Voltar ao Menu Principal"):
        mudar_tela("menu")
        st.rerun()
    
    st.title("Derivação Numerica")
    st.markdown("Calcule a derivadas usando diferenças finitas.")
    st.divider()

    #inputs do user
    st.subheader("Parâmetros da função")
    funcao_input_humano = st.text_input("Digite a função f(x):", key="expressao_usuario")
    
    with st.expander("⌨️ Mostrar Teclado Matemático"):
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        c1.button("x²", use_container_width=True, on_click=adicionar_ao_input, args=("x^2",))
        c2.button("xⁿ", use_container_width=True, on_click=adicionar_ao_input, args=("x^",))
        c3.button("√x", use_container_width=True, on_click=adicionar_ao_input, args=("sqrt(x)",))
        c4.button("π", use_container_width=True, on_click=adicionar_ao_input, args=("π",))
        c5.button("e", use_container_width=True, on_click=adicionar_ao_input, args=("e",))
        c6.button("( )", use_container_width=True, on_click=adicionar_ao_input, args=("(x)",))
        
        c7, c8, c9, c10, c11, c12 = st.columns(6)
        c7.button("sen", use_container_width=True, on_click=adicionar_ao_input, args=("sen(x)",))
        c8.button("cos", use_container_width=True, on_click=adicionar_ao_input, args=("cos(x)",))
        c9.button("tan", use_container_width=True, on_click=adicionar_ao_input, args=("tan(x)",))
        c10.button("log", use_container_width=True, on_click=adicionar_ao_input, args=("log(x)",))
        c11.button("eˣ", use_container_width=True, on_click=adicionar_ao_input, args=("exp(x)",))
        c12.button("Limpar", type="primary", use_container_width=True, on_click=limpar_input)
        
        c13, c14, c15, c16, c17, c18 = st.columns(6)
        c13.button(" + ", use_container_width=True, on_click=adicionar_ao_input, args=("+",))
        c14.button(" - ", use_container_width=True, on_click=adicionar_ao_input, args=("-",))
        c15.button(" * ", use_container_width=True, on_click=adicionar_ao_input, args=("*",))
        c16.button(" / ", use_container_width=True, on_click=adicionar_ao_input, args=("/",))
        c17.button(" ( ", use_container_width=True, on_click=adicionar_ao_input, args=("(",))
        c18.button(" ) ", use_container_width=True, on_click=adicionar_ao_input, args=(")",))
    
    funcao_traduzida = traduzir_para_python(funcao_input_humano)

    col1, col2 = st.columns(2)
    with col1:
        x_input = st.number_input("Ponto x:", value=2.0, step=0.1)
        ordem_input = st.selectbox("Ordem da Derivada:", [1,2,3])
    with col2:
        deltaX_input = st.number_input(" deltaX:", value=0.1, format="%.4f", step=0.01)
        metodo_input = st.selectbox("Método:",["central","forward","backward"])
    
    if ordem_input == 1:
        st.markdown("---")
        st.markdown("**Fórmula Utilizada:**")
        if metodo_input == "forward":
            st.markdown(r"$$f'(x) \approx \frac{f(x + \Delta x) - f(x)}{\Delta x}$$")
        if metodo_input == "backward":
            st.markdown(r"$$f'(x) \approx \frac{f(x) - f(x - \Delta x)}{\Delta x}$$")
        if metodo_input == "central":
            st.markdown(r"$$f'(x) \approx \frac{f(x + \Delta x) - f(x - \Delta x)}{2 \Delta x}$$")

    elif ordem_input == 2:
        st.markdown("---")
        st.markdown("**Fórmula Utilizada**")
        if metodo_input == "forward":
            st.markdown(r"$$f''(x) \approx \frac{f(x + 2\Delta x) - 2f(x + \Delta x) + f(x)}{(\Delta x)^2}$$")
        if metodo_input == "backward":
            st.markdown(r"$$f''(x) \approx \frac{f(x) - 2f(x - \Delta x) + f(x - 2\Delta x)}{(\Delta x)^2}$$")
        if metodo_input == "central":
            st.markdown(r"$$f''(x) \approx \frac{f(x + \Delta x) - 2f(x) + f(x - \Delta x)}{(\Delta x)^2}$$")
    
    elif ordem_input == 3:
        st.markdown("---")
        st.markdown("**Fórmula Utilizada**")
        if metodo_input == "forward":
            st.markdown(r"$$f'''(x) \approx \frac{f(x + 3\Delta x) - 3f(x + 2\Delta x) + 3f(x + \Delta x) - f(x)}{(\Delta x)^3}$$")
        if metodo_input == "backward":
            st.markdown(r"$$f'''(x) \approx \frac{f(x) - 3f(x - \Delta x) + 3f(x - 2\Delta x) - f(x - 3\Delta x)}{(\Delta x)^3}$$")
        if metodo_input == "central":
            st.markdown(r"$$f'''(x) \approx \frac{f(x + 2\Delta x) - 2f(x + \Delta x) + 2f(x - \Delta x) - f(x - 2\Delta x)}{2(\Delta x)^3}$$")


    if st.button("Calcular", type="primary"):
        payload = {
            "funcao" : funcao_traduzida,
            "x" : x_input,
            "deltaX" : deltaX_input, 
            "metodo" : metodo_input,
            "ordem" : ordem_input
        }

        with st.spinner("Calculando..."):
            try:
                resposta = requests.post("http://127.0.0.1:8000/derivar", json=payload)

                if resposta.status_code == 200:
                    dados = resposta.json()
                    st.success("Cálculo realizado com sucesso!")
                    st.metric(label=f"Resultado ({metodo_input})", value=f"{dados['resultado']:.6f}")
                else:
                    erro = resposta.json().get('detail', 'Erro desconhecido')
                    st.error(f"Erro na API: {erro}")
            except requests.exceptions.ConnectionError:
                st.error("Não foi possível conectar à API. O FastAPI está rodando?")