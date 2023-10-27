import pandas as pd
# Data leakage (or leakage) happens when your training data contains information about the target, but similar data
# will not be available when the model is used for prediction

# Target leakage
# Target leakage occurs when your predictors include data that will not be available at the time you make predictions
# People take antibiotic medicines after getting pneumonia in order to recover. The raw data shows a strong
# relationship between those columns, but took_antibiotic_medicine is frequently changed after the value for
# got_pneumonia is determined. This is target leakage.

pneumonia = pd.DataFrame({'got_pneumonia': [False, False, True],
                         'took_antibiotic_medicine': [False, False, True]})
print(pneumonia)
# To prevent this type of data leakage, any variable updated (or created) after the target value is realized
# should be excluded.

# Train-Test Contamination
# A different type of leak occurs when you aren't careful to distinguish training data from validation data.


# detect and remove target leakage

import pandas as pd

# Read the data
data = pd.read_csv('../input/AER_credit_card_data.csv',
                   true_values = ['yes'], false_values = ['no'])

# Select target
y = data.card

# Select predictors
X = data.drop(['card'], axis=1)

print("Number of rows in the dataset:", X.shape[0])
X.head()



from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Since there is no preprocessing, we don't need a pipeline (used anyway as best practice!)
my_pipeline = make_pipeline(RandomForestClassifier(n_estimators=100))
cv_scores = cross_val_score(my_pipeline, X, y,
                            cv=5,
                            scoring='accuracy')

print("Cross-validation accuracy: %f" % cv_scores.mean())



# With experience, you'll find that it's very rare to find models that are accurate 98% of the time. It happens,
# but it's uncommon enough that we should inspect the data more closely for target leakage.

# A few variables look suspicious. For example, does expenditure mean expenditure on this card or on cards used
# before applying? At this point, basic data comparisons can be very helpful:

expenditures_cardholders = X.expenditure[y]
expenditures_noncardholders = X.expenditure[~y]
# EXP : Here, y is our target variable 'card' and it is a pd.Series of True and False.
# Here, only the entries for expenditure where value of y is True are stored in expenditures_cardholders.
print('Fraction of those who did not receive a card and had no expenditures: %.2f' \
      %((expenditures_noncardholders == 0).mean()))
print('Fraction of those who received a card and had no expenditures: %.2f' \
      %(( expenditures_cardholders == 0).mean()))



# As shown above, everyone who did not receive a card had no expenditures, while only 2% of those who received
# a card had no expenditures. It's not surprising that our model appeared to have a high accuracy. But this also seems
# to be a case of target leakage, where expenditures probably means expenditures on the card they applied for.



# Drop leaky predictors from dataset
potential_leaks = ['expenditure', 'share', 'active', 'majorcards']
X2 = X.drop(potential_leaks, axis=1)

# Evaluate the model with leaky predictors removed
cv_scores = cross_val_score(my_pipeline, X2, y,
                            cv=5,
                            scoring='accuracy')

print("Cross-val accuracy: %f" % cv_scores.mean())

