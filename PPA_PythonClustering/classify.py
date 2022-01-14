import numpy as pd
import pandas as pd
import sklearn
from sklearn.cluster import Birch
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale

import sklearn.metrics as sm
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report

import matplotlib.pyplot as plt

from sklearn import linear_model

df = pd.read_csv(r"C:\Users\aaron\Desktop\CICS397A\HW3\data.csv")

reg = linear_model.LinearRegression()
reg.fit([[0,0], [2,2],[4,4]], [0,1,2])

reg.coef_



