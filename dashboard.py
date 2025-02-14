import streamlit as st
import pandas as pd
import os

# Caminho do arquivo de progresso
CSV_FILE = "progresso_aprendizado.csv"

# Definição dos tópicos detalhados
topicos = {
    "Área": [
        "Fundamentos de Programação em Python",
        "Fundamentos de Programação em Python",
        "Fundamentos de Programação em Python",
        "Fundamentos de Programação em Python",
        "Fundamentos de Programação em Python",
        "Inteligência Artificial e Machine Learning",
        "Inteligência Artificial e Machine Learning",
        "Inteligência Artificial e Machine Learning",
        "Inteligência Artificial e Machine Learning",
        "Inteligência Artificial e Machine Learning",
        "Agentes Inteligentes e Aplicações Web com LLMs",
        "Agentes Inteligentes e Aplicações Web com LLMs",
        "Agentes Inteligentes e Aplicações Web com LLMs",
        "Agentes Inteligentes e Aplicações Web com LLMs",
        "Desenvolvimento Web para Aplicações de IA",
        "Desenvolvimento Web para Aplicações de IA",
        "Desenvolvimento Web para Aplicações de IA",
        "Desenvolvimento Web para Aplicações de IA",
        "APIs, RAG e GraphRAG",
        "APIs, RAG e GraphRAG",
        "APIs, RAG e GraphRAG",
        "APIs, RAG e GraphRAG",
    ],
    "Tópico": [
        "Sintaxe, variáveis, estruturas de controle",
        "Estruturas de dados (listas, dicionários, tuplas, conjuntos)",
        "Programação orientada a objetos (OOP)",
        "Manipulação de arquivos e expressões regulares",
        "Bibliotecas essenciais: numpy, pandas, matplotlib",
        "Fundamentos de aprendizado de máquina",
        "Modelos supervisionados e não supervisionados",
        "Redes neurais e deep learning",
        "Bibliotecas essenciais: scikit-learn, tensorflow, pytorch",
        "Engenharia de features e tuning de modelos",
        "Large Language Models (GPT-4, Claude, Mistral)",
        "Retrieval-Augmented Generation (RAG) para personalização",
        "Integração de APIs de LLMs (OpenAI, Hugging Face, LangChain)",
        "Aplicações de IA para processamento de documentos jurídicos",
        "Backend: FastAPI, Flask, Django",
        "Frontend: React.js, Next.js (para interfaces interativas)",
        "Bancos de dados: PostgreSQL, MongoDB, Pinecone para RAG",
        "Segurança e autenticação (OAuth, JWT)",
        "Construção e consumo de APIs REST e GraphQL",
        "RAG (Recuperação aumentada por geração) para melhorar precisão",
        "GraphRAG para estruturar a recuperação de dados",
        "Técnicas de indexação e busca vetorial (ChromaDB, Weaviate)"
    ],
    "Total Tarefas": [10] * 22,  # Define 10 tarefas por tópico (pode ser ajustado)
    "Tarefas Concluídas": [0] * 22  # Inicialmente todas zeradas
}

# Se o arquivo CSV não existir, cria com valores padrão
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(topicos)
    df.to_csv(CSV_FILE, index=False)
else:
    df = pd.read_csv(CSV_FILE)

# Título
st.title("📊 Painel de Progresso - Aprendizado IA Jurídica")

# Seção para atualização do progresso
st.sidebar.header("✅ Atualize seu Progresso")
for i, row in df.iterrows():
    novo_valor = st.sidebar.slider(
        f"{row['Tópico']} ({row['Tarefas Concluídas']}/{row['Total Tarefas']})",
        0, row["Total Tarefas"], row["Tarefas Concluídas"]
    )
    df.at[i, "Tarefas Concluídas"] = novo_valor

# Calcular progresso em porcentagem
df["Progresso (%)"] = (df["Tarefas Concluídas"] / df["Total Tarefas"]) * 100

# Salvar progresso no CSV
df.to_csv(CSV_FILE, index=False)

# Exibir Tabela Formatada
st.write("### 📋 Progresso Detalhado")
st.dataframe(df)

# Gráfico de progresso por área
st.write("### 📈 Progresso por Área de Estudo")
progress_area = df.groupby("Área")["Progresso (%)"].mean()
st.bar_chart(progress_area)