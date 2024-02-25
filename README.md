# Desafio Técnico - Cientista de Dados Júnior

## Descrição

Bem-vindo! Este é um fork do repositório original do desafio e aqui estão as minhas respostas para o desafio técnico para a vaga de Cientista de Dados Júnior no Escritório Municipal de Dados do Rio de Janeiro. Este desafio tem o objetivo de avaliar habilidades técnicas em manipulação de dados, consulta SQL, análise de dados e visualização de dados utilizando ferramentas como BigQuery e Python. Para a visualização dos dados, criei uma aplicação local usando Streamlit.

### Objetivo

O objetivo deste desafio é realizar análises exploratórias em conjuntos de dados públicos disponíveis no BigQuery, responder a perguntas específicas sobre esses dados utilizando SQL e Python, e criar visualizações informativas e visualmente atraentes. Nessa branch, você encontrará somente a visualização dos dados em forma de dados. Na branch main estão as respostas às perguntas do desafio.

### Conjunto de Dados

Os conjuntos de dados utilizados neste desafio são:

- **Chamados do 1746:** Dados relacionados a chamados de serviços públicos na cidade do Rio de Janeiro. O caminho da tabela é : `datario.administracao_servicos_publicos.chamado_1746`
- **Bairros do Rio de Janeiro:** Dados sobre os bairros da cidade do Rio de Janeiro - RJ. O caminho da tabela é: `datario.dados_mestres.bairro`
- **Ocupação Hoteleira em Grandes Eventos no Rio**: Dados contendo o período de duração de alguns grandes eventos que ocorreram no Rio de Janeiro em 2022 e 2023 e a taxa de ocupação hoteleira da cidade nesses períodos. O caminho da tabela é: `datario.turismo_fluxo_visitantes.rede_hoteleira_ocupacao_eventos`

### Ferramentas e Recursos

Você precisará de acesso ao Google Cloud Platform (GCP) para utilizar o BigQuery e consultar os dados públicos disponíveis no projeto `datario`. Além disso, vamos utilizar a biblioteca `basedosdados` em Python para acessar os dados do BigQuery.

- Tutorial para acessar dados no BigQuery, desde a criação da conta no GCP até consultar os dados utilizando SQL e Python: [Como acessar dados no BigQuery](https://docs.dados.rio/tutoriais/como-acessar-dados/)

### Perguntas do Desafio

As perguntas do desafio estão detalhadas no arquivo `perguntas_desafio.md`. As respostas das perguntas estão na branch main e a visualização dos dados extraídos está nesta branch.

## Etapas - Streamlit

1. Siga o tutorial acima para criar sua conta no GCP e aprender como utilizar o BigQuery para consultar os dados. Você precisa ter um id válido de projeto para conseguir fazer as consultas do arquivo `querys.py`.
2. Com o Google Cloud Studio e BigQuery já configurados, é possível fazer as consultas disponíveis nos arquivos para construir a visualização dos dados (`querys.py`, alterando somente o id do projeto no início dos arquivos). A consulta só funcionará mediante a prévia configuração nas plataformas mencionadas e autenticação de conta.
3. Tenha certeza de que todos os pacotes listados em `requirements.txt` estão instalados e configurados propriamente nas variáveis do sistema. Para facilitar o processo, você pode criar e ativar o ambiente virtual e rodar o comando `pip install -r requirements.txt`, baixando tudo que é necessário de uma só vez.
4. Pronto. Agora podemos visualizar as tabelas. No terminal, dentro da pasta `Dashboard`, rode o comando `streamlit run dashboard.py` para visualizar os dados em um formato mais parecido com um Dashboard ou `streamlit run view.py`, para visualizar tabelas que se aproximam mais de um relatório.
5. Uma aplicação web aparecerá e irá carregar a medida que as consultas vão sendo feitas para constuir as tabelas e gráficos.

## Possíveis problemas
- O comando `streamlit run arquivo.py` pode retornar um erro de path. Isso significa que o seu pacote provavelmente não está configurado nas variáveis do sistema. Caso isso ocorra, basta digitar 
`export PATH="/Users/seu_usuario/Library/Python/3.9/bin:$PATH`
no seu terminal, alterando `seu_usuario` pelo seu user. Depois disso, `streamlit run` funcionará normalmente.
[x] Caso esteja usando o ambiente virtual, basta digitar esse comando uma vez. Se não, você provavelmente precisará dele algumas vezes antes de rodar a aplicação streamlit.

- Se as querys não estiverem funcionando corretamente, certifique-se de **alterar o id da variável `project_id` pelo id do seu projeto criado na conta do Google Cloud no arquivo `Dashboard/funcoes`**. Esse é o único dado que precisa ser alterado para que elas funcionem.

## Contribuições
Para contribuir, sinta-se livre para criar issues no projeto e/ou entrar em contato.

## Autoria
Por Milena Maia
<br>
email: milenamaiaaraujo@gmail.com
