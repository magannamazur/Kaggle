import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
data = pd.read_csv('../input/melb_data.csv')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price

# Separate data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y)

# XGBoost stands for extreme gradient boosting, which is an implementation of gradient boosting with several
# additional features focused on performance and speed.



from xgboost import XGBRegressor

my_model = XGBRegressor()
my_model.fit(X_train, y_train)



from sklearn.metrics import mean_absolute_error

predictions = my_model.predict(X_valid)
print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))


# Parameter Tuning
# - n_estimators specifies how many times to go through the modeling cycle
# - early_stopping_rounds causes the model to stop iterating when the validation score stops improving,
# how many rounds of straight deterioration to allow before stopping.
# - when using early_stopping_rounds, you also need to set aside some data for calculating the validation scores,
# this is done by setting the eval_set parameter.
# - a small learning rate and large number of estimators will yield more accurate XGBoost models.
# This means each tree we add to the ensemble helps us less. So,a higher value for n_estimators without overfitting
#  It's common to set the parameter n_jobs equal to the number of cores on your machine
my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
my_model.fit(X_train, y_train,
             early_stopping_rounds=5,
             eval_set=[(X_valid, y_valid)],
             verbose=False)

