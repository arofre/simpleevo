import numpy as np
import matplotlib.pyplot as plt

def plot(foodlist,fertlist,attrlist, poplist):
    x = np.linspace(1,1000,len(foodlist))
    x1 = np.linspace(1,1000,len(fertlist))
    x2 = np.linspace(1, 1000, len(attrlist))
    x3 = np.linspace(1,1000,len(poplist))
    plt.figure(1)
    plt.plot(x,foodlist,label = "Average food gathering")
    plt.plot(x1,fertlist, label = "Average fertility")
    plt.plot(x2,attrlist, label = "Average attractiveness")
    plt.legend()
    plt.figure(2)
    plt.plot(x3,poplist, label = "Population size")
    plt.legend()
    plt.show()

