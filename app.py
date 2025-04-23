import os
import openai
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import streamlit as st
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configuração da interface
st.title("📚 Chatbot de PDFs Acadêmicos")
st.write("Faça perguntas sobre seus artigos científicos e obtenha respostas baseadas no conteúdo!")

# Upload de PDFs
pdf_files = st.file_uploader("Carregue seus arquivos PDF", type="pdf", accept_multiple_files=True)

if pdf_files:
    # Processamento dos PDFs
    texts = []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    
    for pdf_file in pdf_files:
        # Salva temporariamente o arquivo
        with open(f"temp_{pdf_file.name}", "wb") as f:
            f.write(pdf_file.getbuffer())
        
        # Carrega e divide o PDF
        loader = PyPDFLoader(f"temp_{pdf_file.name}")
        pages = loader.load_and_split(text_splitter)
        texts.extend(pages)
        
        # Remove o arquivo temporário
        os.remove(f"temp_{pdf_file.name}")

    # Cria embeddings e vetorstore
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(texts, embeddings)
    
    # Cria a cadeia de QA
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    
    # Chat interativo
    st.write("## 💬 Chat com seus documentos")
    user_question = st.text_input("Faça sua pergunta sobre os artigos:")
    
    if user_question:
        answer = qa.run(user_question)
        st.write("**Resposta:**")
        st.write(answer)