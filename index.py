import pandas as pd

filepath = './diagnostico_estatistico_phyil.csv'

df = pd.read_csv(filepath, sep=';', decimal=',')

# 1 - Acessando as primeiras 10 linhas do DataFrame
#print(df.head(10))

# 2 - Filtrando o DataFrame para exibir apenas as linhas onde o Status seja "Significativo ✅"
#df_significativo = df.query('Status == "Significativo ✅"')

# 3 - exibindo o tamanho do DataFrame Significativo
#print(df_significativo.shape)

# 4 - Identificando qual classificador teve o maior número de resultados significativos
# O método value_counts() conta a frequência de cada valor na coluna "Clf" do DataFrame df_significativo e retorna uma série ordenada com os valores únicos e suas contagens. O método head(1) é usado para exibir apenas o primeiro resultado, que corresponde ao classificador com o maior número de resultados significativos.   
#df_significativo_counts = df_significativo["Clf"].value_counts()
#print(df_significativo_counts.head(1))

#Agrupando os Dados por Classificador e calculando a média dos ganhos
print(df.groupby("Clf")[['Ganho %', 'Ganho relativo %']].mean())

df_ordenado = df.sort_values(by=['Ganho %', 'Ganho relativo %'], ascending=False)
