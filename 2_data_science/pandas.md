
- Visualizar as colunas do DF: ```df.columns.values```

- Descreve a informação agrupada por grupo especificado:  ```df.groupby('VALOR PARCELA').describe()```

- retorna uma serie com a contagem dos valores únicos:  ```df['NOME MUNICÍPIO'].value_counts()```



- Quantidade de Pagamentos em cada cidade e ordena pelo indice
```bash 
df['NOME MUNICÍPIO'].value_counts().sort_index()
``

df['NOME MUNICÍPIO'].sum()

col_municipio=df['NOME MUNICÍPIO']

df = df.sort_values('VALOR PARCELA', ascending=False)









