# Guia Completo: Base de Dados de Aproveitamentos Hídricos de Portugal

## 📊 Fontes Principais de Dados

### 1. **Open Infrastructure Map (OpenStreetMap)**
- **URL**: https://openinframap.org/stats/area/Portugal/plants?source=hydro
- **Dados Disponíveis**: 
  - 200 centrais hidroelétricas mapeadas
  - Potência instalada: 8.513 MW
  - Localização geográfica em mapa interativo
  - Tipo de aproveitamento (armazenamento vs fio de água)
  - Operador/Proprietário
  - Potência individual de cada central

**Vantagens**:
- ✅ Dados geoespaciais (mapa interativo)
- ✅ Acesso aberto e gratuito
- ✅ Classificação por tipo de aproveitamento
- ✅ Dados estruturados em tabela exportável

**Limitações**:
- ❌ Podem ter lacunas (nem todas as centrais)
- ❌ Dados crowdsourced (variam em precisão)

---

### 2. **Agência Portuguesa do Ambiente (APA) - Barragens de Portugal**
- **URL**: https://apambiente.pt/prevencao-e-gestao-de-riscos/barragens-de-portugal
- **Dados Disponíveis**:
  - 260 grandes barragens (altura > 15m ou volume > 1 hm³)
  - Lista completa de albufeiras classificadas
  - Informações de utilização (produção energia, rega, abastecimento)
  - Classificação de estado e proteção

**Informação Detalhada**:
- Disponível: https://apambiente.pt/agua/lista-de-albufeiras-lagos-e-lagoas-classificados

**Dados por Bacia Hidrográfica**:
- Lima
- Cávado
- Douro
- Mondego
- Vouga
- Ribeiras do Oeste
- Mira
- Guadiana

---

### 3. **Boletim Semanal de Albufeiras (APA)**
- **URL**: https://apambiente.pt/agua/sistema-nacional-de-informacao-de-recursos-hidricos-snirh
- **Dados Disponíveis**:
  - Volume armazenado em tempo real
  - Percentagem de enchimento por albufeira
  - Evolução semanal/mensal
  - Dados históricos (desde 1990/91)
  - Situação crítica de albufeiras

---

### 4. **Comissão Nacional Portuguesa de Grandes Barragens (CNPGB)**
- **Mapa Oficial**: https://cnpgb.apambiente.pt/mapabarragens
- **Lista Completa**: https://cnpgb.apambiente.pt/lista_barragens
- **Dados Disponíveis**:
  - Localização por distrito e concelho
  - Características técnicas
  - Estado de segurança
  - Regulação normativa

---

### 5. **Energias de Portugal (EDP) - Dados Corporativos**
- **Relatório 2024**: https://www.edp.com/pt/noticia/relatorio-anual
- **Dados Disponíveis**:
  - 46 centrais hidroelétricas operacionais
  - Potência total: 5.785 MW
  - Produção anual média: 11.400 GWh
  - Informações por sistema de aproveitamento:
    - Sistema do Douro (17+3 centrais, 1.656 MW)
    - Sistema do Tejo-Mondego (10 centrais, 1.552 MW)
    - Sistema do Cávado-Lima (37 centrais, 160 MW)
  - Características de cada central (tipo, produtibilidade, infraestruturas)

**Documentos Técnicos**:
- EMAS Declaration 2024: Dados ambientais e operacionais detalhados
- Relatório EDP A Hidroeletricidade em Portugal

---

### 6. **SNIRH - Sistema Nacional de Informação de Recursos Hídricos**
- **URL**: https://snirh.apambiente.pt/
- **Dados Disponíveis**:
  - Monitorização em tempo real
  - Dados hidrológicos por bacia
  - Qualidade da água
  - Caudais
  - Séries históricas

---

### 7. **REN Data Hub**
- **URL**: https://datahub.ren.pt/
- **Dados Disponíveis**:
  - Informação sobre energia em Portugal
  - Transformação do setor energético
  - Dados de transmissão
  - Integração de fontes renováveis

---

### 8. **Geoportal LNEG - Base de Dados Hidrogeológicos**
- **URL**: https://geoportal.lneg.pt/pt/bds/rec_hidrogeol
- **Dados Disponíveis**:
  - Informação geológica
  - Recursos hidrogeológicos
  - Furos, poços, nascentes
  - Sondagens em todo o país

---

### 9. **APREN - Associação Portuguesa de Energias Renováveis**
- **Mapa E2P**: Mapa de Centros Eletroprodutores Renováveis em Portugal
- **Dados Disponíveis**:
  - Localização de todas as centrais renováveis
  - Classificação por tipo
  - Dados técnicos

---

### 10. **INSPIRE Geoportal - Centrais Hídricas**
- **URL**: https://inspire-geoportal.ec.europa.eu/
- **Dados Disponíveis**:
  - Grandes hídricas e mini-hídricas
  - Dados de licenciamento
  - Dados geoespaciais em conformidade europeia
  - Informação de Direção-Geral de Energia

---

### 11. **APA - Aproveitamentos Hidráulicos e Concessões**
- **Lista de Instalações (PDF)**: https://apambiente.pt/sites/default/files/_Agua/DRH/Licenciamento/AH_Concessoes/AH_Lista.pdf
- **Portal de Concessões**: https://apambiente.pt/agua/aproveitamentos-hidraulicos-concessoes
- **Dados Disponíveis**:
  - Lista oficial de instalações licenciadas
  - Informação sobre concessões de domínio hídrico

---

## 12. Dados Críticos de Concessão e Operação

Para obter dados detalhados sobre **Dono/Operador, Prazos e Estado da Concessão**, utilize a seguinte estratégia combinada:

### Fontes para Dados Contratuais
1. **SNITURH (APA) - Títulos de Utilização de Recursos Hídricos**
   - **O que procurar**: Identificação do titular oficial e prazo da licença.
   - **Como aceder**: Pesquisar listas de "Títulos Emitidos" nos sites das ARH (Administrações de Região Hidrográfica) ou no portal da APA.

2. **Relatórios Anuais de Operadores (EDP, Movhera, Iberdrola, Endesa)**
   - **EDP**: Consulte a secção "Ativos Intangíveis" nos Relatórios e Contas Anuais. Detalha a vida útil restante das concessões.
   - **Movhera**: Detém as concessões do Douro (Miranda, Picote, Bemposta, Baixo Sabor, Feiticeiro, Foz Tua) adquiridas em 2020. Prazo médio remanescente reportado na aquisição: ~45 anos.
   - **Iberdrola**: Sistema do Tâmega (Gouvães, Daivões, Alto Tâmega). Concessões de 75 anos a contar do início da exploração (c. 2022-2024), válidas até ~2097.

3. **Diário da República (DRE)**
   - A fonte definitiva para datas exatas.
   - **Pesquisa Chave**: `"contrato de concessão" + [Nome da Barragem]`
   - **Pesquisa Chave**: `"caducidade concessão aproveitamento"` (para identificar centrais revertidas ao Estado).

### Classificação de Estado da Concessão
- **Ativo**: Concessão em vigor (maioria das grandes barragens).
- **Prorrogação**: Concessão expirou mas o operador mantém gestão provisória (ex: Barragem do Cabril, expirou em 2022).
- **Revertido/Expirado**: Concessão terminou e o ativo reverteu para o Estado (comum em mini-hídricas antigas).

---

## 📋 Estrutura Recomendada para Base de Dados (Completa)

Esta estrutura foi desenhada para capturar todas as dimensões do ativo: técnica, geográfica, legal e operacional.

### 1. Identificação e Estado (Tabela `centrais_hidricas`)
- `id_central` (PK - Chave Primária)
- `nome_oficial`: Nome registado no título (ex: "Aproveitamento Hidroelétrico de France")
- `nome_comum`: Nome pelo qual é conhecida (ex: "Barragem de Covas")
- `codigo_apa`: Código oficial da Agência Portuguesa do Ambiente
- `codigo_snirh`: Código de monitorização no SNIRH
- `estado_operacional`: Operacional / Em Construção / Desativada / Demolida
- `tipo_instalacao`: Barragem com Albufeira / Fio de Água / Bombagem (PHE) / Mini-hídrica

### 2. Concessão e Propriedade (Tabela `concessoes`)
- `id_concessao` (PK)
- `central_id` (FK - Chave Estrangeira para `centrais_hidricas`)
- `operador_atual`: Entidade que explora (ex: Movhera, EDP Produção, Aquila Capital)
- `titular_titulo`: Titular legal do TURH (pode ser diferente do operador)
- `data_inicio_concessao`: Data de assinatura do contrato ou publicação do decreto
- `data_fim_concessao`: Data de termo do contrato atual
- `duracao_anos`: Anos totais da concessão (ex: 75)
- `estado_legal`: Ativa / Prorrogada / Caducada / Revertida ao Estado
- `link_documento_legal`: URL para o contrato ou decreto no Diário da República
- `notas_contratuais`: Observações sobre condições especiais, prorrogações, etc.

### 3. Localização Geográfica (Tabela `localizacoes`)
- `id_localizacao` (PK)
- `central_id` (FK)
- `bacia_hidrografica_principal`: (ex: Douro, Lima, Minho, Vouga)
- `curso_agua`: Rio ou ribeira específica (ex: Rio Coura, Rio Tejo)
- `distrito`: Unidade administrativa (ex: Viana do Castelo, Vila Real)
- `concelho`: Município (ex: Vila Nova de Cerveira, Peso da Régua)
- `freguesia`: Divisão administrativa (ex: Covas, Sabrosa)
- `coordenadas_longitude`: Longitude (WGS84)
- `coordenadas_latitude`: Latitude (WGS84)
- `geom`: Objeto geométrico para GIS (Point SRID 4326)

### 4. Características Técnicas de Produção (Tabela `dados_tecnicos`)
- `id_dados_tecnicos` (PK)
- `central_id` (FK)
- `potencia_instalada_mw`: Potência total instalada (ex: 44.1 MW)
- `produtibilidade_media_gwh`: Produção média anual (ex: 120.5 GWh)
- `ano_entrada_servico`: Ano de início de operação comercial
- `num_grupos_geradores`: Quantidade de turbinas/grupos
- `tipo_turbinas`: Francis / Pelton / Kaplan / Bulbo / Crossflow
- `caudal_maximo_m3s`: Caudal máximo turbinável (m³/s)
- `queda_bruta_m`: Desnível máximo útil (metros)
- `eficiencia_media_percent`: Rendimento médio de conversão

### 5. Barragem e Albufeira (Tabela `dados_hidraulicos`)
- `id_dados_hidraulicos` (PK)
- `central_id` (FK)
- `tipo_barragem`: Arco / Gravidade / Arco-Gravidade / Terra / Enrocamento / Desnivelada
- `altura_cota_fundacao_m`: Altura máxima desde a fundação
- `comprimento_coroamento_m`: Extensão do topo da barragem
- `capacidade_total_hm3`: Volume total armazenável (hm³)
- `capacidade_util_hm3`: Volume utilizável para produção (hm³)
- `area_inundada_km2`: Área da superfície da albufeira em NPA (km²)
- `cota_npa_m`: Nível de Pleno Armazenamento (metros)
- `cota_nme_m`: Nível Mínimo de Exploração (metros)
- `caudal_ecologico_m3s`: Caudal obrigatório para jusante

### 6. Dados de Monitorização (Tabela `monitorização_operacional`)
- `id_monitoramento` (PK)
- `central_id` (FK)
- `data_leitura`: Data/Hora da medição
- `volume_albufeira_hm3`: Volume atual armazenado
- `percentagem_enchimento`: Nível de enchimento (%)
- `producao_diaria_gwh`: Produção do dia (GWh)
- `caudal_actual_m3s`: Caudal turbinado atual
- `fonte_dados`: SNIRH / EDP / Operador / Manual

---

## 🔧 Script SQL para Criação (PostgreSQL/PostGIS)

Este script cria uma estrutura relacional robusta, normalizada e pronta para produção.

```sql
-- ============================================================
-- EXTENSÕES NECESSÁRIAS
-- ============================================================
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- ============================================================
-- TABELA 1: CENTRAIS HÍDRICAS (Base)
-- ============================================================
CREATE TABLE centrais_hidricas (
    id_central SERIAL PRIMARY KEY,
    nome_oficial VARCHAR(255) NOT NULL UNIQUE,
    nome_comum VARCHAR(255),
    codigo_apa VARCHAR(50),
    codigo_snirh VARCHAR(50),
    tipo_instalacao VARCHAR(50) NOT NULL CHECK (
        tipo_instalacao IN ('Barragem Albufeira', 'Fio de Água', 'Bombagem', 'Mini-hídrica')
    ),
    estado_operacional VARCHAR(50) DEFAULT 'Operacional' CHECK (
        estado_operacional IN ('Operacional', 'Em Construção', 'Desativada', 'Demolida', 'Pré-operacional')
    ),
    descricao TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- TABELA 2: CONCESSÕES (Dados Legais e Contratuais)
-- ============================================================
CREATE TABLE concessoes (
    id_concessao SERIAL PRIMARY KEY,
    central_id INTEGER NOT NULL UNIQUE REFERENCES centrais_hidricas(id_central) ON DELETE CASCADE,
    operador_atual VARCHAR(150),
    titular_titulo VARCHAR(150) NOT NULL,
    data_inicio_concessao DATE,
    data_fim_concessao DATE,
    duracao_anos INTEGER,
    estado_legal VARCHAR(50) NOT NULL DEFAULT 'Ativa' CHECK (
        estado_legal IN ('Ativa', 'Prorrogação', 'Caducada', 'Revertida', 'Em Renegociação')
    ),
    numero_decreto_lei VARCHAR(50), -- Ex: "Decreto-Lei nº 107/1970"
    link_documento_legal TEXT, -- URL para o Diário da República
    notas_contratuais TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- TABELA 3: LOCALIZAÇÕES GEOGRÁFICAS
-- ============================================================
CREATE TABLE localizacoes (
    id_localizacao SERIAL PRIMARY KEY,
    central_id INTEGER NOT NULL UNIQUE REFERENCES centrais_hidricas(id_central) ON DELETE CASCADE,
    bacia_hidrografica VARCHAR(100) NOT NULL,
    curso_agua VARCHAR(100) NOT NULL,
    distrito VARCHAR(100) NOT NULL,
    concelho VARCHAR(100) NOT NULL,
    freguesia VARCHAR(100),
    coordenada_latitude NUMERIC(10, 6) NOT NULL,
    coordenada_longitude NUMERIC(10, 6) NOT NULL,
    geom GEOMETRY(POINT, 4326) NOT NULL, -- Formato GIS (WGS84)
    altitude_m INTEGER,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- TABELA 4: DADOS TÉCNICOS DE PRODUÇÃO
-- ============================================================
CREATE TABLE dados_tecnicos (
    id_dados_tecnicos SERIAL PRIMARY KEY,
    central_id INTEGER NOT NULL UNIQUE REFERENCES centrais_hidricas(id_central) ON DELETE CASCADE,
    potencia_instalada_mw NUMERIC(10, 2) NOT NULL,
    potencia_nominal_mw NUMERIC(10, 2),
    produtibilidade_media_gwh NUMERIC(10, 2),
    produtibilidade_minima_gwh NUMERIC(10, 2),
    produtibilidade_maxima_gwh NUMERIC(10, 2),
    ano_entrada_servico INTEGER,
    num_grupos_geradores INTEGER,
    tipo_turbinas VARCHAR(100),
    fabricante_turbinas VARCHAR(150),
    caudal_maximo_m3s NUMERIC(10, 2),
    caudal_minimo_m3s NUMERIC(10, 2),
    queda_bruta_m NUMERIC(10, 2),
    queda_liquida_m NUMERIC(10, 2),
    eficiencia_media_percent NUMERIC(5, 2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- TABELA 5: DADOS HIDRÁULICOS E BARRAGEM
-- ============================================================
CREATE TABLE dados_hidraulicos (
    id_dados_hidraulicos SERIAL PRIMARY KEY,
    central_id INTEGER NOT NULL UNIQUE REFERENCES centrais_hidricas(id_central) ON DELETE CASCADE,
    tipo_barragem VARCHAR(100) NOT NULL,
    material_barragem VARCHAR(100),
    altura_cota_fundacao_m NUMERIC(10, 2),
    altura_coroamento_m NUMERIC(10, 2),
    comprimento_coroamento_m NUMERIC(10, 2),
    espessura_maxima_m NUMERIC(10, 2),
    capacidade_total_hm3 NUMERIC(10, 3),
    capacidade_util_hm3 NUMERIC(10, 3),
    capacidade_minima_hm3 NUMERIC(10, 3),
    area_inundada_km2 NUMERIC(10, 3),
    cota_npa_m NUMERIC(10, 2), -- Nível de Pleno Armazenamento
    cota_nme_m NUMERIC(10, 2), -- Nível Mínimo de Exploração
    cota_fundacao_m NUMERIC(10, 2),
    caudal_ecologico_m3s NUMERIC(10, 2),
    caudal_vertedor_maximo_m3s NUMERIC(10, 2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- TABELA 6: MONITORIZAÇÃO OPERACIONAL (Time Series)
-- ============================================================
CREATE TABLE monitorizacao_operacional (
    id_monitoramento SERIAL PRIMARY KEY,
    central_id INTEGER NOT NULL REFERENCES centrais_hidricas(id_central) ON DELETE CASCADE,
    data_leitura TIMESTAMP NOT NULL,
    volume_albufeira_hm3 NUMERIC(10, 3),
    percentagem_enchimento NUMERIC(5, 2) CHECK (percentagem_enchimento BETWEEN 0 AND 100),
    producao_diaria_gwh NUMERIC(10, 2),
    producao_horaria_mwh NUMERIC(10, 2),
    caudal_turbinado_m3s NUMERIC(10, 2),
    caudal_vertido_m3s NUMERIC(10, 2),
    caudal_ecologico_m3s NUMERIC(10, 2),
    temperatura_agua_celsius NUMERIC(5, 2),
    fonte_dados VARCHAR(100) CHECK (
        fonte_dados IN ('SNIRH', 'EDP', 'Operador', 'Manual', 'API_Externa')
    ),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- ÍNDICES PARA PERFORMANCE
-- ============================================================
CREATE INDEX idx_centrais_nome ON centrais_hidricas(nome_oficial);
CREATE INDEX idx_centrais_tipo ON centrais_hidricas(tipo_instalacao);
CREATE INDEX idx_centrais_estado ON centrais_hidricas(estado_operacional);

CREATE INDEX idx_concessao_operador ON concessoes(operador_atual);
CREATE INDEX idx_concessao_fim ON concessoes(data_fim_concessao);
CREATE INDEX idx_concessao_estado ON concessoes(estado_legal);

CREATE INDEX idx_localizacao_bacia ON localizacoes(bacia_hidrografica);
CREATE INDEX idx_localizacao_concelho ON localizacoes(concelho);
CREATE INDEX idx_localizacao_geom ON localizacoes USING GIST(geom);

CREATE INDEX idx_monitoramento_data ON monitorizacao_operacional(data_leitura);
CREATE INDEX idx_monitoramento_central ON monitorizacao_operacional(central_id, data_leitura);
```

---

## 📥 Exemplo de Inserção de Dados (Mini-hídrica de France - Vila Nova de Cerveira)

```sql
-- ============================================================
-- 1. INSERIR CENTRAL HIDROELÉTRICA
-- ============================================================
INSERT INTO centrais_hidricas (
    nome_oficial, 
    nome_comum, 
    codigo_apa, 
    tipo_instalacao, 
    estado_operacional
) VALUES (
    'Aproveitamento Hidroelétrico de France',
    'Mini-hídrica de Covas / Central de France',
    'AH-CN-001',
    'Mini-hídrica',
    'Operacional'
) RETURNING id_central;

-- Resultado esperado: id_central = 1

-- ============================================================
-- 2. INSERIR LOCALIZAÇÃO
-- ============================================================
INSERT INTO localizacoes (
    central_id, 
    bacia_hidrografica, 
    curso_agua, 
    distrito, 
    concelho, 
    freguesia,
    coordenada_latitude, 
    coordenada_longitude,
    geom
) VALUES (
    1,
    'Minho',
    'Rio Coura',
    'Viana do Castelo',
    'Vila Nova de Cerveira',
    'Covas',
    41.889,
    -8.705,
    ST_SetSRID(ST_MakePoint(-8.705, 41.889), 4326)
);

-- ============================================================
-- 3. INSERIR DADOS DA CONCESSÃO
-- ============================================================
INSERT INTO concessoes (
    central_id,
    operador_atual,
    titular_titulo,
    data_inicio_concessao,
    data_fim_concessao,
    duracao_anos,
    estado_legal,
    numero_decreto_lei,
    link_documento_legal,
    notas_contratuais
) VALUES (
    1,
    'Aquila Capital',
    'Aquila Capital (ex-EDP Small Hydro)',
    '1970-03-11',
    '2045-03-11',
    75,
    'Ativa',
    'Decreto-Lei nº 107/1970',
    'https://diariodarepublica.pt/dr/detalhe/decreto-lei/107-1970-228669',
    'Transferida de EDP Small Hydro para Aquila Capital em Dezembro 2018. Portfólio de 21 mini-hídricas.'
);

-- ============================================================
-- 4. INSERIR DADOS TÉCNICOS
-- ============================================================
INSERT INTO dados_tecnicos (
    central_id,
    potencia_instalada_mw,
    potencia_nominal_mw,
    produtibilidade_media_gwh,
    ano_entrada_servico,
    num_grupos_geradores,
    tipo_turbinas,
    caudal_maximo_m3s,
    queda_bruta_m,
    eficiencia_media_percent
) VALUES (
    1,
    1.2,
    1.2,
    5.0,
    1974,
    1,
    'Francis',
    0.6,
    25.0,
    82.0
);

-- ============================================================
-- 5. INSERIR DADOS DA BARRAGEM
-- ============================================================
INSERT INTO dados_hidraulicos (
    central_id,
    tipo_barragem,
    material_barragem,
    altura_coroamento_m,
    capacidade_total_hm3,
    cota_npa_m,
    cota_nme_m,
    caudal_ecologico_m3s
) VALUES (
    1,
    'Pequena Barragem',
    'Betão',
    8.0,
    0.50,
    150.0,
    145.0,
    0.15
);
```

---

## 📊 Consultas Úteis para Análise

```sql
-- Listar todas as centrais com concessão a expirar nos próximos 10 anos
SELECT 
    ch.nome_oficial,
    c.operador_atual,
    c.data_fim_concessao,
    (c.data_fim_concessao - CURRENT_DATE) / 365 AS anos_restantes,
    l.bacia_hidrografica
FROM centrais_hidricas ch
JOIN concessoes c ON ch.id_central = c.central_id
JOIN localizacoes l ON ch.id_central = l.central_id
WHERE c.data_fim_concessao BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '10 years'
ORDER BY c.data_fim_concessao ASC;

-- Capacidade total de armazenamento por bacia hidrográfica
SELECT 
    l.bacia_hidrografica,
    COUNT(ch.id_central) AS num_centrais,
    SUM(dh.capacidade_total_hm3) AS capacidade_total_hm3,
    SUM(dt.potencia_instalada_mw) AS potencia_total_mw
FROM centrais_hidricas ch
JOIN localizacoes l ON ch.id_central = l.central_id
JOIN dados_hidraulicos dh ON ch.id_central = dh.central_id
JOIN dados_tecnicos dt ON ch.id_central = dt.central_id
WHERE ch.tipo_instalacao = 'Barragem Albufeira'
GROUP BY l.bacia_hidrografica
ORDER BY capacidade_total_hm3 DESC;

-- Localizar centrais por operador
SELECT 
    c.operador_atual,
    COUNT(ch.id_central) AS num_centrais,
    SUM(dt.potencia_instalada_mw) AS potencia_mw,
    SUM(dt.produtibilidade_media_gwh) AS producao_gwh_ano
FROM centrais_hidricas ch
JOIN concessoes c ON ch.id_central = c.central_id
JOIN dados_tecnicos dt ON ch.id_central = dt.central_id
WHERE c.operador_atual IS NOT NULL
GROUP BY c.operador_atual
ORDER BY potencia_mw DESC;

-- Centrais ordenadas por potência instalada (Top 10)
SELECT 
    ch.nome_oficial,
    l.bacia_hidrografica,
    c.operador_atual,
    dt.potencia_instalada_mw,
    dt.produtibilidade_media_gwh,
    ch.tipo_instalacao
FROM centrais_hidricas ch
JOIN dados_tecnicos dt ON ch.id_central = dt.central_id
JOIN localizacoes l ON ch.id_central = l.central_id
JOIN concessoes c ON ch.id_central = c.central_id
ORDER BY dt.potencia_instalada_mw DESC
LIMIT 10;
```

---

## ✅ Checklist de Implementação

- [ ] Criar base de dados PostgreSQL com PostGIS
- [ ] Executar script SQL de criação (tabelas, índices, constraints)
- [ ] Definir políticas de backup e replicação
- [ ] Implementar API REST para consultas (ex: usando PostgREST)
- [ ] Criar dashboards de visualização (ex: Grafana, Tableau)
- [ ] Automatizar importação de dados do SNIRH (API/Web scraping)
- [ ] Validar integridade de dados (duplicatas, missing values)
- [ ] Documentar dicionário de dados (data dictionary)
- [ ] Treinar utilizadores finais
- [ ] Estabelecer calendário de atualização mensal/semanal

---

## 📝 Notas Importantes

1. **Modelo Relacional**: As 6 tabelas evitam redundância e permitem atualizações independentes
2. **PostGIS**: Permite análises geoespaciais avançadas (buffer, nearest neighbor, etc.)
3. **Índices**: Essenciais para performance com grandes volumes de dados
4. **Time Series**: A tabela `monitorizacao_operacional` pode armazenar histórico contínuo
5. **Auditoria**: Campos `data_criacao` e `data_atualizacao` rastreiam mudanças