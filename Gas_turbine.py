# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 21:01:33 2021

@author: AVERKHO
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')


dat=pd.read_excel('./Gas Turbine.xlsx')

fig=plt.figure(1)
ax=fig.add_subplot(111)
line1=ax.plot(dat['Output'],label='Output',color='blue')
ax.set_ylabel('Output, MW')
ylims=ax.get_ylim()
ax.set_ylim([25,ylims[1]])

ax2=ax.twinx()
line2=ax2.plot(dat['Temperature'],label='Temperature',color='red')
ax.set_xticklabels([])
ax2.set_ylabel('Temperature, 0C')
ax.grid(True)

lines=line1+line2
labels=[l.get_label() for l in lines]
plt.legend(lines,labels,loc='lower left')
ax.set_title('Gas Turbine productivity',size=14)
