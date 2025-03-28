import pdfplumber
import pandas as pd
import zipfile
import os


#
def extract_table_from_pdf(pdf_path):
    print("Extraindo os dados da tabela Rol de Procedimentos e Eventos em Saúde do PDF do Anexo I")
    all_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    all_data.append(row)
    df = pd.DataFrame(all_data[1:], columns=all_data[0])
    print("Dados extraídos com sucesso de todas as páginas do PDF.")
    return df



def replace_abbreviations(df):
    print("Substituindo as abreviações OD e AMB ")
    df = df.replace({
        'OD': 'Odontológica',
        'AMB': 'Ambulatorial'
    })
    return df

def compress_csv(csv_file, zip_file):
    print("Compactando o arquivo csv em um ZIP")
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_file, os.path.basename(csv_file))  # Adiciona o CSV no ZIP


pdf_path = "anexo_1.pdf"

data_frame = extract_table_from_pdf(pdf_path)

data_frame = replace_abbreviations(data_frame)

csv_filename = "rol_procedimentos_eventos_completo.csv"
data_frame.to_csv(csv_filename, index=False)

# Definir o nome do arquivo ZIP (substitua "{seu_nome}" com o seu nome real)
zip_filename = "Teste_Luis_Gustavo.zip"

compress_csv(csv_filename, zip_filename)

print(f"O arquivo CSV foi compactado com sucesso em {zip_filename}.")