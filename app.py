import streamlit as st
import pandas as pd
import time
import folium
from streamlit_folium import st_folium

# Configuração oficial da página em modo estendido para o mapa ficar gigante
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
    if st.button("🛞 INICIAR NAVEGAÇÃO EM TEMPO REAL"):
        with st.spinner("Conectando ao satélite e traçando rota padrão Google Maps..."):
            time.sleep(1.5)
        st.session_state.tela_atual = "mapa"
        st.rerun()

# --- TELA 2: INTERFACE ESTILO GOOGLE MAPS ---
elif st.session_state.tela_atual == "mapa":
    
    # Painel superior verde de navegação clássico do Google Maps
    st.success("🟢 BR-116 - Rodovia Régis Bittencourt | Rota de Carga Pesada Liberada | Siga em frente por 120 km")
    
    # Divisão de tela: Esquerda Mapa Gigante / Direita Controles do Motorista
    col_mapa, col_painel = st.columns([2, 1])
    
    with col_mapa:
        st.markdown("### 🗺️ Linha de Rota e Trajeto Ativo (Google Maps Style)")
        
        # Criando o mapa real centralizado na rodovia entre Curitiba e SP
        m = folium.Map(location=[-24.5000, -48.5000], zoom_start=8, tiles="OpenStreetMap")
        
        # Coordenadas que traçam a linha azul do caminho a seguir na estrada
        coordenadas_linha = [
            [-25.4284, -49.2733], # Curitiba
            [-24.7123, -47.8542], # Registro
            [-24.5200, -47.7500], # Ponto do Radar
            [-23.5505, -46.6333]  # São Paulo
        ]
        
        # Desenha a linha azul clássica do Google Maps indicando o caminho
        folium.PolyLine(coordenadas_linha, color="blue", weight=6, opacity=0.8, tooltip="Rota Principal EIXO'S").add_to(m)
        
        # Adiciona marcadores interativos com alertas na rodovia
        folium.Marker([-25.4284, -49.2733], popup="Origem: Curitiba", icon=folium.Icon(color="green", icon="play")).add_to(m)
        folium.Marker([-24.5200, -47.7500], popup="⚠️ ALERTA: Radar de Velocidade 80km/h", icon=folium.Icon(color="red", icon="flash")).add_to(m)
        folium.Marker([-24.7123, -47.8542], popup="⛽ Posto Graal: Benefício VIP Disponível!", icon=folium.Icon(color="orange", icon="star")).add_to(m)
        folium.Marker([-23.5505, -46.6333], popup="Destino: São Paulo", icon=folium.Icon(color="blue", icon="flag")).add_to(m)
        
        # Renderiza o mapa interativo na tela
        st_folium(m, width=700, height=450)
        
        # Painel inferior de telemetria do motorista
        st.metric(label="Velocímetro Digital", value="80 km/h", delta="Velocidade Ideal para o Trecho", delta_color="normal")
        
    with col_painel:
        st.markdown("### 🎙️ Painel de Controle e Voz")
        st.info("📻 CANAL ATIVO: BR-116 Trecho SP | 142 Colegas Online")
        
        if st.button("💬 'EIXO, BORRACHEIRO'"):
            st.warning("🔊 Copiloto: 'Borracharia do Gaúcho detectada no KM 440 da BR-116. Deseja traçar rota alternativa?'")
            
        if st.button("💬 'EIXO, AUXÍLIO MECÂNICO'"):
            st.warning("🔊 Copiloto: 'Mecânica Diesel Irmãos Silva a 12km de distância na pista da direita.'")
            
        st.markdown("---")
        
        # Central VIP e Cupons de Desconto de Parada
        if not st.session_state.vip_ativo:
            st.subheader("🛡️ MODO SEGURO VIP")
            st.write("Monitore roubo de carga e ganhe duchas grátis nas paradas do caminho para SP.")
            if st.button("⚡ ATIVAR VIP VIA PIX (R$ 49,99)"):
                st.session_state.vip_ativo = True
                st.success("Plano VIP ativo! Rádio PX e Cupons liberados!")
                time.sleep(1)
                st.rerun()
        else:
            st.success("🟩 MODO VIP ATIVO E PROTEGIDO")
            if st.button("🎫 VER MEU CUPOM DUCHA GRÁTIS"):
                st.session_state.tela_atual = "cupom"
                st.rerun()
                
        if st.button("🔙 Encerrar Viagem / Menu"):
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