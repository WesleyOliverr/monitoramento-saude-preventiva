Projeto Extensionista: Monitoramento de Saúde Coletiva Municipal

Este repositório contém o código de geração de dados e a base de registros parametrizados para o desenvolvimento de um painel analítico voltado ao monitoramento da saúde preventiva em comunidades locais. O projeto foi desenvolvido como Atividade Extensionista do Centro Universitário Internacional UNINTER.

📋 Descrição do Projeto

O objetivo do projeto é estruturar um modelo analítico de acompanhamento de agravos de saúde (como Hipertensão, Diabetes, Dengue, Saúde Mental e Pré-natal) na rede de atenção básica de saúde. A ferramenta permite identificar áreas com maior necessidade de ações preventivas e otimizar a tomada de decisão em gestão de saúde pública.

🔒 Nota Metodológica e Conformidade com a LGPD

Em conformidade com a Lei Geral de Proteção de Dados (LGPD — Lei nº 13.709/2018) e devido a restrições de acesso a prontuários médicos reais sem aprovação de Comitê de Ética em Pesquisa, o projeto utilizou a técnica de simulação por dados sintéticos parametrizados.

Os dados foram gerados de forma programática utilizando a linguagem Python (gerar_dados.py).

As distribuições estatísticas de faixas etárias, bairros e agravos de saúde reproduzem proporções reais observadas em relatórios públicos de saúde municipal.

A utilização de semente aleatória (seed=42) garante a reprodutibilidade exata da base para fins acadêmicos e analíticos.

🛠️ Tecnologias Utilizadas

Python 3: Para modelagem e geração da base de dados sintética.

Pandas & NumPy: Para manipulação estruturada dos dados e aplicação das distribuições probabilísticas.

Microsoft Excel: Para armazenamento da base parametrizada.

🚀 Como Executar o Script de Dados

Caso queira gerar a base de dados novamente no seu ambiente local:

Clone o repositório ou baixe os arquivos.

Certifique-se de ter o Python instalado.

Instale as dependências necessárias executando:

pip install pandas numpy openpyxl


Execute o script:

python gerar_dados.py


O arquivo dados_saude_preventiva.xlsx será gerado automaticamente no mesmo diretório.
