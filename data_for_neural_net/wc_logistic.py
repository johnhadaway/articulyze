import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

dataset = np.loadtxt("reformatted.csv", delimiter=",")
np.random.shuffle(dataset)
X = dataset[:,0:11]
Y = dataset[:,11]

train_x = np.zeros(500).reshape(500,1)
train_y = np.zeros(500)
test_x = np.zeros(250).reshape(250,1)
test_y = np.zeros(250)

for i in range(0,500):
    train_x[i] = X[i][10]
    train_y[i] = Y[i]

for i in range(0,250):
    test_x[i] = X[500+i][10]
    test_y[i] = Y[500+i]


# test_x.reshape(-1,1)
# train_x.reshape(-1,1)
model = LogisticRegression()
model = model.fit(train_x, train_y)
acc = model.score(test_x, test_y)
print(acc)

unshuffled_dataset = np.loadtxt("reformatted.csv", delimiter=",")
unshuffled_x = np.zeros(750).reshape(750,1)
for i in range(0,750):
    unshuffled_x[i] = unshuffled_dataset[i,10]

prob_estimates = model.predict_proba(unshuffled_x)
df = pd.DataFrame(data=prob_estimates)
df.to_csv('wc_data.csv')

