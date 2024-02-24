import basedosdados as bd

main_path = "datario.administracao_servicos_publicos.chamado_1746"
neighborhood_path = "datario.dados_mestres.bairro"
events_path = "datario.turismo_fluxo_visitantes.rede_hoteleira_ocupacao_eventos"
project_id = "dadosrio"


quantidade_chamados_dia = f"""
SELECT
  COUNT(*) AS total_chamados_abertos
FROM
  {main_path}
WHERE
  DATE(data_inicio) = '2023-04-01';
"""

maior_ocorrencia_por_tipo_dia_especifico = f"""
SELECT
  tipo,
  COUNT(*) AS total_ocorrencias
FROM
  {main_path}
WHERE
  DATE(data_inicio) = '2023-04-01'
GROUP BY
  tipo
ORDER BY
  total_ocorrencias DESC
LIMIT
  1;
"""

bairros_com_mais_chamados_neste_dia = f"""
SELECT 
    b.nome AS nome_bairro,
    c.recorrencia_bairro AS recorrencia
FROM 
    {neighborhood_path} b
JOIN (
    SELECT 
        id_bairro,
        COUNT(*) AS recorrencia_bairro 
    FROM 
        {main_path}
    WHERE 
        DATE(data_inicio) = '2023-04-01'
    GROUP BY 
        id_bairro
    ORDER BY 
        recorrencia_bairro DESC 
    LIMIT 3
) c ON b.id_bairro = c.id_bairro;

"""

subprefeitura_query = f"""
SELECT subprefeitura
FROM {neighborhood_path}
WHERE id_bairro IN (
    SELECT id_bairro
    FROM (
        SELECT id_bairro, COUNT(*) AS recorrencia_bairro 
        FROM {main_path}
        WHERE DATE(data_inicio) = '2023-04-01'
        GROUP BY id_bairro 
        ORDER BY recorrencia_bairro DESC 
        LIMIT 1
    )
);
"""

chamados_bairros_nulos = f"""
SELECT COUNT(*) AS quantidade
FROM {main_path} AS c
LEFT JOIN {neighborhood_path} AS b ON c.id_bairro = b.id_bairro
WHERE b.id_bairro IS NULL;
"""

chamados_bairros_nulos_na_data = f"""
SELECT COUNT(*) AS quantidade
FROM {main_path} AS c
LEFT JOIN {neighborhood_path} AS b ON c.id_bairro = b.id_bairro
WHERE DATE(c.data_inicio) = '2023-04-01' AND b.id_bairro IS NULL;
"""

tipo_chamado_bairro_nulo_na_data = f"""
SELECT tipo, status
FROM {main_path} AS c
LEFT JOIN {neighborhood_path} AS b ON c.id_bairro = b.id_bairro
WHERE DATE(c.data_inicio) = '2023-04-01' AND b.id_bairro IS NULL;
"""

subtipo_especifico_na_data = f"""
SELECT
  COUNT (*) as quantidade
FROM
  {main_path}
WHERE
  DATE(data_inicio) BETWEEN '2022-01-01' AND '2023-12-31'
  AND subtipo = 'Perturbação do sossego';
"""

chamados_subtipo_abertos_eventos = f"""
SELECT
  c.*
FROM
  {main_path} AS c
JOIN
  {events_path} AS e
ON
  DATE(c.data_inicio) BETWEEN DATE(e.data_inicial)
  AND DATE(e.data_final)
WHERE
  c.subtipo = 'Perturbação do sossego'
  AND e.evento IN ('Reveillon',
    'Carnaval',
    'Rock in Rio');
"""

chamados_por_evento = f"""
SELECT
  e.evento AS evento,
  COUNT(*) AS quantidade_por_evento
FROM
  {main_path} AS c
JOIN
  {events_path} AS e
ON
  DATE(c.data_inicio) BETWEEN DATE(e.data_inicial)
  AND DATE(e.data_final)
WHERE
  c.subtipo = 'Perturbação do sossego'
  AND e.evento IN ('Reveillon',
    'Carnaval',
    'Rock in Rio')
GROUP BY
  e.evento;
"""

maior_media_por_evento = f"""
SELECT
  e.evento as evento,
  COUNT(*) / TIMESTAMP_DIFF(DATE(MAX(c.data_inicio)), DATE(MIN(c.data_inicio)), DAY) AS media_diaria_chamados
FROM
  {main_path} AS c
JOIN
  {events_path} AS e
ON
  DATE(c.data_inicio) BETWEEN DATE(e.data_inicial)
  AND DATE(e.data_final)
WHERE
  c.subtipo = 'Perturbação do sossego'
  AND e.evento IN ('Reveillon',
    'Carnaval',
    'Rock in Rio')
GROUP BY
  e.evento
ORDER BY
  media_diaria_chamados DESC
LIMIT
  1;
""" 

comparacao_medias_diarias = f"""
  -- Média diária durante os eventos específicos
WITH
  media_diaria_eventos AS (
  SELECT
    e.evento,
    COUNT(*) / TIMESTAMP_DIFF(DATE(MAX(c.data_inicio)), DATE(MIN(c.data_inicio)), DAY) AS media_diaria_chamados_evento
  FROM
   {main_path} AS c
  JOIN
    {events_path} AS e
  ON
    DATE(c.data_inicio) BETWEEN DATE(e.data_inicial)
    AND DATE(e.data_final)
  WHERE
    c.subtipo = 'Perturbação do sossego'
    AND e.evento IN ('Reveillon',
      'Carnaval',
      'Rock in Rio')
  GROUP BY
    e.evento ),
  -- Média diária durante todo o período
  media_diaria_total AS (
  SELECT
    COUNT(*) / TIMESTAMP_DIFF('2023-12-31', '2022-01-01', DAY) AS media_diaria_chamados_total
  FROM
    {main_path} AS c
  WHERE
    c.subtipo = 'Perturbação do sossego'
    AND DATE(c.data_inicio) BETWEEN '2022-01-01'
    AND '2023-12-31' )
    
  -- Combinando as médias diárias durante os eventos específicos com a média diária total
SELECT
  'Média Diária Durante Eventos' AS tipo_media,
  evento,
  media_diaria_chamados_evento AS media_diaria_chamados
FROM
  media_diaria_eventos
UNION ALL
SELECT
  'Média Diária Total' AS tipo_media,
  NULL,
  media_diaria_chamados_total
FROM
  media_diaria_total;
"""