from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn import preprocessing
import pandas as pd
from sklearn.externals import joblib
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score


# fix random seed for reproducibility

seed = 7
numpy.random.seed(seed)


# load pima indians dataset
dataset = numpy.loadtxt("reformatted2.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:11]
Y = dataset[:,11:13]

min_max_scaler = preprocessing.MinMaxScaler()
min_max_scaler.fit(X)
scaled_X = min_max_scaler.transform(X)

#MIN MAX SCALER
scaler_filename = "scaler.save"
joblib.dump(min_max_scaler, scaler_filename)
print(scaled_X)

# create model
def create_model():
    model = Sequential()
    model.add(Dense(11, input_dim=11, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(2, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def main():
    model = create_model()
    # Fit the model
    model.fit(scaled_X, Y, epochs=150, batch_size=5)
    # evaluate the model
    scores = model.evaluate(scaled_X, Y)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    # serialize model to JSON
    model_json = model.to_json()
    with open("model2.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model2.h5")
    print("Saved model to disk")

    ans = model.predict(scaled_X)
    df = pd.DataFrame(data=ans)
    df.to_csv('data2.csv')

def test():
    dataset = numpy.loadtxt("reformatted2.csv", delimiter=",")
    # split into input (X) and output (Y) variables
    X = dataset[:, 0:11]
    Y = dataset[:, 11:13]
    model = KerasClassifier(build_fn=create_model, epochs=150, batch_size=10, verbose=0)
    kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    results = cross_val_score(model, X, Y, cv=kfold)
    print(results.mean())

main()
