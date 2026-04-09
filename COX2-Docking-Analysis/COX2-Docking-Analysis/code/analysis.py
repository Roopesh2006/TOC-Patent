import pandas as pd

data = pd.read_csv("../data/dataset.csv")

print("=== Drug Ranking Based on Binding Energy ===")
print(data.sort_values(by="BindingEnergy"))

print("\nBest Drug:")
best = data.sort_values(by="BindingEnergy").iloc[0]
print(best)
