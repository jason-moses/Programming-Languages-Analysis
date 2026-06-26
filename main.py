import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("QueryResults.csv", names = ["DATE","TAG", "POST"], header = 0)
df.DATE = pd.to_datetime(df["DATE"])
reshaped_df = df.pivot(index = "DATE", columns = "TAG", values = "POST")
print(reshaped_df.columns)
reshaped_df.fillna(0, inplace = True)
print(reshaped_df.isna().values.any())

plt.figure(figsize=(10,6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Year",fontsize=14)
plt.ylabel("Number of Posts",fontsize=14)
plt.ylim(0,35000)
for column in reshaped_df.columns:
  plt.plot(reshaped_df.index, reshaped_df[column], linewidth=2, label=reshaped_df[column].name)
  plt.legend(fontsize=10)
plt.show()



