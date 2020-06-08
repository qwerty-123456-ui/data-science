

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#basic graph
x=[0,1,2,3,4,5]
y=[0,2,4,6,8,10]
# plt.figure(figsize=(5,3),dpi=100)
# plt.plot(x,y,label='2x',color='red',linewidth=2,linestyle='--',marker='.',markersize=10,markeredgecolor='blue')
#shortcut fn='[color][marker][line]'
plt.plot(x,y,'b^--',label='2x')

#line number 2
x2 =  np.arange(0,4,0.5)
plt.plot(x2[:6],x2[:6]**2,'r',label="x^2")
plt.plot(x2[5:],x2[5:]**2,'r--')
print(x2)
plt.title('our first graph',fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,7,7.5,10])
plt.legend()
plt.savefig("mygraph.png",dpi=300)
plt.show()
# print('❤')
###bar chart
labels=['A','B','C']
values=[1,4,2]
bars=plt.bar(labels,values)
patterns=['/','*','o']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
# bars[0].set_hatch('/')
# bars[1].set_hatch('o')
# bars[2].set_hatch('*')
bars=plt.figure(figsize=(6,4))
plt.show()