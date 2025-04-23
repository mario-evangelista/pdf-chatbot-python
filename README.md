# 📚 Chatbot Acadêmico Baseado em PDFs

## 🎯 Objetivo

Este projeto cria um chatbot inteligente capaz de responder perguntas com base no conteúdo de artigos científicos e documentos em PDF. Ideal para pesquisadores e estudantes que precisam extrair informações de múltiplos artigos acadêmicos.

## ✨ Funcionalidades Principais

- 📤 Upload de múltiplos arquivos PDF simultaneamente
- 🔍 Processamento e indexação inteligente do conteúdo
- 💬 Respostas contextualizadas baseadas nos documentos
- 🚀 Interface amigável desenvolvida com Streamlit
- ⚡ Busca vetorial eficiente usando FAISS

## 🛠️ Tecnologias Utilizadas

- **LangChain** - Framework para aplicações com modelos de linguagem
- **OpenAI** - Modelos de IA para geração de respostas
- **FAISS** - Biblioteca para busca vetorial eficiente
- **PyPDF** - Extração de texto de arquivos PDF
- **Streamlit** - Interface web intuitiva

## 📥 Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI (para API key)

### Passo a Passo

1. Clone o repositório:
```bash
git clone https://github.com/mario-evangelista/pdf-chatbot-python.git
cd pdf-chatbot
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` e adicione sua API key:
```env
OPENAI_API_KEY=sua_chave_aqui
```

4. Execute a aplicação:
```bash
streamlit run app.py
```

5. Acesse no navegador:
```
http://localhost:8501
```

## 🗂️ Estrutura do Projeto

```
pdf-chatbot/
├── inputs/               # Pasta para documentos de exemplo
├── app.py               # Código principal da aplicação
├── requirements.txt     # Dependências do projeto
├── .env                 # Configurações de ambiente
└── README.md            # Este arquivo
```

## 📌 Exemplo de Uso

1. Faça upload de um ou mais artigos científicos em PDF
2. Aguarde o processamento dos documentos (pode levar alguns segundos)
3. Faça perguntas sobre o conteúdo dos artigos
4. Receba respostas precisas baseadas no texto dos documentos

## 🔍 Insights Técnicos

- **Segmentação de Texto**: O texto é dividido em chunks de 1000 caracteres com overlap de 200 para manter o contexto
- **Embeddings**: Usamos embeddings da OpenAI para representação semântica do texto
- **Busca Vetorial**: FAISS permite buscas eficientes mesmo em grandes conjuntos de documentos
- **Cadeia de QA**: Combinação de retrieval + geração para respostas precisas

## 📈 Próximas Melhorias

- [ ] Adicionar referências às páginas dos PDFs nas respostas
- [ ] Implementar histórico de conversas
- [ ] Suporte a outros formatos (DOCX, TXT)
- [ ] Opção para salvar sessões de pesquisa
- [ ] Deploy como aplicação web pública

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch com sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## ✉️ Contato

Mário Evangelista - [marioevangelista](https://www.linkedin.com/in/marioevangelista) - mariojbe@gmail.com

Link do Projeto: [https://github.com/mario-evangelista/pdf-chatbot-python](https://github.com/mario-evangelista/pdf-chatbot-python)
