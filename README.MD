# **Análise do Impacto da ONG Passos Mágicos**

## 📌 **Sobre o Projeto**

Este projeto foi desenvolvido no contexto do Datathon da pós-graduação em Data Analytics da FIAP. O objetivo é analisar o impacto da ONG **Passos Mágicos** sobre o desempenho educacional dos estudantes atendidos, utilizando técnicas de análise de dados e visualização interativa.

A **Passos Mágicos** é uma organização dedicada a transformar a realidade de crianças e jovens em situação de vulnerabilidade social por meio da educação. Com base nos dados fornecidos, este projeto visa extrair insights e gerar um storytelling que auxilie a ONG na tomada de decisões estratégicas.

## 🎯 **Objetivo**

O principal objetivo do projeto é desenvolver uma **proposta analítica**, criando um **dashboard interativo** e uma **análise exploratória dos dados** para identificar padrões e indicadores de performance dos estudantes. Além disso, foi implementada uma abordagem preditiva com dois simuladores:

- **Simulador de professores**: Utiliza **Logistic Regression** para prever o desempenho dos estudantes com base nos fatores analisados.
- **Simulador de alunos**: Utiliza **Gradient Boosting** para estimar o impacto das variáveis no desenvolvimento dos estudantes.

## 📊 **Base de Dados**

A base de dados utilizada contém informações educacionais e socioeconômicas dos estudantes atendidos pela ONG no período de **2020 a 2022**. Além disso, foram analisados relatórios institucionais fornecidos pela Passos Mágicos para contextualizar os dados e extrair insights relevantes.

## 🛠 **Metodologia e Ferramentas**

O projeto foi desenvolvido utilizando as seguintes metodologias e ferramentas:

- **Análise Exploratória de Dados (EDA)** para entender padrões e comportamentos dos estudantes.
- **Visualização de Dados** por meio de dashboards interativos.
- **Storytelling com Dados** para destacar insights e auxiliar na tomada de decisão.
- **Modelagem preditiva** com algoritmos de Machine Learning.
- **Ferramentas utilizadas**: Python, SQL, Sklearn, Pandas, Pycaret, Streamlit e Plotly.


**Descrição dos diretórios e arquivos principais:**

- `app/`: Contém o código-fonte da aplicação principal, incluindo o script `main.py` que inicia o aplicativo.
- `data/`: Diretório para os dados do projeto.
  - `raw/`: Armazena os dados brutos originais.
  - `processed/`: Contém os dados processados e prontos para análise.
- `datathon/`: Inclui materiais relacionados ao desafio do Datathon, como o arquivo `desafio.pdf`.
- `models/`: Guarda os modelos treinados, como `modelo_simulador_professores.pkl` e `modelo_simulador_alunos.pkl`.
- `notebooks/`: Contém os Jupyter Notebooks utilizados para análise exploratória e treinamento dos modelos.
- `reports/`: Diretório para relatórios gerados.
  - `figures/`: Armazena figuras e gráficos utilizados nos relatórios.
- `resources/`: Inclui recursos adicionais, como imagens e outros arquivos de suporte.
- `.gitignore`: Especifica arquivos e diretórios a serem ignorados pelo Git.
- `logs.log`: Arquivo de log para monitoramento da aplicação.
- `packages.txt`: Lista de pacotes necessários para o ambiente.
- `requirements.txt`: Arquivo com as dependências do projeto.
- `README.md`: Este arquivo, fornecendo uma visão geral do projeto.

## 📂 **Entrega**

A entrega deste projeto consiste em:

- [**Dashboard Interativo**](https://datathon-fiap.streamlit.app/) com insights visuais dos dados.
- **Relatório Analítico** detalhando os achados e interpretações.
- **Repositório no GitHub** contendo o [código-fonte e documentação](https://github.com/andersonpacheco1/passos-magicos-datathon).

## 🚀 **Como Executar o Projeto**

Para rodar o projeto localmente:

1. Clone este repositório:
   ```bash
   git clone https://github.com/andersonpacheco1/passos-magicos-datathon.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd passos-magicos-datathon
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação Streamlit:
   ```bash
   streamlit run app.py
   ```

## 📬 **Contato**

Caso tenha dúvidas ou sugestões, entre em contato!

- 👨‍💻 **Anderson Pacheco e Humberto Costa**

---

💡 **Este projeto busca impactar positivamente a educação de crianças e jovens. Sua contribuição é bem-vinda!**

