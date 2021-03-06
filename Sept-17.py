
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
def findArea (N):
    Ro = 1
    Ri = 0.5
    ymin = -1
    ymax = 1
    xmin = -1 
    xmax = 1
    Area = math.pi*((Ro**2)-(Ri**2))
    totalp = 0
    insidep = 0
    for i in range(0,N):
        x = random.uniform(xmin,xmax)
        y = random.uniform(ymin,ymax)
        if (x**2 + y**2) >= Ri**2 and (x**2 + y**2) <= Ro**2:
            totalp +=1
            insidep +=1
        else:
            totalp +=1
        pointList.append(i)
        ErrorList.append(i)
    pseudo = (insidep/totalp)*4
    error = abs(((insidep - totalp)/totalp))
    return pseudo,Area,error

    def plotError():
        ErrorList = []
        pointList = []
        plt.plot(pointList,ErrorList)
        plt.show(block=True)

