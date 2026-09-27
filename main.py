'''
NumPy Stats Analyzer

Uma ferramenta de linha de comando para realizar análises estatísticas básicas em um arquivo CSV.
'''

import numpy as np
import argparse

def analyse_data(file_path):
    '''
    Carrega dados de um arquivo CSV e calcula estatística descritivas.
    
    Args:
        file_path (str): O caminho para o arquivo CSV.
        
    Returns:
        None. Imprime os resultado diretamente no console.
    '''
    
    try:
        # Carrega os dados do CSV, pulando a primeira linha (cabeçalho)
        # O delimitador é a vígula.
        data = np.loadtxt(file_path, delimiter = ',', skiprows = 1)
        
        # Carrega o cabeçalho para usar nos prints
        header = np.genfromtxt(file_path, delimiter = ',', dtype = str, max_rows = 1)
        
        print(f'Análise do arquivo: {file_path}\n')
        print('-' * 40)
        
        # Itera sobre cada coluna (axis = 0)
        for i, column_name in enumerate(header):
            column_data = data[:, i]
            
            mean = np.mean(column_data)
            median = np.median(column_data)
            std_dev = np.std(column_data)
            min_val = np.min(column_data)
            max_val = np.max(column_data)
            count = len(column_data)
            
            print(f'Estatística para a coluna: "{column_name}"')
            print(f'    - Total de elementos:   {count}')
            print(f'    - Méida:                {mean:.2f}')
            print(f'    - Mediana:              {median:.2f}')
            print(f'    - Desvio Padrão:        {std_dev:.2f}')
            print(f'    - Mínimo:               {min_val:.2f}')
            print(f'    - Máximo:               {max_val:.2f}')
            print('-' * 40)
    
    except FileNotFoundError:
        print(f'Erro: O arquivo "{file_path}" não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
        
if __name__ == '__main__':
    # Configura o parser de argumentos de linha de comando
    parser = argparse.ArgumentParser(description = 'Analisa um arquivo CSV usando NumPy.')
    parser.add_argument('file_path', type = str, help = 'O caminho para o arquivo CSV a ser analisado.')
    
    args = parser.parse_args()
    
    # Chama a função principal com o caminho do arquivo fornecido
    analyse_data(args.file_path)