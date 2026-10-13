# Calculadora de Risco de Câncer - INCA Brasil

**Uma ferramenta de análise de risco de câncer baseada nos dados do Instituto Nacional do Câncer (INCA) do Brasil.**

## 🚀 Características

- **Cálculo de risco por gênero e idade**
- **Risco acumulado de 5 e 10 anos**
- **Visualização com gráficos interativos**
- **Deploy fácil no Streamlit Community Cloud**

## 📂 Estrutura de Arquivos

```
📦 INCA-BR
 ┣ 📄 app.py                   # Aplicação Streamlit principal
 ┣ 📄 requirements.txt         # Dependências Python
 ┣ 📄 man.csv                  # Dados de risco masculino
 ┣ 📄 woman.csv                 # Dados de risco feminino
 ┣ 📄 README.md                # Este arquivo
```

## 🔧 Requisitos

- Python 3.10+
- Streamlit

## 🛠 Instalação

### 1. Criar ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar a aplicação

```bash
streamlit run app.py
```

Acesse em: `http://localhost:8501`

## 🎯 Como Usar

1. **Informe sua idade**
2. **Selecione seu gênero**
3. **Visualize o risco de câncer**
4. **Gráficos interativos mostram risco acumulado**

## 📤 Deploy no Streamlit

1. **Faça push para o GitHub**
2. **Acesse [Streamlit Community Cloud](https://share.streamlit.io/)**
3. **Selecione "New App" e escolha seu repositório**
4. **Clique em Deploy!**

## 📋 Cânceres Considerados (Base INCA)

### Masculino:
- Próstata
- Colorretal  
- Estômago
- Pulmão

### Feminino:
- Mama
- Colorretal
- Estômago

## 📜 Licença

MIT License - Sinta-se livre para usar e modificar.

## 🤝 Contribuições

Pull Requests bem-vindas!