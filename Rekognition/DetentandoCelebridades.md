# AWS Rekognition - Detectando Celebridades em Imagens

## Estrutura do Projeto

```
aws-rekognition-celebridades/
│-- src/
│   │-- detecta_celebridades.py  # Código principal para detecção
│   │-- utils.py  # Funções auxiliares
│-- tests/
│   │-- test_detecta_celebridades.py  # Testes unitários
│-- exemplos/
│   │-- imagem1.jpg  # Imagens de exemplo
│   │-- imagem2.jpg
│-- README.md  # Documentação do projeto
│-- requirements.txt  # Dependências do projeto
```

## Código Principal (src/detecta_celebridades.py)

```python
import boto3
import json

def detecta_celebridades(imagem_caminho):
    client = boto3.client('rekognition')
    
    with open(imagem_caminho, 'rb') as imagem:
        resposta = client.recognize_celebrities(Image={'Bytes': imagem.read()})
    
    celebridades = []
    for celebridade in resposta.get('CelebrityFaces', []):
        celebridades.append({
            'Nome': celebridade['Name'],
            'Confiança': celebridade['MatchConfidence']
        })
    
    return celebridades

if __name__ == "__main__":
    imagem_teste = "../exemplos/imagem1.jpg"
    resultado = detecta_celebridades(imagem_teste)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
```

## Exemplo de Uso

### Entrada:
Imagem contendo celebridades.

### Saída:
```json
[
  {
    "Nome": "Brad Pitt",
    "Confiança": 99.5
  },
  {
    "Nome": "Angelina Jolie",
    "Confiança": 98.7
  }
]
```

## Teste Unitário (tests/test_detecta_celebridades.py)

```python
import unittest
from src.detecta_celebridades import detecta_celebridades

class TestDetectaCelebridades(unittest.TestCase):
    def test_detecta_celebridades(self):
        imagem_teste = "../exemplos/imagem1.jpg"
        resultado = detecta_celebridades(imagem_teste)
        self.assertIsInstance(resultado, list)
        self.assertTrue(all('Nome' in celeb and 'Confiança' in celeb for celeb in resultado))

if __name__ == "__main__":
    unittest.main()
```

## Exemplos de Aplicação
1. **Segurança e Controle de Acesso**: Empresas podem usar esta tecnologia para detectar celebridades e verificar identidades em eventos exclusivos.
2. **Engajamento em Redes Sociais**: Aplicativos podem identificar e marcar automaticamente celebridades em fotos, otimizando a experiência dos usuários.

## Instalação e Uso

1. Instale as dependências:
   ```bash
   pip install boto3
   ```

2. Configure as credenciais AWS:
   ```bash
   aws configure
   ```

3. Execute a detecção:
   ```bash
   python src/detecta_celebridades.py
