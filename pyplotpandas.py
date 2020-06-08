import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
gas=pd.read_csv('gas_prices.csv')
# print(gas.head(5))
# plt.plot(gas.Year,gas.USA)
# plt.plot(gas['Year'],gas.Canada)
plt.figure(figsize=(8,8),dpi=100)
plt.title('Gas prices over time (in usd)',fontdict={'fontweight':'bold','fontsize':10})
# plt.plot(gas.Year,gas['South Korea'],'b.-',label="south korea")
plt.plot(gas.Year,gas.Australia,'y.-')

for country in gas:
    if country !='Year':
        # print(country)
        plt.plot(gas.Year,gas[country],marker='.',label=country)
plt.xticks(gas.Year[::3].tolist()+[2011])
plt.xlabel('Year')
plt.ylabel('US dollars')
plt.legend()
plt.savefig('Gas_price_fig.png',dpi=300)
plt.show()
