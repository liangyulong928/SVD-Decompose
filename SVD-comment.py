import numpy as np
from scipy.sparse.linalg import svds
import matplotlib.pyplot as plt
import scipy
import pandas as pd
data = pd.read_csv('Cell_Phones_and_Accessories.csv')
commodityList = data['commodity']
userList = data['user']
levelList = data['level']
commodity = list(set(data['commodity']))
user = list(set(data['user']))
row = []
col = []
data = []
row.append(commodity.index(commodityList[0]))
col.append(user.index(userList[0]))
data.append(levelList[0]/1.0)
for i in range(1,len(commodityList)):
    if (row[-1]==commodity.index(commodityList[i])) and (col[-1]==user.index(userList[i])):
        data[-1] += levelList[i]
    else:
        row.append(commodity.index(commodityList[i]))
        col.append(user.index(userList[i]))
        data.append(levelList[i]/1.0)

c = scipy.sparse.coo_matrix((data,(row,col)),shape = (len(row),len(col)))
U,S,T = svds(c,10)

for i in range(9):
    x = U[:, i]
    y = U[:, i+1]
    fig = plt.figure(figsize=(16, 10))
    ax = plt.subplot()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    font1 = {'family' : 'Arial',
            'weight' : 'normal',
            'size'   : 18,
            'color' : 'red'
    }
    plt.xlabel("u%d" % (i + 1),font1)
    plt.ylabel("u%d" % (i + 2),font1)
    ax.scatter(x, y, s=0.5, c='k', marker='.')
    plt.savefig(f"./data-sketch-2/taskRelaiton{i}.png",dpi=300)

for i in range(9):
    x = T[i, :]
    y = T[i+1, :]
    fig = plt.figure(figsize=(16, 10))
    ax = plt.subplot()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    font1 = {'family' : 'Arial',
               'weight' : 'normal',
                'size'   : 18,
                'color' : 'red'
    }
    plt.xlabel("v%d" % (i + 1),font1)
    plt.ylabel("v%d" % (i + 2),font1)
    ax.scatter(x, y, s=0.5, c='k', marker='.')
    plt.savefig(f"./data-sketch-2/taskRelaiton-v{i+1}.png",dpi=300)  