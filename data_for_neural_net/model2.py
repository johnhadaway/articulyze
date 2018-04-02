from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn import preprocessing
import pandas as pd
from sklearn.externals import joblib

# fix random seed for reproducibility
numpy.random.seed(7)

# load pima indians dataset
dataset = numpy.loadtxt("reformatted2.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:11]
Y = dataset[:,11:13]

'''
min_max_scaler = preprocessing.MinMaxScaler()
min_max_scaler.fit(X)
scaled_X = min_max_scaler.transform(X)
scaler_filename = "scaler.save"
joblib.dump(min_max_scaler, scaler_filename)
'''

scaled_X = X
# create model
model = Sequential()
model.add(Dense(11, input_dim=11, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(scaled_X, Y, epochs=150, batch_size=10)

# evaluate the model
scores = model.evaluate(scaled_X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

'''
# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
'''
ans = model.predict(scaled_X)
df = pd.DataFrame(data=ans)
df.to_csv('data2.csv')

