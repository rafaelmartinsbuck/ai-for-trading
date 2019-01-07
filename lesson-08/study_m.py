import pandas as pd
import numpy as np

df = pd.DataFrame({"A":[1,2,3,4], "B":[5,6,7,8], "c":[2,3,4,5]})
print(df)

def gen(df):
    df_cpy = df.copy()
    for index, row in df_cpy.iterrows():
        top = row.nlargest(1)
        row[:] = 0
        row[top.index] = 1
    return df_cpy

df_modify = gen(df)


df_mul = df * df_modify

print(df_modify)

print(df_mul)