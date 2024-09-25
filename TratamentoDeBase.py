import pandas as pd
import os
import re

def arruma_col_int(x):
        if pd.isna(x):
            return 0
        x = str(x).replace(',', '.')
        x = re.sub(r'[^\d.]', '', x) 
        try:
            return int(float(x)) 
        except ValueError:
            return 0

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

    path = 'Caminho com diversas bases para leitura e tratamento'

    string_int = ['Coluna_Int1', 'Coluna_Int2']

    string_float = ['Coluna_float1', 'Coluna_float2']

    df = pd.DataFrame()

    for file in os.listdir(path) :
        print(path + file)
        chunk = pd.read_csv(path + file, chunksize=1000000, low_memory=False)
        frame = pd.concat(chunk)
        df = pd.concat([df, frame], ignore_index=True)    

    df['Coluna_GRUPO'] = 'GRUPO SELECIONADO'

    df.dropna(subset= 'Coluna_ID', inplace=True)    

    df[string_int] = df[string_int].applymap(arruma_col_int)

    df[string_float] = df[string_float].applymap(arruma_col_float)

    df['Data'] = pd.to_datetime(df['Data'])
    df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')

    subgrupos = {
        'subgrupo1':'Sub_Grupo_1',
        'subgrupo2':'Sub_Grupo_2',
        'subgrupo3':'Sub_Grupo_3'
    }

    df['Coluna_Sub_Grupo'] = df['Coluna_Sub_Grupo'].replace(subgrupos)

    base_tratada = df[[
            'Coluna_ID',
            'Coluna_float1', 
            'Coluna_float2', 
            'Coluna_Int1', 
            'Coluna_Int2',
            'Coluna_GRUPO',
            'Coluna_Sub_Grupo',
            'Data'
            ]]
    
    return base_tratada       
