import boto3
import json
from PIL import Image
import io

# Função para extrair texto usando AWS Textract
def extract_text_from_image(file_path):
    client = boto3.client('textract')
    
    with open(file_path, 'rb') as image_file:
        image_bytes = image_file.read()
    
    response = client.detect_document_text(Document={'Bytes': image_bytes})
    extracted_text = ''
    
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            extracted_text += item['Text'] + '\n'
    
    return extracted_text

# Função principal para executar o projeto
def main():
    image_path = "samples/exemplo.jpg"  # Caminho da imagem de exemplo
    output_path = "output/resultado.txt"
    
    print("📂 Extraindo texto da imagem...")
    extracted_text = extract_text_from_image(image_path)
    
    with open(output_path, 'w') as output_file:
        output_file.write(extracted_text)
    
    print(f"✅ Extração concluída! O texto foi salvo em: {output_path}")
    print("Conteúdo extraído:")
    print(extracted_text)

if __name__ == "__main__":
    main()
