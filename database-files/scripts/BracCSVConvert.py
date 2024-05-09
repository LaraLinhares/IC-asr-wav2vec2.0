import os
import csv
import re

# Pasta onde estão os arquivos de áudio
pasta_audio = '/home/lara/Área de Trabalho/codigos-ic/Braccent/Mono/Baiano/Feminino'

# Pasta onde está o arquivo de transcrições
pasta_transcricao = '/home/lara/Área de Trabalho/codigos-ic/transcricao'

# Lista para armazenar os nomes dos arquivos e transcrições
dados = []

# Regex para extrair o número da frase do nome do arquivo
regex_numero_frase = r'frase_(\d+)_'

# Percorre todos os arquivos da pasta de áudio
for nome_arquivo_audio in os.listdir(pasta_audio):
    caminho_arquivo_audio = os.path.join(pasta_audio, nome_arquivo_audio)
    
    # Verifica se o caminho é um arquivo de áudio (ignora pastas)
    if os.path.isfile(caminho_arquivo_audio):
        # Verifica se o nome do arquivo de áudio segue o padrão esperado
        if 'frase_' in nome_arquivo_audio:
            # Extrai o número da frase do nome do arquivo usando expressão regular
            match = re.search(regex_numero_frase, nome_arquivo_audio)
            if match:
                numero_frase = int(match.group(1))
        
                # Constrói o nome do arquivo de transcrição correspondente
                nome_arquivo_transcricao = f'transcricao-braccent_frase_{numero_frase}.txt'
                caminho_arquivo_transcricao = os.path.join(pasta_transcricao, nome_arquivo_transcricao)
        
                # Lê a transcrição correspondente
                with open(caminho_arquivo_transcricao, 'r') as arquivo_transcricao:
                    transcricao = arquivo_transcricao.read().strip()
        
                dados.append([nome_arquivo_audio, transcricao])
            else:
                print(f"Não foi possível extrair o número da frase do arquivo de áudio: {nome_arquivo_audio}")
        else:
            print(f"Nome de arquivo de áudio inválido: {nome_arquivo_audio}")

# Nome do arquivo CSV que será gerado
nome_arquivo_csv = 'braccentTesteBrac.csv'

# Cria o arquivo CSV e escreve os nomes dos arquivos e transcrições
with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv: 
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Audio', 'Transcricao'])  # Cabeçalho do CSV
    
    # Escreve cada nome de arquivo e transcrição em uma linha do CSV
    for dado in dados:
        escritor_csv.writerow(dado)

print(f'O arquivo CSV "{nome_arquivo_csv}" foi criado com sucesso!')
