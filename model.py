from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

df = pd.read_csv("full_dataset.csv")


df = df.drop(columns=['FIPS', 'county_name', 'state_abbr', 'state_name',
                      'state_FIPS', 'county_FIPS', 'state'])#dropping unnecessary cols

df = df.apply(lambda x: x.astype(float))#converting each column to float

print(df['NFLIS'].head())
print(df.loc[df['Year'] == 2010].shape)

train_data = 

model = Sequential()
model.add(Dense(16, activation = 'relu', input_shape = (3109, )))
model.add(Dense(3109, activation = 'relu'))
