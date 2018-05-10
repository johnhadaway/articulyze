from keras.models import model_from_json
import numpy

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

dataset = numpy.loadtxt("reformatted.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:11]

print(X)
predictions = loaded_model.predict(X)
#print(predictions)
