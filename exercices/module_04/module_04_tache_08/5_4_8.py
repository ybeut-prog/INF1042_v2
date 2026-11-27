import pandas as pd

df = pd.read_csv("basket.csv")


salary_stats = df.groupby("position")["salary"].agg(
    ["mean", "max", "min"]
)

print(salary_stats)
