from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

df = pd.read_csv("full_dataset.csv")
print(df.dtypes)

'''
model = Sequential()
model.add(Dense(16, activation = 'relu', input_shape = ()))
model.add(Dense(10, activation = 'relu'))
'''
