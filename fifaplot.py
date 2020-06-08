import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fifa=pd.read_csv('fifa_data.csv')
# print(fifa.head())
# plt.figure(figsize=(5,5),dpi=100)

# #histograms
# bins=[x for x in range(40,101,10)]
# plt.hist(fifa.Overall,bins=bins,color='#abcdef')
# plt.xticks(bins)
# plt.ylabel('number of players')
# plt.xlabel('skill level')
# plt.title('distribution of skill in players')
# plt.show()

#pie charts

# left=fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
# right=fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]
#
# labels=['left','right']
# colors=['#abcdef','#aabbcc']
# plt.pie([left,right],labels=labels,colors=colors,autopct='%.2f %%')
# plt.title('Foot preference of fifa players')
# plt.show()

# #pie chart 2
# fifa.Weight=[int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
# plt.style.use('ggplot')
# light=fifa.loc[fifa.Weight<125].count()[0]
# light_medium=fifa.loc[(fifa.Weight>125) & (fifa.Weight<150)].count()[0]
# medium=fifa.loc[(fifa.Weight>=150) & (fifa.Weight<175)].count()[0]
# medium_heavy=fifa.loc[(fifa.Weight>=175) & (fifa.Weight<200)].count()[0]
# heavy=fifa.loc[(fifa.Weight>=200)].count()[0]
# weights=[light,light_medium,medium,medium_heavy,heavy]
# labels=['under 125','125-150','150-175','175-200','over 200']
# explode=(.1,.1,.1,.1,.1)
# plt.pie(weights,labels=labels,autopct='%.2f %%',pctdistance=11.0,explode=explode)
# plt.show()


# box whiskers
plt.figure(figsize=(5,8))
barcelona=fifa.loc[fifa.Club=='FC Barcelona']['Overall']
madrid=fifa.loc[fifa.Club=='Real Madrid']['Overall']
revs=fifa.loc[fifa.Club=='New England Revolution']['Overall']
labels=['Bracelona','Madrid','NE Revolution']
boxes=plt.boxplot([barcelona,madrid,revs],labels=labels,patch_artist=True,whiskerprops={'linewidth':2},medianprops={'linewidth':2})
for box in boxes['boxes']:
    box.set(color='#4286f4',linewidth=2)
    box.set(facecolor='#e0e0e0')
plt.title('Professional Soccer Team Comparison')
plt.ylabel('Fifa Overall Rating')
plt.show()
