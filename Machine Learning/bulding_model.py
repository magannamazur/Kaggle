import pandas as pd

melbourne_file_path = '../input/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
# To choose variables/columns, we'll need to see a list of all columns in the dataset
print(melbourne_data.columns)

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

# Prediction Target / y
y = melbourne_data.Price

# Choosing "Features" / X
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# Building Your Model
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
print(y.head().tolist())

