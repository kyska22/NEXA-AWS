# AWS Rekognition - Detectando Celebridades em Imagens

## Introdução
Este projeto utiliza o serviço **AWS Rekognition** para detectar e identificar celebridades em imagens. A solução é desenvolvida em **Python** e explora a API do Rekognition para análise de imagens e etiquetagem automática de rostos reconhecidos.

## Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:
```
aws-rekognition-celebridades/
│-- src/
│   │-- rekognition.py  # Código principal para interação com AWS Rekognition
│   │-- utils.py        # Funções auxiliares
│-- tests/
│   │-- test_rekognition.py  # Testes unitários
│-- images/
│   │-- sample.jpg      # Imagens de exemplo
│-- README.md           # Documentação do projeto
│-- requirements.txt    # Dependências do projeto
```

## Pré-requisitos
1. Conta AWS ativa com permissões para o serviço **Rekognition**.
2. Chaves de acesso configuradas no perfil AWS CLI.
3. Python 3.x instalado.
4. Bibliotecas necessárias instaladas:
    ```sh
    pip install boto3 pillow
    ```

## Código Principal (`rekognition.py`)
```python
import boto3
import json

def detecta_celebridades(imagem_caminho):
    cliente = boto3.client('rekognition')
    
    with open(imagem_caminho, 'rb') as imagem:
        resposta = cliente.recognize_celebrities(Image={'Bytes': imagem.read()})
    
    celebridades = resposta.get('CelebrityFaces', [])
    resultado = []
    
    for celebridade in celebridades:
        resultado.append({
            'Nome': celebridade['Name'],
            'Confiança': celebridade['MatchConfidence']
        })
    
    return resultado

if __name__ == "__main__":
    caminho = "images/sample.jpg"
    resultado = detecta_celebridades(caminho)
    print(json.dumps(resultado, indent=4, ensure_ascii=False))
```

## Testes (`test_rekognition.py`)
```python
import unittest
from src.rekognition import detecta_celebridades

class TestRekognition(unittest.TestCase):
    def test_detecta_celebridades(self):
        imagem_teste = "images/sample.jpg"
        resultado = detecta_celebridades(imagem_teste)
        self.assertIsInstance(resultado, list)
        
if __name__ == "__main__":
    unittest.main()
```

## Exemplos de Entrada e Saída
### Entrada:
Imagem contendo rostos de celebridades, ex.: `images/sample.jpg`

### Saída:
```json
[
    {
        "Nome": "Leonardo DiCaprio",
        "Confiança": 99.2
    },
    {
        "Nome": "Angelina Jolie",
        "Confiança": 97.8
    }
]
```

## Casos de Uso
1. **Mídia e Entretenimento**: Empresas podem usar a ferramenta para identificar automaticamente celebridades em eventos, filmes e imagens publicadas online.
2. **Segurança e Monitoramento**: Pode ser usado em sistemas de vigilância para detectar e identificar celebridades ou pessoas de interesse em locais públicos.

## Conclusão
Este projeto demonstra como utilizar AWS Rekognition para detectar e etiquetar celebridades em imagens, aproveitando a API do serviço para criar soluções inovadoras em reconhecimento facial.

