# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:22:21 2023

@author: hugoa
"""

print("hello from wael")
print("yooo")
print("vois-tu mon code ?")

print("test with branch")

print('test with branch arthur')
#Exercise 5--------------------------------------------------------------------------

import matplotlib.pyplot as plt

column_labels = list('ABC')
row_labels = list('WXYZ')
data = np.array([[1, 2, 3], [0, 3, 2], [1, 2, 3], [4, 3, 2]]) 
fig, axis = plt.subplots() 
heatmap = axis.pcolor(data, cmap=plt.cm.Greens)
plt.savefig('test.png')
plt.show() 
