import pandas as pd

filepath = './diagnostico_estatistico_phyil.csv'

df = pd.read_csv(filepath, sep=';', decimal=',')

# 1 - Acessando as primeiras 10 linhas do DataFrame
#print(df.head(10))

# 2 - Filtrando o DataFrame para exibir apenas as linhas onde o Status seja "Significativo ✅"
df_significativo = df.query('Status == "Significativo ✅"')

# 3 - exibindo o tamanho do DataFrame Significativo
print(df_significativo.shape)

# 4 - Identificando qual classificador teve o maior número de resultados significativos
