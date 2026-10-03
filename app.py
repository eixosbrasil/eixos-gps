import streamlit as st
import pandas as pd
import time

# Configuração da página oficial
st.set_page_config(page_title="EIXO'S GPS - Oficial", page_icon="🛞", layout="centered")

# Inicialização segura dos estados do aplicativo
if 'vip_ativo' not in st.session_state:
    st.session_state.vip_ativo = False
if 'tela_atual' not in st.session_state:
    st.session_state.tela_atual = "config"

# --- TELA 1: CONFIGURAÇÃO DO BRUTO ---
if st.session_state.tela_atual == "config":
    st.title("🛞 EIXO'S GPS BRASIL")
    st.subheader("Configure o seu Bruto para rodar seguro")
    
    tipo_camiao = st.selectbox("Tipo de Caminhão", ["Toco (2 Eixos)", "Truck (3 Eixos)", "Carreta (5 Eixos)", "Bitrem (7 Eixos)", "Rodotrem (9 Eixos)"])
    eixos = st.number_input("Número de Eixos Totais", min_value=2, max_value=9, value=7)
    suspensos = st.checkbox("Viajando com eixos suspensos (Vazio)")
    altura = st.number_input("Altura Máxima da Carga (metros)", min_value=2.0, max_value=5.5, value=4.40, step=0.1)
    peso = st.number_input("Peso Total Bruto (PBT em Toneladas)", min_value=2, max_value=100, value=45)
    
    st.markdown("---")
    if st.button("🛞 SALVAR CONFIGURAÇÃO E IR PARA O MAPA"):
        with st.spinner("Calibrando rotas nacionais por eixos e altura..."):
            time.sleep(1.5)
        st.session_state.tela_atual = "mapa"
        st.rerun()

# --- TELA 2: INTERFACE DO MAPA REAL ---
elif st.session_state.tela_atual == "mapa":
    st.title("🗺️ Mapa de Rodagem em Tempo Real")
    st.info("🚚 ROTA ATIVA: Curitiba (PR) ➡️ São Paulo (SP) via BR-116 (Régis Bittencourt)")
    
    # -------------------------------------------------------------
    # MAPA REAL INTEGRADO (Plotando pontos reais na BR-116)
    # -------------------------------------------------------------
    st.markdown("### 🗺️ Rota Comercial Ativa e Pontos de Apoio:")
    
    # Coordenadas reais de pontos na rota Curitiba - SP para desenhar no mapa
    dados_mapa = pd.DataFrame({
        'latitude': [
            -25.4284,  # Origem: Curitiba
            -24.7123,  # Ponto de Apoio: Registro (BR-116)
            -24.5200,  # Balança Obrigatória Ativa
            -23.5505   # Destino: São Paulo
        ],
        'longitude': [
            -49.2733,  # Curitiba
            -47.8542,  # Registro
            -47.7500,  # Balança
            -46.6333   # São Paulo
        ]
    })
    
    # Desenha o mapa interativo na tela do celular/PC
    st.map(dados_mapa)
    st.caption("ℹ️ Dê zoom ou arraste o mapa acima para ver o trajeto real da BR-116.")
    
    # Simulação dos comandos de voz inteligentes
    st.markdown("### 🎙️ Comando de Voz Ativo (Simule sua fala):")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💬 'EIXO, BORRACHEIRO'"):
            st.warning("🔊 Copiloto: 'Borracharia do Gaúcho localizada no km 450 da BR-116 (Registro). Atendimento Móvel Grátis pelo app. Deseja ligar?'")
                
    with col2:
        if st.button("💬 'EIXO, AUXÍLIO MECÂNICO'"):
            st.warning("🔊 Copiloto: 'Oficina Diesel Irmãos Silva detectada próxima à praça de pedágio. Socorro mecânico grátis na pista.'")
            
    with col3:
        if st.button("💬 'EIXO, GERAR CUPOM'"):
            if st.session_state.vip_ativo:
                st.session_state.tela_atual = "cupom"
                st.rerun()
            else:
                st.error("❌ Comando bloqueado. Esta opção exige o Plano VIP.")

    st.markdown("---")
    
    # Espaço da Monetização VIP
    if not st.session_state.vip_ativo:
        st.subheader("🛡️ CENTRAL DO MOTORISTA VIP")
        st.write("Monitore áreas de assalto na Régis, ative o Botão de Pânico e libere a Rádio PX Digital com os colegas de SP.")
        st.write("• **Plano Mensal:** R$ 4,99/mês")
        st.write("• **Plano Anual:** R$ 49,99/ano (🔥 GANHE 2 MESES GRÁTIS)")
        
        if st.button("⚡ ATIVAR PLANO ANUAL VIA PIX (R$ 49,99)"):
            st.session_state.vip_ativo = True
            st.success("🔊 Copiloto: 'Parabéns, colega! Plano VIP ativo. Rádio PX e cupons liberados para o trecho de SP!'")
            time.sleep(1.5)
            st.rerun()
    else:
        st.success("🟩 MODO VIP ATIVO: Você está protegido no eixo Curitiba - SP.")
        if st.button("🎫 VER MEU CUPOM DE DESCONTO VIP (Posto Graal SP)"):
            st.session_state.tela_atual = "cupom"
            st.rerun()
            
    st.markdown("---")
    col_back, col_cad = st.columns(2)
    with col_back:
        if st.button("🔙 Editar Caminhão"):
            st.session_state.tela_atual = "config"
            st.rerun()
    with col_cad:
        if st.button("🛠️ Cadastrar Oficina"):
            st.session_state.tela_atual = "cadastro_parceiro"
            st.rerun()

# --- TELA 3: CADASTRO GRATUITO ---
elif st.session_state.tela_atual == "cadastro_parceiro":
    st.title("🛠️ Portal do Parceiro de Estrada")
    st.subheader("Cadastre seu serviço de graça no mapa da BR-116")
    
    nome_oficina = st.text_input("Nome da Borracharia ou Oficina", "Ex: Mecânica Diesel SP")
    whats_oficina = st.text_input("WhatsApp de Atendimento", "Ex: (11) 99999-9999")
    st.checkbox("Borracharia de Linha Pesada")
    st.checkbox("Mecânica Geral Diesel")
    
    if st.button("🔥 FICAR VISÍVEL NO MAPA NACIONAL AGORA"):
        st.success("🔊 Sistema: 'Cadastro concluído! Seu ponto de socorro já aparece na rota para SP!'")
        time.sleep(1.5)
        st.session_state.tela_atual = "mapa"
        st.rerun()
        
    if st.button("🔙 Cancelar e Voltar"):
        st.session_state.tela_atual = "mapa"
        st.rerun()

# --- TELA 4: TELA DO CUPOM DE DESCONTO ---
elif st.session_state.tela_atual == "cupom":
    st.title("🎫 SEU CUPOM EXCLUSIVO EIXO'S VIP")
    st.subheader("Apresente o código no caixa do posto em SP")
    
    st.code("# EIXO-SP116", language="text")
    st.write("**POSTO PARCEIRO:** REDE GRAAL - Rodovia Régis Bittencourt KM 440")
    st.write("### ✅ BENEFÍCIOS VALIDADOS NO SEU PLANO:")
    st.write("- 🚿 Ducha Quente TOTALMENTE GRÁTIS")
    st.write("- ☕ 1 Café Expresso Cortesia da Casa")
    st.write("- 💰 R$ 0,10 de Desconto por Litro no Diesel S10")
    st.write("⏳ *Este cupom expira em 42 minutos. Aproveite o descanso na chegada a SP, colega!*")
    
    if st.button("🗺️ VOLTAR PARA O MAPA"):
        st.session_state.tela_atual = "mapa"
        st.rerun()