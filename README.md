# Projeto de Web Scraping e Transformação de Dados

## Introdução
Este projeto foi desenvolvido para automatizar dois processos:
1. **Teste de Web Scraping**: Extração e download de arquivos PDF de uma página web específica.
2. **Teste de Transformação de Dados**: Manipulação e exportação de dados extraídos de PDFs para um arquivo CSV e compactação em formato ZIP.

## Funcionalidades

### **Teste 1: Web Scraping**
- Acessa uma página da web.
- Identifica links de PDFs listados na página.
- Realiza o download dos arquivos e os compacta em um único arquivo ZIP chamado `anexos.zip`.

### **Teste 2: Transformação de Dados**
- Extrai tabelas de arquivos PDF utilizando a biblioteca `pdfplumber`.
- Substitui abreviações como "OD" e "AMB" por seus respectivos significados completos.
- Exporta os dados tratados para um arquivo CSV chamado `rol_procedimentos_eventos_completo.csv`.
- Compacta o arquivo CSV em um ZIP chamado `Teste_Luis_Gustavo.zip`.

## Pré-requisitos

Certifique-se de que os seguintes pacotes estão instalados:
- **Bibliotecas Python**:
  - `pdfplumber`
  - `pandas`
  - `requests`
  - `BeautifulSoup4`
  - `click`
- **Módulos Nativos**:
  - `os`
  - `zipfile`

