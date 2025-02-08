# 📘 Projeto: Extração de Texto de Imagens com AWS Textract usando Python  

## 📋 Descrição
Este projeto utiliza o serviço **AWS Textract** para extrair texto de imagens de documentos. O código foi desenvolvido em Python e pode ser usado para automatizar o processamento de documentos digitalizados, como recibos, contratos e certificados.

---

## 🔧 Estrutura do Projeto
```
aws-textract-project/
│
├── main.py               # Código principal para executar a extração de texto
├── requirements.txt      # Bibliotecas necessárias para o projeto
├── config.py             # Configurações do projeto (como credenciais AWS)
├── samples/              # Pasta com exemplos de imagens para teste
├── output/               # Pasta para armazenar resultados das extrações
└── README.md             # Documentação do projeto
```

---

## 📦 Passos para Configuração do Projeto

1. **Configurar AWS CLI e Textract**
   - Crie uma conta AWS (se ainda não tiver).
   - Configure as credenciais usando o AWS CLI (`aws configure`).
   - Garanta que o serviço Textract esteja habilitado.

2. **Instalar Bibliotecas Necessárias**
   Execute o seguinte comando no terminal para instalar as bibliotecas:
   ```bash
   pip install boto3 pillow
   ```

3. **Adicionar Imagens para Teste**
   Coloque as imagens de exemplo na pasta `samples/`.

---

## 🔍 Exemplo de Uso

### Entrada
Imagem (`exemplo.jpg`) contendo o seguinte texto:
```
Certificado de Participação  
Fulano de Tal participou do curso de Programação em Python  
Data: 01/01/2025  
```

### Saída (`output/resultado.txt`)
```
Certificado de Participação
Fulano de Tal participou do curso de Programação em Python
Data: 01/01/2025
```

---

## 🌍 Casos de Uso na Vida Real

### 1. **Automatização de Processamento de Documentos**
Empresas podem usar esta solução para automatizar a digitalização e extração de informações de recibos, contratos e documentos fiscais, eliminando a necessidade de inserção manual de dados.

### 2. **Análise de Documentos Jurídicos**
Advogados podem utilizar este projeto para analisar documentos jurídicos, extrair texto e buscar termos específicos em grandes volumes de arquivos digitalizados.

---

## 💡 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuprojeto/aws-textract-project.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script principal:
   ```bash
   python main.py
   ```

---

## 📂 Arquivo `requirements.txt`
```
boto3
pillow
```

---
