from flask import Flask, request, jsonify, render_template
import pytesseract
import pdfplumber
import openai
import os
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Configuração do caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

# Substitua com sua chave da API OpenAI de forma segura
openai.api_key = 'SUA CHAVE API OPENAI AQUI'

def extract_text_from_file(file):
    file_type = file.content_type

    if 'pdf' in file_type:
        with BytesIO(file.read()) as f:
            pdf_text = ""
            with pdfplumber.open(f) as pdf:
                for page in pdf.pages:
                    pdf_text += page.extract_text() or ""
        return pdf_text

    elif 'word' in file_type:
        from docx import Document
        with BytesIO(file.read()) as f:
            doc = Document(f)
            doc_text = ""
            for para in doc.paragraphs:
                doc_text += para.text
        return doc_text

    elif 'plain' in file_type:
        return file.read().decode('utf-8')

    elif 'image' in file_type:
        img = Image.open(BytesIO(file.read()))
        return pytesseract.image_to_string(img, lang='por')

    else:
        raise ValueError('Tipo de arquivo não suportado.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'edital' not in request.files or 'atestados' not in request.files:
        return jsonify({'error': 'Faltando arquivos para análise'}), 400

    edital_file = request.files['edital']
    atestados_files = request.files.getlist('atestados')

    try:
        edital_text = extract_text_from_file(edital_file)
        atestados_texts = [extract_text_from_file(file) for file in atestados_files]

        # Construindo o prompt para análise
        messages = [
            {"role": "system", "content": "Você é um assistente que analisa documentos de edital e atestados para verificar a conformidade com critérios específicos."},
            {"role": "user", "content": f"""Analise o edital a seguir e determine se cada atestado atende aos critérios especificados. Compare cada atestado com os seguintes critérios e forneça uma avaliação detalhada para cada um:

Critérios a serem analisados:
1. Objeto: Identifique e trascreva o objeto da licitação e verifique se o atestado atende o que está no objeto do edital. Transcreva tanto o objeto do Edital quanto o objeto do atestado.
2. Critérios de Habilitação Técnica: Avalie se o atestado atende aos critérios de habilitação técnica e/ou qualificação técnica especificados no edital. Transcreva todos os itens dos critérios de habilitação técnica ou qualificação técnica especificadas no edital, e diga se aquele determinado item é atendido pelo atestado e informe o número da página do atestado que atende ao item citado.
3. Critérios Adicionais: Verifique se o atestado atende a outros critérios adicionais mencionados no edital.
4. Critérios do Fornecedor: Avalie se o atestado atende aos critérios relacionados ao fornecedor especificados no edital. Transcreva os itens referentes aos critérios ou requisitos do fornecedor, e diga se o atestado atende ao item e informe a página do atestado que atende ao item citado.
5. Requisitos: Verifique se o atestado cumpre todos os requisitos mencionados no edital. Transcreva os itens dos requisitos mencionados no edital, e diga se o atestado atende ao item e informe a página do atestado que atende ao item citado.
6. Metodologia: Avalie se o atestado segue a metodologia descrita no edital. Transcreva os itens mencionados no edital, e diga se o atestado atende ao item e informe a página do atestado que atende ao item citado.
7. Certificação: Verifique se o atestado possui as certificações necessárias conforme o edital. Transcreva as certificações necessárias, e diga se o atestado atende ao item e informe a página do atestado que atende ao item citado.
8. Parceria: Avalie se o atestado atende aos requisitos relacionados a parcerias mencionados no edital. Transcreva as parcerias requisitadas, e diga se o atestado atende ao item e informe a página do atestado que atende ao item citado.

Para cada atestado, faça a seguinte comparação:

{''.join(f'Comparação entre o Edital "{edital_file.filename}" e o Atestado "{atestados_files[i].filename}":\n' +
          f'Atestado {i+1}:\n{text}\n\n' for i, text in enumerate(atestados_texts))}

Forneça uma análise detalhada, comparando cada atestado com cada critério listado e explique se o atestado atende ou não aos critérios do edital. Adicione ✔️ para critérios atendidos e ❌ para critérios não atendidos."""}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=3000,
            temperature=0.5
        )

        result = response.choices[0].message['content'].strip()
        return jsonify({'result': result})

    except openai.error.OpenAIError as e:
        print(f"Erro na API OpenAI: {str(e)}")  # Log do erro da API
        return jsonify({'error': f'Erro na API OpenAI: {str(e)}'}), 500
    except Exception as e:
        print(f"Erro interno: {str(e)}")  # Log de erro interno
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
