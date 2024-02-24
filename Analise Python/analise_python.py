import basedosdados as bd
import analise_sql
import funcoes

main_path = "datario.administracao_servicos_publicos.chamado_1746"
neighborhood_path = "datario.dados_mestres.bairro"
events_path = "datario.turismo_fluxo_visitantes.rede_hoteleira_ocupacao_eventos"
project_id = "dadosrio"


# QUESTÃO 1 - Quantos chamados foram abertos no dia 01/04/2023? ✅

open_os_specific_day = funcoes.apply_query(analise_sql.quantidade_chamados_dia)
open_os_specific_day = funcoes.extract_array_substrings(open_os_specific_day, "total_chamados_abertos")

# print(f"\n\nO número total de chamados abertos em 2023-04-01 foi: {open_os_specific_day}\n\n")


# QUESTÃO 2 - Qual o tipo de chamado que teve mais teve chamados abertos no dia 01/04/2023? ✅

order_by_type = funcoes.apply_query(analise_sql.maior_ocorrencia_por_tipo_dia_especifico)
order_by_type = funcoes.extract_array_substrings(order_by_type, "tipo")
# print(f"\n\n O tipo de chamado com maior número de ocorrências neste dia foi: {order_by_type}\n\n")


# QUESTÃO 3 - Quais os nomes dos 3 bairros que mais tiveram chamados abertos nesse dia? ✅

bairros_mais_ocorrencias = funcoes.apply_query(analise_sql.bairros_com_mais_chamados_neste_dia)
bairros_mais_ocorrencias = funcoes.extract_array_substrings(bairros_mais_ocorrencias, "nome_bairro")

# print(f"\n\n Os 3 bairros com maior número de ocorrências são: {bairros_mais_ocorrencias}.\n\n")

# Questão 4 - Qual o nome da subprefeitura com mais chamados abertos nesse dia? ✅
subprefeitura_mais_chamados = funcoes.apply_query(analise_sql.subprefeitura_query)
subprefeitura_mais_chamados = funcoes.extract_array_substrings(subprefeitura_mais_chamados, "subprefeitura")
# print(f"O nome da subprefeitura com maior ocorrência neste dia: {subprefeitura_mais_chamados}")


# Questão 5 - Existe algum chamado aberto nesse dia que não foi associado a um bairro ou subprefeitura na tabela de bairros? Se sim, por que isso acontece? ✅
chamado_sem_bairro_associado = funcoes.apply_query(analise_sql.chamados_bairros_nulos)
chamado_sem_bairro_associado = funcoes.extract_array_substrings(chamado_sem_bairro_associado, "quantidade")

chamado_sem_bairro_associado_na_data = funcoes.apply_query(analise_sql.chamados_bairros_nulos_na_data)
chamado_sem_bairro_associado_na_data = funcoes.extract_array_substrings(chamado_sem_bairro_associado_na_data, "quantidade")

# print(f"Ocorrências não associada à bairro ou subprefeitura sem limitar a data (ou seja, no geral): {chamado_sem_bairro_associado}.")
# print(f"\n\nOcorrências não associada à bairro ou subprefeitura no dia '2023-04-01': {chamado_sem_bairro_associado_na_data}.")

# Vários fatores podem justificar não ter prefeitura ou bairro associado, como falta de informações ao preencher ou ao não mapeamento. No caso do dia em específico, vemos que trata-se de um chamado do tipo "Ônibus" (como mostrado na query a seguir), uma verificação de ar condicionado, então, ao meu ver, não faz sentido ter um bairro associado, já que o ônibus pode percorrer vários bairros. Os outros chamados possuem outros tipos e, em alguns deles, faria sentido a informação do bairro.


# Verificando o tipo de ocorrência que não foi associado à bairros e subprefeituras
tipo_chamado_bairro_nulo_na_data = funcoes.apply_query(analise_sql.tipo_chamado_bairro_nulo_na_data)
tipo_chamado_bairro_nulo_na_data = funcoes.extract_array_substrings(tipo_chamado_bairro_nulo_na_data, "tipo")
# print(f"\nTipo de ocorrência não associada à bairro ou subprefeitura na data especificada: {tipo_chamado_bairro_nulo_na_data}.")


# QUESTÃO 6 - Quantos chamados com o subtipo "Perturbação do sossego" foram abertos desde 01/01/2022 até 31/12/2023 (incluindo extremidades)? ✅
subtipo_especifico_na_data = funcoes.apply_query(analise_sql.subtipo_especifico_na_data)
subtipo_especifico_na_data = funcoes.extract_array_substrings(subtipo_especifico_na_data, "quantidade")
# print(f"Quantidade de chamados abertos com subtipo Perturbação do sossego na data: {subtipo_especifico_na_data}")


# QUESTÃO 7 - Selecione os chamados com esse subtipo que foram abertos durante os eventos contidos na tabela de eventos (Reveillon, Carnaval e Rock in Rio). ✅
df_chamados_em_eventos = funcoes.apply_query(analise_sql.chamados_subtipo_abertos_eventos)
# print(f"Seleção de chamados abertos com subtipo Perturbação do sossego durante os eventos especificados: {df_chamados_em_eventos}")


# QUESTÃO 8 - Quantos chamados desse subtipo foram abertos em cada evento? ✅
chamados_por_evento = funcoes.apply_query(analise_sql.chamados_por_evento)
eventos = funcoes.extract_array_substrings(chamados_por_evento, "evento")
quantidade_por_evento = funcoes.extract_array_substrings(chamados_por_evento, "quantidade_por_evento")
# print(f"Para os eventos {eventos}, foram abertos {quantidade_por_evento}, respectivamente.")


# QUESTÃO 9. Qual evento teve a maior média diária de chamados abertos desse subtipo?  ✅
evento_maior_media_chamados = funcoes.apply_query(analise_sql.maior_media_por_evento)
evento_maior_media = funcoes.extract_array_substrings(evento_maior_media_chamados, "evento")
media = funcoes.extract_array_substrings(evento_maior_media_chamados, "media_diaria_chamados")
# print(f"Maior média diária de chamados abertos com subtipo Perturbação do sossego foi do evento {evento_maior_media}, com uma média diária aproximada de {round(float(media))}.")


# QUESTÃO 10 - Compare as médias diárias de chamados abertos desse subtipo durante os eventos específicos (Reveillon, Carnaval e Rock in Rio) e a média diária de chamados abertos desse subtipo considerando todo o período de 01/01/2022 até 31/12/2023. ✅
df_comparacoes_por_evento = funcoes.apply_query(analise_sql.comparacao_medias_diarias)
# print(f"Comparações solicitadas: {df_comparacoes_por_evento}")