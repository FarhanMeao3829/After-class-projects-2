import seaborn as sns 
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

print(df.head(10))

sns.distplot(df["size"])
sns.distplot(df["tip"])

sns.distplot(df["total_bill"], kde=False)
sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", style="time")
sns.pairplot(df, hue='sex')
plt.show()