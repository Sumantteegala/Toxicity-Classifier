import pandas as pd

df = pd.read_csv("jigsaw-toxic-comment-classification-challenge/train.csv",encoding='latin-1')

del df["id"]

print(df.head())
