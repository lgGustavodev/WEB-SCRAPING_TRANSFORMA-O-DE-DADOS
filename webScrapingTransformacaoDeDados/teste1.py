import requests
from bs4 import BeautifulSoup
import zipfile


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)

if response.status_code == 200:
    print("Página Acessada Com Sucesso!!!")
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', class_='internal-link')

    pdf_files = []
    pdf_count = 0

    for link in links:
        href = link.get('href')
        if href and href.endswith('.pdf'):
            pdf_url = href if href.startswith('http') else f"https://www.gov.br{href}"
            pdf_response = requests.get(pdf_url)

            if pdf_response.status_code == 200:
                pdf_count += 1
                pdf_name = f"anexo_{pdf_count}.pdf"
                with open(pdf_name, "wb") as pdf_file:
                    pdf_file.write(pdf_response.content)
                pdf_files.append(pdf_name)
                print(f"Download do Anexo {pdf_count} realizado com sucesso!")
            else:
                print(f"Erro ao baixar o Anexo {pdf_count}.")

            if pdf_count == 2:
                break

    if pdf_files:
        with zipfile.ZipFile("anexos.zip", "w") as zipf:
            for pdf in pdf_files:
                zipf.write(pdf)
        print("Todos os anexos foram compactados no arquivo 'anexos.zip' com sucesso!")
    else:
        print("Nenhum PDF foi baixado para compactação.")
else:
    print("Falha ao acessar a página.")
