import pandas as pd

df = pd.read_csv("basket.csv")


df["total_points"] = df["ppg"] * df["matches"]


df["cost_per_point"] = df["salary"] / df["total_points"]


df.loc[df["total_points"] == 0, "cost_per_point"] = float("inf")


top_5_expensive = df.nlargest(5, "cost_per_point")


print(top_5_expensive[[
    "player",
    "total_points",
    "salary",
    "cost_per_point"
]])
