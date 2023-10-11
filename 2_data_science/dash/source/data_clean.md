
# Limpando Dados 

### DataFrame.shape - mostra a dimensão do DataFrame  em linha e colunas
```DataFrame.shape```

### drop_duplicates() - remover registros duplicados de um Data Frame
```DataFrame.drop_duplicates()```


### value_counts() - mostra e conta valores únicos de uma coluna
```DataFrame['Nacionalidade'].value_counts()```

Nota: O mesmo pode ser conseguido usando as cláusulas "Distinct", "Count" e "Group By".

### IsNull() - registros com valores nulos
Para mostrar todos os registros com valor nulo na coluna "Nacionalidade"
```DataFrame[pd.isnull(dataFile['Nacionalidade'])]```

### dropna() - Limpar os NaN
```DataFrame.dropna()```

