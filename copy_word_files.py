import shutil
import os


def main():
    base_file = "C:/Users/Usuário/Desktop/Nível3.0/Rotina/Week21_2024.docx"  # Insira o caminho do seu arquivo Word base aqui
    base_dest_path = "C:/Users/Usuário/Desktop/Arquivos"  # Insira o caminho do diretório onde os novos arquivos serão salvos aqui

    # Verificando se o arquivo base existe
    if not os.path.isfile(base_file):
        print("O arquivo base não foi encontrado.")
        return

    # Criando os arquivos Week22_2024 até Week30_2024 baseados no arquivo Week21_2024
    for week_number in range(22, 31):
        new_file_name = f"Week{week_number}_2024.docx"
        new_file_path = os.path.join(base_dest_path, new_file_name)
        shutil.copyfile(base_file, new_file_path)
        print(f"Arquivo {new_file_name} criado com sucesso!")


if __name__ == "__main__":
    main()

