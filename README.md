# 📊 Sales Dashboard Real-Time
> Dashboard de vendas em tempo real com streaming de dados, KPIs automáticos e alertas inteligentes

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Demo-FF4B4B?logo=streamlit)](https://streamlit.io)
[![Kafka](https://img.shields.io/badge/Apache_Kafka-Streaming-231F20?logo=apachekafka)](https://kafka.apache.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)](https://docker.com)
[![Demo](https://img.shields.io/badge/🚀_Demo-Online-00C851)](https://gabriel-sales-dashboard.streamlit.app)

## 🎯 Sobre

Dashboard de vendas com **atualização em tempo real** via Kafka. KPIs automáticos, gráficos interativos, alertas configuráveis e exportação de relatórios. Dados chegam do ERP/API e são exibidos sem refresh manual.

- 📡 Streaming em tempo real com Apache Kafka
- 📊 KPIs automáticos: receita, ticket médio, conversão, churn
- 🔔 Alertas configuráveis por threshold
- 📥 Exportação para PDF e Excel

## 🏗️ Arquitetura

```
ERP / API de Vendas
    └─► Kafka Producer
            └─► Kafka Topic: vendas
                    └─► Consumer (Python)
                            └─► PostgreSQL (histórico)
                                    └─► Streamlit (dashboard RT)
```

## 🛠️ Stack

| Componente | Tech |
|-----------|------|
| Streaming | Apache Kafka |
| Banco | PostgreSQL 16 |
| Dashboard | Streamlit + Plotly |
| Backend | FastAPI |
| Deploy | Docker Compose |

## 🚀 Rodando

```bash
git clone https://github.com/Kaique-ML/sales-dashboard-realtime
cd sales-dashboard-realtime

cp .env.example .env
docker compose up --build
# Dashboard: http://localhost:8501
```

## 📂 Estrutura

```
sales-dashboard-realtime/
├── dashboard/
│   ├── app.py                  # Streamlit principal
│   ├── kpis.py                 # Cálculo de KPIs
│   └── charts.py               # Gráficos Plotly
├── data/
│   ├── producer.py             # Kafka producer simulado
│   └── consumer.py             # Kafka consumer
├── tests/
│   └── test_kpis.py
├── docker-compose.yml
└── .env.example
```

## 📊 KPIs Monitorados

- 💰 Receita total (dia / semana / mês)
- 🎯 Taxa de conversão
- 🛒 Ticket médio
- 📦 Pedidos em aberto
- 📉 Produtos com queda de vendas > 20%

---
**Gabriel Kaique Portel Silva** | [LinkedIn](https://linkedin.com/in/gabriel-kaique-881475284) | [GitHub](https://github.com/Kaique-ML)
