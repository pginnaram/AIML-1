import pandas as pd
import matplotlib.pyplot as plt
import math

#Read the data
data = pd.read_csv("../data/Experiment_1_Dataset.csv", header=None)
X1 = []
X2 = []
Y = []
print(data.shape)
for row in range(data.shape[0]):
    for col in range(data.shape[1]):
        sample = data.loc[row, col]
        if math.isnan(float(sample)):
            continue
        label = int(sample)
        X1.append(row)
        X2.append(col)
        Y.append(label)
        print(row, col, label)
print(Y)

# %matplotlib inline
fig = plt.figure()
plt.scatter(X2,X1,c=Y)

plt.show()

