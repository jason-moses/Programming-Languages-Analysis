import pandas as pd

df = pd.read_csv("matplotlib_data.csv")

print(df.head())
print(df.columns)

df["DATE"] = pd.to_datetime(df["DATE"])
df["COUNT"].replace(",", "",regex=False)
df["COUNT"] = pd.to_numeric(df["COUNT"])

import matplotlib.pyplot as plt
plt.figure(figsize = (10,6))
plt.plot(df["DATE"], df["COUNT"])

plt.title("Matplotlib Downloads Over Time")
plt.xlabel("Date")
plt.ylabel("Downloads")

plt.show()

