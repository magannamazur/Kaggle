# Mean Absolute Error
# error=actual−predicted
# So, if a house cost $150,000 and you predicted it would cost $100,000 the error is $50,000.


import pandas as pd

melbourne_file_path = '../input/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
filtered_melbourne_data = melbourne_data.dropna(axis=0)
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(X, y)

# mean absolute error
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
print(mean_absolute_error(y, predicted_home_prices))

# validation data
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))