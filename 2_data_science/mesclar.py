prod=["iphone","ipad","airpod"]
prod_new=["apple_watch","macbook"]
prod.extend(prod_new)
print(prod)
print()


prod_dict={"iphone":700,"ipad":11000,"airpod":2500}
prod_new_dict={"apple_watch":3500,"macbook":15000}
prod_dict= prod_dict | prod_new_dict
print(prod_dict)
print()

# Dataframe
import pandas as pd

prod_dict={"iphone":700,"ipad":11000,"airpod":2500}
prod_new_dict={"apple_watch":3500,"macbook":15000}

# Dataframe
df = pd.DataFrame(prod_dict)
df.to_csv('preco_cadeira.csv', encoding='utf-8', sep=';')

quit()

prod = pd.DataFrame(prod_dict)
prod.to_csv('prod.csv', encoding='utf-8', sep=',')

new = pd.DataFrame(prod_new_dict)
new.to_csv('new.csv', encoding='utf-8', sep=',')

