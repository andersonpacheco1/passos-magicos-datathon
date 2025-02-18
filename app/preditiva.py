import streamlit as st
import pickle
import pandas as pd
from pathlib import Path
import joblib

# Caminho do modelo salvo
prof_model_path = Path(__file__).parent.parent / "models/lr_pedra_classification.pkl"
schol_model_path = Path(__file__).parent.parent / "models/gbc_pedra_classification_scholar.pkl"

@st.cache_resource
def load_prof_model():
    return joblib.load(prof_model_path)

@st.cache_resource
def load_schol_model():
    return joblib.load(schol_model_path)

# Carregar o modelo
prof_model = load_prof_model()
schol_model = load_schol_model()

st.title("Simulador de Pedra de Alunos")

fases = {
        '1º ano': ('Alfa', 7), '2º ano': ('Alfa', 8),
        '3º ano': ('Fase 1', 8), '4º ano': ('Fase 1', 9),
        '5º ano': ('Fase 2', 10), '6º ano': ('Fase 2', 11),
        '7º ano': ('Fase 3', 12), '8º ano': ('Fase 3', 13),
        '9º ano': ('Fase 4', 14), '1º EM': ('Fase 5', 15),
        '2º EM': ('Fase 6', 16), '3º EM': ('Fase 7', 17)
    }

category_pedras = {
    0: 'Quartzo',
    1: 'Ágata',
    2: 'Ametista',
    3: 'Topázio'
}

sim_prof, sim_schol = st.tabs(["Simulador do Professor", "Simulador do Aluno"])

st.header("O que é o Simulador de Pedra?")
st.markdown("""
O Simulador de Pedra foi desenvolvido para auxiliar professores e alunos a compreenderem melhor o desempenho educacional com base nos indicadores dos relatório da PEDE PASSOS.

Ele permite que professores insiram os dados dos alunos para obter uma previsão da **Pedra Educacional**, uma categorização simbólica do nível de desenvolvimento educacional do estudante.

Já os alunos podem utilizar o simulador para entender sua posição em relação aos principais indicadores e identificar pontos de melhoria. Essa ferramenta busca fornecer insights que ajudem no aprimoramento do aprendizado e no suporte ao desenvolvimento acadêmico e pessoal.

O simulador foi separado por utilidade: **os professores têm acesso a todos os indicadores**, pois possuem uma visão mais completa do desempenho dos alunos, enquanto **os alunos têm acesso apenas parcialmente aos indicadores**, para que possam acompanhar seu progresso de forma objetiva.

📌 *Nota:* O melhor formato para os simuladores seria apresentar a avaliação dos indicadores no mesmo modelo da pesquisa original. Esse pode ser um ponto de melhoria futura para tornar a experiência mais intuitiva e alinhada ao processo de avaliação da Associação Passos Mágicos.
""")

st.header("Explicação dos Indicadores")
st.markdown("""
Os indicadores chaves da PEDE PASSOS são ferramentas de avaliação do desenvolvimento educacional dos estudantes da Associação Passos Mágicos. O **Índice de Desenvolvimento Educacional (INDE)** é o principal índice avaliativo, composto por três dimensões: acadêmica, psicossocial e psicopedagógica. Essas dimensões são medidas por sete indicadores:

* **IAN (Indicador de Adequação de Nível)**: Mede a adequação do nível acadêmico do estudante.
* **IDA (Indicador de Desempenho Acadêmico)**: Avalia o desempenho nas provas de Português, Matemática e Inglês.
* **IEG (Indicador de Engajamento)**: Expressa o engajamento nas atividades solicitadas, como lição de casa para estudantes das Fases 0 a 7, e ações de voluntariado para a Fase 8.
* **IAA (Indicador de Autoavaliação)**: Obtido por meio de um questionário sobre a avaliação do estudante sobre si mesmo e suas relações.
* **IPS (Indicador Psicossocial)**: Avaliação da equipe de psicólogas sobre o desenvolvimento do aluno nas interações familiares e emocionais.
* **IPP (Indicador Psicopedagógico)**: Avaliação da equipe de educadores e psicopedagogos sobre o desenvolvimento das aptidões do aluno.
* **IPV (Indicador do Ponto de Virada)**: Estágio em que o estudante demonstra, por meio de sua trajetória, a utilização da educação para transformar sua vida.

Os indicadores IAN, IDA, IEG e IAA são classificados como **indicadores de avaliação**, pois são construídos a partir de resultados obtidos diretamente dos estudantes. Os indicadores IPS, IPP e IPV são **indicadores de conselho**, formados por avaliações da equipe de professores, psicólogos e pedagogos.
""")

with sim_prof:
    
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
        PORT = st.number_input("Português", min_value=0.0, max_value=10.0, value=None, format="%.1f", key="prof_port")
        IAA = st.slider("IAA", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f", key="prof_iaa")
        IPV = st.slider("IPV", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f", key="prof_ipv")

    with col2:
        MAT = st.number_input("Matemática", min_value=0.0, max_value=10.0, value=None, format="%.1f", key="prof_mat")
        IEG = st.slider("IEG", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f", key="prof_ieg")
        IPP = st.slider("IPP", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f", key="prof_ipp")

    with col3:
        ING = st.number_input("Inglês", min_value=0.0, max_value=10.0, value=None, format="%.1f", key="prof_ing")
        IPS = st.slider("IPS", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f", key="prof_ips")

    IDA = pd.Series([PORT, MAT, ING]).mean(skipna=True)

    input_data = pd.DataFrame([[IAA, IAN, IDA, IEG, IPP, IPS, IPV]], 
                            columns=["IAA", "IAN", "IDA", "IEG", "IPP", "IPS", "IPV"])

    if st.button("Prever Pedra", key="prof_pred"):
        prediction = prof_model.predict(input_data)[0]
        st.write(f"### Previsão: {category_pedras[int(prediction)]}")

with sim_schol:
    
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_fase = st.selectbox("Selecione o seu Ano Escolar atual", list(fases.keys()))
    
    actual_fase, ideal_age = fases[selected_fase]

    with col2:
        actual_age = idade_aluno = st.number_input("Selecione sua idade", min_value=7, max_value=17, step=1)

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
        PORT = st.number_input("Português", min_value=0.0, max_value=10.0, value=None, format="%.1f", key="schol_port")
        IAA = st.slider("IAA", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f", key="schol_iaa")

    with col2:
        MAT = st.number_input("Matemática", min_value=0.0, max_value=10.0, value=None, format="%.1f", key="schol_mat")
        IEG = st.slider("IEG", min_value=0.0, max_value=10.0, value=5.0, step=0.1, format="%.1f", key="schol_ieg")

    with col3:
        ING = st.number_input("Inglês", min_value=0.0, max_value=10.0, value=None, format="%.1f", key="schol_ing")

    IDA = pd.Series([PORT, MAT, ING]).mean(skipna=True)

    input_data = pd.DataFrame([[IAA, IAN, IDA, IEG]], 
                            columns=["IAA", "IAN", "IDA", "IEG"])

    if st.button("Prever Pedra", key="schol_pred"):
        prediction = schol_model.predict(input_data)[0]
        st.write(f"### Previsão: {category_pedras[int(prediction)]}")