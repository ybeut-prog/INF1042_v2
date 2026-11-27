import pandas as pd

df = pd.read_csv("basket.csv")


players_by_country = df.groupby(
    ["Team", "country"]
).size().unstack(fill_value=0)

print(players_by_country)
