import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("company_sales_data.csv")
print(train)

profitList = train ['total_profit'].tolist()
monthList = train ['month_number'].tolist()

plt.plot(monthList, profitList, label= 'Month-wise profit data of the last year')

plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 300000, 400000, 600000, 800000])
plt.show()

profitList = train ['total_profit'].tolist()
monthList = train ['month_number'].tolist()

plt.plot(monthList, profitList, label= 'Profit data of last year',
         color='r', marker='o', markerfacecolor='k',
         linestyle='--', linewidth=3)

plt.xlabel('Month Numbr')
plt.ylabel('Profit in dollar')
plt.legend(loc= 'lower right')
plt.title('Company sales data of the last year')
plt.xticks(monthList)
plt.yticks([100000, 300000, 400000, 600000, 800000])
plt.show()