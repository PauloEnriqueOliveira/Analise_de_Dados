# Analise de Dados

Este repositório tem com intuito mostrar funções do pandas para fazer refinações de bases, estudos, etc. Qualquer dúvida, sinta-se à vontade para me chamar no [linkedin](https://www.linkedin.com/in/paulo-oliveira-a6650121a/).

# Requesitos
- Python
- Pandas
- Jupyter

# Bibliotecas Utilizadas
- [Pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide) ;
- ? 

# Descrição sobre cada file
- ?
- ?
- ?
- ?

# Funções Base
## - Chamada da Biblioteca Pandas
O "import" nada mais é do que a chamada da biblioteca, "pandas" é a biblioteca que estamos chamando ao nosso código, “as pd” serve como abreviação para a chamada do pandas
~~~
import pandas as pd
~~~

## - Leitura de arquivos

O pd.read é utilizado para fazer a leitura da sua base, seja ela em csv, excel, parquet etc.
~~~
pd.read
~~~
Exemplo: “pd.read_csv(r”caminho”). O “r” antes do caminho é para uso do “raw string”, que ajuda a evitar problemas com barras invertidas “\” no caminho do arquivo.
~~~
pd.read_csv(r”caminho”)
~~~

## - Filtros na Leitura de Excel/CSV

### - Separador por caractere
sep: O “sep”, tem como função fazer a separação de colunas por um tipo de caractere específico, ex: sep=”,”.
~~~
pd.read_csv(r”caminho”, sep=";")
~~~

### - Seleção de Tabela
sheets: O “sheets” é utilizado para quando ocorrer do excel ter mais de uma tabela, usando o sheets você pode selecionar a tabela que preferir, ex: sheets=”tabela”.
~~~
pd.read_csv(r”caminho”, sheets="Tabela")
~~~

### - Low Memory
low_memory: O “low_memory”, tem como objetivo tirar as tratativas do excel deixando mais leve o arquivo, ex: low_memory=true.
~~~
pd.read_csv(r”caminho”, low_memory=true)
~~~

### - Seleção de quantidade de linhas
nrows: nrows tem como finalidade você definir quantas linhas ele vai ler do arquivo, com intuito de ficar mais rápida a leitura caso não queira ler a base inteira, ex: nrows=1
~~~
pd.read_csv(r”caminho”, nrows=x)
~~~

## - Definição de Dataframes

Neste exemplo a baixo fazemos a leitura de um csv, com ele eu faço a definição do meu dataframe como “df” e encaminho meu csv para este dataframe para manipularmos ele, sempre que ocorrer alguma alteração que você queira definir para seu dataframe sendo em filtros, retirada de colunas, etc você transforma em seu dataframe, sendo assim sempre que chamar apenas seu "df" você vai estar chamando o csv que você definiu e com as alterações feitas.
~~~
df = pd.read_csv(r”caminho”)
~~~

## - Comandos para serem utilizados no DataFrame

### - Seleção de linhas Iniciais do Dataframe
No comando “df.head()”, você faz a chamada das primeiras linhas do seu Dataframe, você pode estar inserindo um valor entre os parênteses para ele trazer o X de linhas que você quiser, caso não defina um valor ele vai trazer por padrão cinco linhas.
~~~
df.head()
~~~

### - Seleção de linhas finais do Dataframe
No comando “df.tail()”, você faz a chamada das últimas linhas do seu Dataframe, você pode estar inserindo um valor entre os parênteses para ele trazer o X de linhas que você quiser, caso não defina um valor ele vai trazer por padrão cinco linhas.
~~~
df.tail()
~~~

### - Tipo de coluna
Após a definição do dataframe, você pode estar usando “df.dtypes”, o dtypes tem como funcionalidade falar os tipos de cada coluna encontrada no seu dataframe.
~~~
df.dtypes
~~~

### - Nome das coluna
No comando “df.columns” estamos chamando as colunas do seu data frame, para você visualizar todas elas.
~~~
df.columns
~~~

### - Retirada de Colunas
No comando “df.drop(columns=[’coluna’])”, você retira a coluna desejada.
~~~
df.drop(columns=["coluna"])
~~~

### - Retirada de linhas nulas
No comando “df.dropna(subset=’coluna’])”, você retira qualquer linha que tiver a cédula da coluna selecionada nula, ou seja, se a coluna que eu selecionei tiver uma cédula nula na linha 38, a linha 38 inteira vai ser apagada do meu Dataframe.
~~~
df.dropna(subset=’coluna’])
~~~
Caso tenha preferência de retirar qualquer linha que tenha uma cédula nula, você pode apenas utilizar o comando “df.dropna()”.
~~~
df.dropna()
~~~

### - Retirada de duplicatas
No comando “df.drop_duplicates(subset=[‘coluna’])” você estará retirando qualquer outra linha que tenha o valor repetido dentro da coluna selecionada.
~~~
df.drop_duplicates(subset=["coluna"])
~~~
Caso tenha preferência de retirar linhas que são completamente duplicatas.
~~~
df.drop_duplicates()
~~~

### - Renomear Colunas
Para renomearmos colunas, podemos estar utilizando o comando, rename onde você seleciona a coluna que deseja mudar o nome e insere o novo nome dela.
~~~
df.rename(columns={‘coluna’: ‘coluna1’})
~~~

## - Filtros

### - Filtros por Valores
O comando “df[df[‘coluna’] == ‘valor’]”, vê a coluna em seu data frame escolhida e procura o valor ao qual você procura.
~~~
df[df[‘coluna’] == "valor"]
~~~
> [!NOTE]
> “>” : Filtro para valores acima do escolhido.
> 
> “<” : Filtro para valores acima do escolhido.
> 
> “==” : Filtro para valores iguais ao escolhido.
>
> "!=" : Filtro para valores diferentes do selecionado.
> 
> “>=” : Filtro para valores acima ou iguais.
> 
> “<=” : Filtro para valores menores ou iguais.

### - Filtros por Valores Nulos
Para fazer filtros de valores nulos você pode estar usando o comando “df[df[coluna].isna()]”;
~~~
df[df[coluna].isna()]
~~~

### - Filtros por Valores Não Nulos
Para fazer filtros de valores que não estão nulos você pode estar usando o comando “df[df['id'].notna()]”
~~~
df[df['coluna'].notna()]
~~~

## - Tratativas

### - Alterar tipo de coluna
Para fazermos mudanças do tipo de coluna e transformar números inteiros em strings, float em números inteiros etc, você pode estar usando o comando “df.astype({‘coluna’:’tipo’})".
~~~
df.astype({‘coluna’:’tipo’})
~~~

### - Preencher campos nulos
No comando “df.fillna({‘coluna’ : “exemplo”})”, você escolhe uma coluna e preenche todas as células nulas daquela coluna com um valor escolhido.
~~~
df.fillna({"coluna" : “exemplo”})
~~~
















