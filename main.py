import pandas as pd

new = pd.read_csv("clients.csv")
res = new.groupby("countries")

results = res["client_id"].count()
avg = res["age"].mean()
print(results)
print(avg)