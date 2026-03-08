import streamlit as st
import requests

st.set_page_config(page_title="Métodos Numéricos II",layout="centered")

if "tela_atual" not in st.session_state:
    st.session_state.tela_atual = "menu"

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
    funcao_input = st.text_input("Digite a função f(x)", value="x**2")

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



    if st.button("Calcular", type="primary"):
        payload = {
            "funcao" : funcao_input,
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