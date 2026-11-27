import pandas as pd

df = pd.read_csv("basket.csv")


players_by_position = df["position"].value_counts()

print(players_by_position)
