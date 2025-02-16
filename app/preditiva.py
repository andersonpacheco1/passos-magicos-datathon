import streamlit as st
import pickle
import pandas as pd
from pathlib import Path
# from pycaret.classification import load_model
import joblib

# Caminho do modelo salvo
model_path = Path(__file__).parent.parent / "models/lr_pedra_classification.pkl"

@st.cache_resource
def load_prof_model():
    # return load_model(model_path.with_suffix(''))
    return joblib.load(model_path)

# Carregar o modelo
model = load_prof_model()

st.title("Simulador de Pedra de Alunos")

sim_prof, sim_schol = st.tabs(["Simulador do Professor", "Simulador do Aluno"])

with sim_prof:
    
    fases = {
        '1º ano': ('Alfa', 7), '2º ano': ('Alfa', 8),
        '3º ano': ('Fase 1', 8), '4º ano': ('Fase 1', 9),
        '5º ano': ('Fase 2', 10), '6º ano': ('Fase 2', 11),
        '7º ano': ('Fase 3', 12), '8º ano': ('Fase 3', 13),
        '9º ano': ('Fase 4', 14), '1º EM': ('Fase 5', 15),
        '2º EM': ('Fase 6', 16), '3º EM': ('Fase 7', 17)
    }
    
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_fase = st.selectbox("Selecione o Ano Escolar atual do aluno", list(fases.keys()))
    
    actual_fase, ideal_age = fases[selected_fase]

    with col2:
        actual_age = idade_aluno = st.number_input("Idade do Aluno", min_value=7, max_value=17, step=1)

    defasagem = ideal_age - actual_age

    if defasagem >= 0:
        IAN = 10.0
    elif defasagem >= -2:
        IAN = 5.0
    else:
        IAN = 2.5

    st.text('')

    col1, col2, col3 = st.columns(3)

    with col1:
        PORT = st.number_input("Português", min_value=0.0, max_value=10.0, value=None, format="%.1f")
        IAA = st.slider("IAA", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f")
        IPV = st.slider("IPV", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f")

    with col2:
        MAT = st.number_input("Matemática", min_value=0.0, max_value=10.0, value=None, format="%.1f")
        IEG = st.slider("IEG", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f")
        IPP = st.slider("IPP", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f")

    with col3:
        ING = st.number_input("Inglês", min_value=0.0, max_value=10.0, value=None, format="%.1f")
        IPS = st.slider("IPS", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f")

    IDA = pd.Series([PORT, MAT, ING]).mean(skipna=True)

    # Criar DataFrame com os inputs do usuário
    input_data = pd.DataFrame([[IAA, IAN, IDA, IEG, IPP, IPS, IPV]], 
                            columns=["IAA", "IAN", "IDA", "IEG", "IPP", "IPS", "IPV"])

    # Botão para previsão
    if st.button("Prever Pedra"):
        prediction = model.predict(input_data)
        st.write(f"### Predição: {int(prediction[0])}")
        st.write(IDA)
        st.write(IAN)