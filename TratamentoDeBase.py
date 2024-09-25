import pandas as pd
import os
import re

#Utilização da Biblioteca RE, para pegar colunas Int selecionadas, retirar qualquer tipo de caractere especial e preencher cedulas nulas com 0

def arruma_col_int(x):
        if pd.isna(x):
            return 0
        x = str(x).replace(',', '.')
        x = re.sub(r'[^\d.]', '', x) 
        try:
            return int(float(x)) 
        except ValueError:
            return 0
                
#Utilização da Biblioteca RE, para pegar colunas Float selecionadas, retirar qualquer tipo de caractere especial e preencher cedulas nulas com 0

def arruma_col_float(x):
        if pd.isna(x) or x == '':
            return 0.0
        x = str(x).replace(',', '.')
        x = re.sub(r'[^\d.]', '', x)
        try:
            return float(x)
        except ValueError:
            return 0.0
        
def tratar_base():
        
        # Caminho para a leitura de uma pasta com diversas bases CSV que necessitam das tratativas
    path = 'Caminho com diversas bases para leitura e tratamento'

        # Colunas INT selecionadas para receber o tratamento
    string_int = ['Coluna_Int1', 'Coluna_Int2']

        # Colunas Float selecionadas para receber o tratamento
    string_float = ['Coluna_float1', 'Coluna_float2']

    df = pd.DataFrame()

        #Leitura da pasta por chunks para ficar mais leve e concatenação de todas as bases em um só DataFrame para melhor manipulação
    for file in os.listdir(path) :
        print(path + file)
        chunk = pd.read_csv(path + file, chunksize=1000000, low_memory=False)
        frame = pd.concat(chunk)
        df = pd.concat([df, frame], ignore_index=True)    

        #Filtro para seleção de grupo
    df['Coluna_GRUPO'] = 'GRUPO SELECIONADO'

        #Retirar cedulas nulas de colunas desejadas
    df.dropna(subset= ['Coluna_ID', 'Coluna_ID2'] inplace=True)    

              #Tratamento das colunas selecionadas para transformar elas em INT
    df[string_int] = df[string_int].applymap(arruma_col_int)

        #Tratamento das colunas selecionadas para transformar elas em Float
    df[string_float] = df[string_float].applymap(arruma_col_float)

        #Transformar uma coluna em tipo Data 
    df['Data'] = pd.to_datetime(df['Data'])

        #Renomeação de nomes de subgrupos caso encontrados no DataFrame
    subgrupos = {
        'subgrupo1':'Sub_Grupo_1',
        'subgrupo2':'Sub_Grupo_2',
        'subgrupo3':'Sub_Grupo_3'
    }

        #Aplicação das renomeações
    df['Coluna_Sub_Grupo'] = df['Coluna_Sub_Grupo'].replace(subgrupos)

        #Seleção e ordem das colunas na base
    base_tratada = df[[
            'Coluna_ID',
            'Coluna_ID2',
            'Coluna_float1', 
            'Coluna_float2', 
            'Coluna_Int1', 
            'Coluna_Int2',
            'Coluna_GRUPO',
            'Coluna_Sub_Grupo',
            'Data'
            ]]
    
    return base_tratada       
