import streamlit as st
import requests
from utils import traduzir_para_python
from componentes import renderizar_teclado, VisualizadorGrafico

def renderizar_tela_derivada(mudar_tela):
    if st.button("Voltar ao Menu Principal"):
        mudar_tela("menu")
        st.rerun()
    
    st.title("Derivação Numérica")
    st.divider()

    # Divisão principal: Esquerda (Inputs) | Direita (Resultados)
    col_input, col_resultado = st.columns([1.1, 0.9], gap="large")

    with col_input:
        st.subheader("⌨️ Entrada")
        funcao_input_humano = st.text_input("Digite f(x):", key="expressao_usuario", placeholder="Ex: sen(x) + x^2")
        
        # Chamamos o teclado (ele vai se ajustar automaticamente ao espaço da coluna)
        renderizar_teclado() 
        
        funcao_traduzida = traduzir_para_python(funcao_input_humano)

        # Grid de parâmetros mais compacto
        c1, c2 = st.columns(2)
        with c1:
            x_input = st.number_input("Ponto x:", value=2.0, step=0.1)
            ordem_input = st.selectbox("Ordem:", [1, 2, 3])
        with c2:
            deltaX_input = st.number_input("Δx:", value=0.1, format="%.4f", step=0.01)
            metodo_input = st.selectbox("Método:", ["central", "forward", "backward"])
        
        st.divider()
        btn_calcular = st.button("🚀 Calcular Derivada", type="primary", use_container_width=True)

    with col_resultado:
        st.subheader("📊 Resultado")
        
        # Box de fórmula e tradução
        with st.expander("🔍 Detalhes da Tradução", expanded=False):
            st.code(f"Python: {funcao_traduzida}")
            if ordem_input == 1:
                if metodo_input == "forward": st.latex(r"f'(x) \approx \frac{f(x + \Delta x) - f(x)}{\Delta x}")
                elif metodo_input == "backward": st.latex(r"f'(x) \approx \frac{f(x) - f(x - \Delta x)}{\Delta x}")
                elif metodo_input == "central": st.latex(r"f'(x) \approx \frac{f(x + \Delta x) - f(x - \Delta x)}{2 \Delta x}")
            # ... (as outras fórmulas seguem aqui com st.latex)

        if btn_calcular:
            payload = {"funcao": funcao_traduzida, "x": x_input, "deltaX": deltaX_input, "metodo": metodo_input, "ordem": ordem_input}
            with st.spinner("Processando..."):
                try:
                    resposta = requests.post("http://127.0.0.1:8000/derivar", json=payload)
                    if resposta.status_code == 200:
                        dados = resposta.json()
                        st.metric(label="Resultado Final", value=f"{dados['resultado']:.8f}")
                        
                        # Chama o gráfico modular
                        VisualizadorGrafico.renderizar_derivada(funcao_traduzida, x_input)
                    else:
                        st.error("Erro no cálculo da API")
                except Exception:
                    st.error("API Offline")
        else:
            st.info("Configure os parâmetros e clique em Calcular para ver o gráfico.")