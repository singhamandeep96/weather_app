import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset('tips')
# sns.scatterplot(x='total_bill', y='tip', data=tips)
# plt.title("Scatter Plot of Total bill vs Tips ")
# plt.show()


sns.lineplot(x='size', y='total_bill', data=tips)
plt.title("Line Plot of Total bill by size")
plt.show()
