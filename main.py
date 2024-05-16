import shutil
import os

def copy_word_file(source_path, dest_path):
    try:
        shutil.copyfile(source_path, dest_path)
        print("Arquivo copiado com sucesso!")
    except IOError as e:
        print(f"Erro ao copiar o arquivo: {e}")


def main():
    source_file = "C:/Users/Usuário/Desktop/Nível3.0/Rotina/Week21_2024.docx"  # Insira o caminho do seu arquivo Word aqui
    base_dest_path = "C:/Users/Usuário/Desktop/Arquivos"  # Insira o caminho do diretório onde os novos arquivos serão salvos aqui

    # Copiando o arquivo Week21_2024 para o destino
    copy_word_file(source_file, os.path.join(base_dest_path, "Week21_2024.docx"))

    # Criando os arquivos Week22_2024 até Week30_2024
    for week_number in range(22, 31):
        new_file_name = f"Week{week_number}_2024.docx"
        new_file_path = os.path.join(base_dest_path, new_file_name)
        copy_word_file(source_file, new_file_path)


if __name__ == "__main__":
    main()

