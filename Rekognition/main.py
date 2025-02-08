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
