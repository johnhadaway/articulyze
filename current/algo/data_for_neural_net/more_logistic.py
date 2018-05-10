import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# position of metric in dataset
index = {
    'a_polarity': 0,
    'a_subjectivity': 1,
    'characters': 2,
    'dale_chall': 3,
    'dale_chall_percentage': 4,
    'flesch': 5,
    's_polarity': 6,
    's_subjectivity': 7,
    'spache_percentage': 8,
    'weasel_percentage': 9,
    'word_count': 10
}

# dict of options, all initially false
options = {}
for key in list(index.keys()):
    options[key] = False

# ======== EDIT THIS: set which inputs you want ; change output_file name for tracking probabilities ====================
options['word_count'] = True
options['flesch'] = True

output_file = "flesch_logistic.csv"

# ======= don't need to edit anything below here ========================================================================

inputs = dict((key,index[key]) for key,value in options.items() if value == True)
n_inputs = len(inputs)

dataset = np.loadtxt("reformatted.csv", delimiter=",")
np.random.shuffle(dataset)
X = dataset[:,0:11]
Y = dataset[:,11]

train_x = np.zeros((500,n_inputs)) 
train_y = np.zeros(500)
test_x = np.zeros((250,n_inputs)) 
test_y = np.zeros(250)

for i in range(0,500):
    for j,index in zip(range(0,n_inputs),inputs.values()):
        train_x[i][j] = X[i][index]
    train_y[i] = Y[i]

for i in range(0,250):
    for j,index in zip(range(0,n_inputs),inputs.values()):
        test_x[i][j] = X[500+i][index]
    test_y[i] = Y[500+i]


model = LogisticRegression()
model = model.fit(train_x, train_y)
acc = model.score(test_x, test_y)
print(acc)

unshuffled_dataset = np.loadtxt("reformatted.csv", delimiter=",")
unshuffled_x = np.zeros((750,n_inputs)) 
for i in range(0,750):
    for j,index in zip(range(0,n_inputs),inputs.values()):
        unshuffled_x[i][j] = X[i][index]

prob_estimates = model.predict_proba(unshuffled_x)
df = pd.DataFrame(data=prob_estimates)
df.to_csv(output_file)

