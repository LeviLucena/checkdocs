<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Badge" />
  </a>
  <a href="https://flask.palletsprojects.com/en/2.3.x/">
    <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask Badge" />
  </a>
  <a href="https://openai.com/">
    <img src="https://img.shields.io/badge/-OpenAI-000000?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Badge" />
  </a>
  <a href="https://getbootstrap.com/">
    <img src="https://img.shields.io/badge/-Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white" alt="Bootstrap Badge" />
  </a>
  <a href="https://pdfplumber.readthedocs.io/en/latest/">
    <img src="https://img.shields.io/badge/-pdfplumber-000000?style=flat-square&logo=python&logoColor=white" alt="pdfplumber Badge" />
  </a>
  <a href="https://pytesseract.readthedocs.io/en/latest/">
    <img src="https://img.shields.io/badge/-pytesseract-000000?style=flat-square&logo=python&logoColor=white" alt="pytesseract Badge" />
  </a>
  <a href="https://python-docx.readthedocs.io/en/latest/">
  <img src="https://img.shields.io/badge/-python--docx-3776AB?style=flat-square&logo=python&logoColor=white" alt="python-docx Badge" />
  </a>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/306c0712-60dc-4d10-98ea-1608c8accc9f">
</p>

## 📜 Descrição
Este projeto é um aplicativo web desenvolvido com Flask, que permite a análise de documentos de edital e atestados utilizando inteligência artificial. O sistema extrai texto de arquivos PDF, Word, TXT e imagens, e compara os conteúdos conforme critérios específicos definidos no edital.

![image](https://github.com/user-attachments/assets/64871cc7-b6e6-4c35-8c3b-d1ea58e79b3d)

## Funcionalidades

- 📤 **Upload de Documentos**: Permite o envio de um edital e múltiplos atestados.
- 📝 **Extração de Texto**: Utiliza bibliotecas como `pdfplumber`, `pytesseract` e `python-docx` para extrair texto de diferentes tipos de arquivos.
- 🤖 **Análise com IA**: Integra com a API da OpenAI para realizar análises detalhadas dos documentos, verificando conformidade com os critérios especificados.
- 🖥️ **Interface Intuitiva**: Interface simples e responsiva para facilitar o upload e visualização dos resultados.

## Tecnologias Utilizadas

- 🔥 **Flask**: Framework web para Python.
- 🌐 **OpenAI API**: Para análise de texto utilizando IA.
- 📄 **pdfplumber**: Para extração de texto de arquivos PDF.
- 🖼️ **pytesseract**: Para extração de texto de imagens.
- 📑 **python-docx**: Para manipulação de arquivos Word.

## Requisitos

- 🐍 Python 3.x
- ⚙️ Flask
- 🖊️ pytesseract
- 📖 pdfplumber
- 📃 python-docx
- 🔑 openai
- 📸 PIL (Pillow)

## Instalação

1. Clone o repositório:
```
   git clone https://github.com/LeviLucena/checkdocs.git
   cd checkdocs
 ```

2. Crie um ambiente virtual e ative-o:
```
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
 ```
3. Instale as dependências:
```
pip install -r requirements.txt
 ```
4. Configure o caminho do Tesseract no arquivo app.py:
```
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ajuste conforme necessário
```
5. Substitua a chave da API OpenAI no arquivo app.py de forma segura.

## Execução
Para iniciar o aplicativo, execute:
```
python app.py
```

O aplicativo estará disponível em ```http://127.0.0.1:5000.```

## Como Usar
- Acesse a aplicação em seu navegador.
- Carregue o arquivo do edital e os atestados.
- Clique no botão para analisar os documentos.
- Os resultados da análise serão exibidos na tela.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.
