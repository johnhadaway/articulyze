from keras.models import model_from_json
import numpy
from sklearn.externals import joblib

# load json and create model
json_file = open('model2.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model2.h5")
print("Loaded model from disk")

scaler = joblib.load('scaler.save')

loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

dataset = numpy.loadtxt("reformatted2.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[0:2,0:11]
scaled_X = scaler.transform(X)

print(scaled_X)
predictions = loaded_model.predict(scaled_X)
print(predictions)
