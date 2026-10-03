import streamlit as st
import time

# Configuração da página oficial
st.set_page_config(page_title="EIXO'S GPS - Oficial", page_icon="🛞", layout="centered")

# Força o fundo amarelo tráfego e texto preto oficial do EIXO'S em qualquer celular ou PC
st.html("""
    <style>
    .stApp {
        background-color: #FFCC00 !important;
        color: #000000 !important;
    }
    h1, h2, h3, p, span, label, li, div, select, input {
        color: #000000 !important;
        font-family: 'Arial Black', sans-serif !important;
    }
    .stButton>button {
        background-color: #000000 !important;
        color: #FFCC00 !important;
        border-radius: 10px !important;
        border: 2px solid #000000 !important;
        font-weight: bold !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    div[data-baseweb="input"] > input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    </style>
""")

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

# --- TELA 2: INTERFACE DO MAPA SIMULADO ---
elif st.session_state.tela_atual == "mapa":
    st.title("🗺️ Mapa de Rodagem Nacional")
    st.info("🚚 ROTA ATIVA: Rotas de Carga pesada calculadas para todo o Brasil.")
    
    st.markdown("### 🎙️ Comando de Voz Ativo (Simule sua fala):")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💬 'EIXO, BORRACHEIRO'"):
            st.warning("🔊 Copiloto: 'Borracharia do Gaúcho a 4km na BR-116. Atendimento Móvel Grátis pelo app. Deseja ligar?'")
                
    with col2:
        if st.button("💬 'EIXO, AUXÍLIO MECÂNICO'"):
            st.warning("🔊 Copiloto: 'Oficina Diesel Irmãos Silva a 12km. Socorro mecânico na pista cadastrado 100% Grátis.'")
            
    with col3:
        if st.button("💬 'EIXO, GERAR CUPOM'"):
            if st.session_state.vip_ativo:
                st.session_state.tela_atual = "cupom"
                st.rerun()
            else:
                st.error("❌ Comando bloqueado. Esta opção exige o Plano VIP.")

    st.markdown("---")
    
    if not st.session_state.vip_ativo:
        st.subheader("🛡️ CENTRAL DO MOTORISTA VIP")
        st.write("Monitore áreas de assalto, ative o Botão de Pânico por Voz e libere a Rádio PX Digital com os colegas da estrada.")
        st.write("• **Plano Mensal:** R$ 4,99/mês")
        st.write("• **Plano Anual:** R$ 49,99/ano (🔥 GANHE 2 MESES GRÁTIS)")
        
        if st.button("⚡ ATIVAR PLANO ANUAL VIA PIX (R$ 49,99)"):
            st.session_state.vip_ativo = True
            st.success("🔊 Copiloto: 'Parabéns, colega! Plano VIP ativo. Rádio PX e Botão de Pânico liberados!'")
            time.sleep(2)
            st.rerun()
    else:
        st.success("🟩 MODO VIP ATIVO: Você está protegido com o Botão de Pânico e Rádio PX Nacional.")
        if st.button("🎫 VER MEU CUPOM DE DESCONTO VIP (Posto Graal)"):
            st.session_state.tela_atual = "cupom"
            st.rerun()
            
    st.markdown("---")
    col_back, col_cad = st.columns(2)
    with col_back:
        if st.button("🔙 Editar Caminhão"):
            st.session_state.tela_atual = "config"
            st.rerun()
    with col_cad:
        if st.button("🛠️ Cadastrar Oficina/Borracharia"):
            st.session_state.tela_atual = "cadastro_parceiro"
            st.rerun()

# --- TELA 3: CADASTRO GRATUITO DE PARCEIROS DE ESTRADA ---
elif st.session_state.tela_atual == "cadastro_parceiro":
    st.title("🛠️ Portal do Parceiro de Estrada")
    st.subheader("Cadastre seu serviço de graça no maior mapa do Brasil")
    st.write("Consiga mais clientes e atenda caminhoneiros na rodovia. É 100% gratuito!")
    
    nome_oficina = st.text_input("Nome da Borracharia ou Oficina", "Ex: Borracharia do Gaúcho")
    whats_oficina = st.text_input("WhatsApp de Atendimento", "Ex: (11) 99999-9999")
    
    st.write("Selecione suas Especialidades:")
    st.checkbox("Borracharia / Pneus de Linha Pesada")
    st.checkbox("Mecânica Geral Diesel")
    st.checkbox("Auto Elétrico / Injeção Eletrônica")
    st.checkbox("Guincho Pesado / Reboque")
    
    st.write("Horário de Funcionamento:")
    st.radio("Disponibilidade", ["Atendimento 24 Horas", "Horário Comercial"])
    
    if st.button("📍 CAPTURAR MINHA LOCALIZAÇÃO ATUAL VIA GPS"):
        st.info("Coordenadas capturadas com sucesso! Seu ponto está fixado na rodovia.")
        
    if st.button("🔥 FICAR VISÍVEL NO MAPA NACIONAL AGORA"):
        st.success("🔊 Sistema: 'Cadastro concluído! Obrigado por ajudar a manter o Brasil rodando com segurança!'")
        time.sleep(2)
        st.session_state.tela_atual = "mapa"
        st.rerun()
        
    if st.button("🔙 Cancelar e Voltar"):
        st.session_state.tela_atual = "mapa"
        st.rerun()

# --- TELA 4: TELA DO CUPOM DE DESCONTO ---
elif st.session_state.tela_atual == "cupom":
    st.title("🎫 SEU CUPOM EXCLUSIVO EIXO'S VIP")
    st.subheader("Apresente o código no caixa do posto para receber o benefício")
    
    st.code("# EIXO-7729", language="text")
    st.write("**POSTO PARCEIRO:** REDE GRAAL - Rodovia Presidente Dutra KM 22")
    st.write("### ✅ BENEFÍCIOS VALIDADOS NO SEU PLANO:")
    st.write("- 🚿 Ducha Quente TOTALMENTE GRÁTIS")
    st.write("- ☕ 1 Café Expresso Cortesia da Casa")
    st.write("- 💰 R$ 0,10 de Desconto por Litro no Diesel S10")
    st.write("⏳ *Este cupom expira em 42 minutos. Aproveite o descanso, colega!*")
    
    if st.button("🗺️ VOLTAR PARA O MAPA"):
        st.session_state.tela_atual = "mapa"
        st.rerun()