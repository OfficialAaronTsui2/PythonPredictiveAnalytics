import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Western PA Median Age of Death
# https://catalog.data.gov/dataset/allegheny-county-median-age-at-death

# Summary of Dataset:

# The types of all the variables are all floats.
# Missing values were not recorded due to the low amount of data points (deaths) recorded.

# Summary Statistics:
# Black Deaths    Black MD AGE AT DEATH    WHITEdeaths     White MD AGE AT DEATH    TOTALdeaths*        TOTAL MD AGE AT DEATH
# Median
# 20.5              69.3                    72.5                78.1                    133.5                   76.5
# mean
# 47.02             64.01                   121.05              76.23                   171.21                  74.84
# mode 
# 3                 0                       4                   70                      52                      71.7
# range
# 287               83.2                    723                 88.4                    802                     85.9         


#data = pd.read_csv(r"C:\Users\aaron\Desktop\HW2_CICS397A_WesternPA\data.csv")
data = pd.read_csv(r"C:/Users/aaron/Desktop/HW2_CICS397A_WesternPA/data.csv")



#Two histograms of Black/White Deaths
histbins = [0,10,20,30,40,50,60,70,80,90]
     

fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
ax2.hist(data["BLACKdeaths"], bins = histbins, color = 'green')
#plt.show()


fig3 = plt.figure()
ax3 = fig3.add_subplot(1,1,1)
ax3.hist(data["WHITEdeaths"], bins = histbins, color = 'blue')
#plt.show()



histVisualOfBlackDeaths = np.histogram(data["BLACKdeaths"], bins=histbins)
histVisualOfWhiteDeaths = np.histogram(data["WHITEdeaths"], bins=histbins)
#MVT = Middle Values Total
mvtBlack = histVisualOfBlackDeaths[0][4]+histVisualOfBlackDeaths[0][5]
mvtWhite = histVisualOfWhiteDeaths[0][4]+histVisualOfWhiteDeaths[0][5]

#Scatterplot of Black/White Median AaDs
data2 = (data["Black MD AGE AT DEATH"], data["White MD AGE AT DEATH"])
colors = ("blue", "green")
groups = ("Black Median AaD", "White Median AaD")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

for data, color, group in zip(data, colors, groups):
    x, y = data2
    ax.scatter(x, y, alpha=.8, c = color, edgecolors = 'none', s = 30, label = group)
plt.title("Scatterplot of Black vs White Median Age at Death")
plt.legend(loc=2)
#plt.show()

#Scatterplot of Black/White Median AaDs, colors swap if mvtWhite is bigger or equal to mvtBlack
colors = ("blue", "green")
colors2 = ("green", "blue")
groups = ("Black Median AaD", "White Median AaD")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
if mvtBlack > mvtWhite:
    for data, color, group in zip(data, colors, groups):
        x, y = data2
        ax.scatter(x, y, alpha=.8, c = color, edgecolors = 'none', s = 30, label = group)
else:
    for data, color, group in zip(data, colors2, groups):
        x, y = data2
        ax.scatter(x, y, alpha=.8, c = color, edgecolors = 'none', s = 30, label = group)
plt.title("If Else Scatterplot")
plt.legend(loc=2)
plt.show()

