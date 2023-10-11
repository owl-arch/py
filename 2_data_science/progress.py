from tqdm.notebook import trange
from time import sleep
import pandas as pd
import numpy as np
from tqdm import tqdm

df = pd.DataFrame(np.random.randint(0, 100, (1000000, 100)))

tqdm.pandas(desc="power DataFrame 1M x 100 of random int!")

print('1')
df.progress_apply(lambda x: 1)
print('2')
df.groupby(0)[1].count().progress_apply(lambda x: 0)
print('3')


##
# https://www.kdnuggets.com/2022/09/progress-bars-python-tqdm-fun-profit.html
##

# progressive sleep function
def fun(x):
    sleep(0.1)
    return x


# progress loop
for i in tqdm(range(10)):
    fun(i)

print('4')

colors = ["Blue", "Green", "Yellow", "White", "Gray", "Black"]
for x in tqdm(colors):
    sleep(0.1)
    # print(x)


for i in trange(10, desc='Traning Model on 10 Epochs'):
    sleep(0.01)
    for x in trange(100, desc=f'Epoch {i}'):
        sleep(0.001)
