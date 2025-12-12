# Master Dashboard - Hidroelétricas Portugal

Este repositório contém um dashboard interativo que unifica dados das centrais hidroelétricas em Portugal, combinando informações oficiais da APA (Agência Portuguesa do Ambiente) com dados geoespaciais e técnicos do OpenInfraMap (OpenStreetMap).

## 🌍 Visão Geral

O projeto tem como objetivo facilitar a visualização e análise das concessões hidroelétricas, permitindo:
- **Visualização Geoespacial**: Mapa interativo com a localização das centrais.
- **Análise Temporal**: Timeline de expiração das concessões.
- **Detalhes Técnicos**: Capacidade instalada, operador, bacia hidrográfica e finalidade.
- **Comparação de Fontes**: Distinção visual entre dados confirmados (APA+OpenInfraMap) e dados apenas do OpenInfraMap.

👉 **[Ver Dashboard Online](https://<seu-utilizador>.github.io/<nome-do-repo>)** (Substitua pelo seu link após deploy)

## 🛠️ Tecnologias Usadas

- **HTML5/CSS3/JavaScript**: Frontend leve e rápido (sem frameworks pesados).
- **Leaflet.js**: Para o mapa interativo.
- **Chart.js**: Para os gráficos estatísticos.
- **Python**: Para extração, limpeza e injeção de dados (ETL).

## 📂 Estrutura do Projeto

- `index.html`: O dashboard principal (Single Page Application).
- `AH_Master_Merged.csv`: A base de dados Mestra unificada.
- `scripts/`: Scripts Python auxiliares (`merge_hydro_data.py`, `inject_master_data.py`).

## 🚀 Como Atualizar os Dados

1. Executar `python inject_master_data.py` para atualizar o JSON dentro do `index.html` com base no CSV mais recente.
2. Fazer o commit e push das alterações para o GitHub.

## 📝 Fontes de Dados

- **APA**: Lista de Aproveitamentos Hidráulicos.
- **OpenInfraMap/Overpass API**: Dados geoespaciais e técnicos do OpenStreetMap.

---
*Gerado com assistência de AI Agent (Google Deepmind)*
