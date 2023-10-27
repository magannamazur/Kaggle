import pandas as pd

# Read the data
data = pd.read_csv('../input/melb_data.csv')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price



# Then, we define a pipeline that uses an imputer to fill in missing values and a random forest model
# to make predictions.
# While it's possible to do cross-validation without pipelines, it is quite difficult! Using a pipeline will make
# the code remarkably straightforward.

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=50,
                                                              random_state=0))
                             ])

from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
# Recall we set the number of folds with the cv parameter.
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')

print("MAE scores:\n", scores)

# We typically want a single measure of model quality to compare alternative models.
# So we take the average across experiments.

print("Average MAE score (across experiments):")
print(scores.mean())