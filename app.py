import streamlit as st
import pandas as pd
import time

# Configuração oficial da página
st.set_page_config(page_title="EIXO'S GPS - Oficial", page_icon="🛞", layout="wide")

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
    if st.button("🛞 INICIAR VIAGEM (MODO NAVEGAÇÃO W-TRUCK)"):
        with st.spinner("Iniciando GPS e traçando rota segura para veículos pesados..."):
            time.sleep(1.5)
        st.session_state.tela_atual = "mapa"
        st.rerun()

# --- TELA 2: INTERFACE DE NAVEGAÇÃO COMPATÍVEL COM WAZE ---
elif st.session_state.tela_atual == "mapa":
    
    # -------------------------------------------------------------
    # PAINEL SUPERIOR DO WAZE (Próxima Manobra)
    # -------------------------------------------------------------
    st.success("⬅️ EM 500 METRES: Mantenha-se à esquerda na bifurcação em direção a São Paulo (BR-116)")
    
    # Divisão de tela para simular o painel do motorista
    col_mapa, col_painel = st.columns([2, 1])
    
    with col_mapa:
        st.markdown("### 🗺️ Navegação GPS Ativa")
        
        # Coordenadas em tempo real simulando o trajeto na rodovia
        coordenadas_waze = pd.DataFrame({
            'latitude': [-25.4284, -25.3500, -25.2000, -25.1000],
            'longitude': [-49.2733, -49.1500, -48.9500, -48.8000]
        })
        
        # Renderiza o mapa ocupando a tela principal do motorista
        st.map(coordenadas_waze, zoom=10)
        
        # HUD Inferior do Waze (Velocímetro e Tempo)
        st.metric(label="Velocidade Atual (BR-116)", value="80 km/h", delta="Laranja: Radar a 1km", delta_color="inverse")
        
    with col_painel:
        st.markdown("### 🎙️ Copiloto EIXO'S")
        
        # Alertas baseados em voz comunitária
        st.info("📻 CANAL ATIVO: BR-116 Trecho SP | 142 Colegas Online")
        
        if st.button("💬 'EIXO, BORRACHEIRO'"):
            st.warning("🔊 Borracharia do Gaúcho detectada a 4km. Atendimento pesado.")
            
        if st.button("💬 'EIXO, AUXÍLIO MECÂNICO'"):
            st.warning("🔊 Oficina Diesel Irmãos Silva a 12km. Pista livre.")
            
        st.markdown("---")
        
        # Central VIP e Cupons de Desconto de Parada
        if not st.session_state.vip_ativo:
            st.markdown("#### 🛡️ MODO SEGURO VIP")
            st.write("Libere alertas de assalto e ganhe benefícios nas paradas.")
            if st.button("⚡ ATIVAR VIP VIA PIX (R$ 49,99)"):
                st.session_state.vip_ativo = True
                st.success("Plano VIP ativo! Recursos de segurança liberados.")
                time.sleep(1)
                st.rerun()
        else:
            st.success("🟩 MODO VIP PROTEGIDO")
            if st.button("🎫 PEGAR CUPOM DUCHA GRÁTIS"):
                st.session_state.tela_atual = "cupom"
                st.rerun()
                
        if st.button("🔙 Encerrar Viagem"):
            st.session_state.tela_atual = "config"
            st.rerun()

# --- TELA 3: TELA DO CUPOM DE DESCONTO ---
elif st.session_state.tela_atual == "cupom":
    st.title("🎫 SEU CUPOM EXCLUSIVO EIXO'S VIP")
    st.subheader("Apresente o código no caixa do posto em SP")
    
    st.code("# EIXO-SP116", language="text")
    st.write("**POSTO PARCEIRO:** REDE GRAAL - Rodovia Régis Bittencourt KM 440")
    st.write("### ✅ BENEFÍCIOS VALIDADOS NO SEU PLANO:")
    st.write("- 🚿 Ducha Quente TOTALMENTE GRÁTIS")
    st.write("- ☕ 1 Café Expresso Cortesia da Casa")
    st.write("- 💰 R$ 0,10 de Desconto por Litro no Diesel S10")
    
    if st.button("🗺️ VOLTAR PARA A NAVEGAÇÃO"):
        st.session_state.tela_atual = "mapa"
        st.rerun()