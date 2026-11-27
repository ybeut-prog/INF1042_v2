import pandas as pd

df = pd.read_csv("basket.csv")

top_10 = df.nlargest(10, "salary")

print(top_10[["Team", "salary"]])
