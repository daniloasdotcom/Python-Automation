import os

# define o caminho da pasta que deseja acessar
pasta = 'C:/Users/Usuário/Downloads/Microbiologia/MicroGeral'

# lista todos os arquivos na pasta
arquivos = os.listdir(pasta)

# percorre todos os arquivos na pasta
for arquivo in arquivos:
    # verifica se o arquivo é um arquivo PDF
    if arquivo.endswith('.pdf'):
        # define o novo nome do arquivo removendo os 5 primeiros dígitos do nome atual
        novo_nome = arquivo[13:]
        # define o caminho completo do arquivo antigo e novo
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        # renomeia o arquivo
        os.rename(caminho_antigo, caminho_novo)
