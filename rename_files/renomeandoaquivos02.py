import os

# define o caminho da pasta que deseja acessar
pasta = 'C:/Users/Usuário/Downloads/ArtigosAlicia'

# lista todos os arquivos na pasta
arquivos = os.listdir(pasta)

# percorre todos os arquivos na pasta
for arquivo in arquivos:
    # verifica se o arquivo é um arquivo PDF e começa com "nexojornal.com.br-"
    if arquivo.endswith('.pdf') and arquivo.startswith('nexojornal.com.br-'):
        # define o novo nome do arquivo removendo o trecho "nexojornal.com.br-" do nome atual
        novo_nome = arquivo.replace('nexojornal.com.br-', '')
        # define o caminho completo do arquivo antigo e novo
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        # renomeia o arquivo
        os.rename(caminho_antigo, caminho_novo)
