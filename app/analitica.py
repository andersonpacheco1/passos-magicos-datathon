import streamlit as st
import pandas as pd

st.title('Datathon Passos Mágicos')

introducao, objetivo, metodologia, resultados, conclusao, bibliografia = st.tabs(['Introdução', 'Objetivo', 'Metodologia', 'Resultados', 'Conclusão', 'Bibliografia'])

with introducao:

    st.write('## Contexto')
    st.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer scelerisque odio vel justo facilisis, vel tempus metus interdum. Nullam ut tempus lorem. 
             Integer ornare sapien libero, et congue neque tempus eu. Phasellus eget rhoncus metus. Etiam non pretium erat, in ullamcorper tortor. Ut pellentesque ut ante et vestibulum. 
             Nam ac tellus fringilla, fermentum massa vel, fermentum eros. Etiam sit amet nulla magna. Donec rutrum nisi a lobortis scelerisque. Suspendisse potenti. 
             Suspendisse imperdiet tortor a urna efficitur ultrices. Aliquam sed nisi sit amet sapien congue feugiat id sit amet magna. In lacinia blandit aliquam. 
             Nam elementum dolor semper lacus condimentum sollicitudin. Nunc eu mi eu eros faucibus ullamcorper a eu dolor.             
    ''')

    st.write('## Cenário')
    st.markdown("""
        A **Passos Mágicos** é uma organização social sem fins lucrativos que tem como objetivo **transformar a vida de crianças e adolescentes em situação de vulnerabilidade social através da educação**. O projeto começou em 1992, ajudando crianças em orfanatos.  Em 2016, expandiu-se, tornando-se a Associação Passos Mágicos.
                
        A Passos Mágicos atende a população de Embu-Guaçu, município localizado a 56 km da capital paulista. Em 2022, a organização atingiu a marca de mais de 1.000 beneficiários, o que representa cerca de 1,4% da população de Embu-Guaçu.

        **A metodologia da Passos Mágicos se baseia em quatro pilares:**

        *   **Educação de qualidade:** Oferecida através do Programa de Aceleração do Conhecimento (PAC), que inclui aulas de alfabetização, português, matemática e inglês.
        *   **Assistência psicológica:** Através de atendimentos individuais e em grupo, com o objetivo de promover o autoconhecimento, controle emocional e desenvolvimento de habilidades socioemocionais.
        *   **Ampliação da visão de mundo:** Por meio de programas que proporcionam contato com diferentes culturas, idiomas e áreas de conhecimento.
        *   **Protagonismo:** Incentivando os alunos a serem agentes de suas próprias histórias e a buscarem seus sonhos.

        Além do PAC, a Passos Mágicos oferece:

        *   **Bolsas de estudo:** Para alunos que se destacam no PAC, em escolas particulares do ensino fundamental e médio, e também no ensino superior.
        *   **Cursos técnicos:** Em parceria com o SENAI, para alunos e mães de alunos.
        *   **Auxílio para ingresso no mercado de trabalho:** Conectando alunos com oportunidades de emprego e estágio.
        *   **Assistência social:** Com atividades voltadas para o fortalecimento de vínculos familiares.

        A Passos Mágicos acredita que a **educação é a base para a transformação social** e trabalha para que cada vez mais crianças e jovens tenham a oportunidade de **realizar seus sonhos**.
    """)

    local = pd.DataFrame({'lat': [-23.8308], 'lon': [-46.8122]})

    st.map(local, latitude='lat', longitude='lon', size=5000, zoom=8)

    st.write('## Problema Central')
    st.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer scelerisque odio vel justo facilisis, vel tempus metus interdum. Nullam ut tempus lorem. 
             Integer ornare sapien libero, et congue neque tempus eu. Phasellus eget rhoncus metus. Etiam non pretium erat, in ullamcorper tortor. Ut pellentesque ut ante et vestibulum. 
             Nam ac tellus fringilla, fermentum massa vel, fermentum eros. Etiam sit amet nulla magna. Donec rutrum nisi a lobortis scelerisque. Suspendisse potenti. 
             Suspendisse imperdiet tortor a urna efficitur ultrices. Aliquam sed nisi sit amet sapien congue feugiat id sit amet magna. In lacinia blandit aliquam. 
             Nam elementum dolor semper lacus condimentum sollicitudin. Nunc eu mi eu eros faucibus ullamcorper a eu dolor.             
    ''')