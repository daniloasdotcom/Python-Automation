from fpdf import FPDF
import os

# Criar uma instância de FPDF e definir os parâmetros do documento
pdf = FPDF(unit="pt", format=[660, 610])

# Caminho para a pasta que contém as imagens
folder_path = 'D:/prog/agroSurvey/captura/Parafinalizar'

# Iterar por todos os arquivos na pasta especificada
for image_file in os.listdir(folder_path):
    if image_file.endswith(".png"):  # Verifica se o arquivo é uma imagem PNG
        pdf.add_page()
        image_path = os.path.join(folder_path, image_file)
        pdf.image(image_path, x=0, y=0, w=660, h=610)  # Adiciona a imagem ajustando ao tamanho da página

# Salvar o PDF
output_pdf_path = 'arquivo02.pdf'
pdf.output(output_pdf_path)

print(f'PDF criado com sucesso: {output_pdf_path}')

print(f'PDF criado com sucesso: {output_pdf_path}')






