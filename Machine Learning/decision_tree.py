# We use data to decide how to break the houses into two groups, and then again to determine the predicted price
# in each group. This step of capturing patterns from data is called fitting or training the model.
# The data used to fit the model is called the training data.
#
# The details of how the model is fit (e.g. how to split up the data) is complex enough that we will save it for later.
# After the model has been fit, you can apply it to new data to predict prices of additional homes.

import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '../input/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
print(melbourne_data.describe())

# The results show 8 numbers for each column in your original dataset.
# The first number, the count, shows how many rows have non-missing values.
# Missing values arise for many reasons.
# The second value is the mean, which is the average.
# Under that, std is the standard deviation, which measures how numerically spread out the values are.
# To interpret the min, 25%, 50%, 75% and max values, imagine sorting each column from lowest to highest value.
# The first (smallest) value is the min. If you go a quarter way through the list, you'll find a number
# that is bigger than 25% of the values and smaller than 75% of the values.
# That is the 25% value (pronounced "25th percentile"). The 50th and 75th percentiles are defined analogously,
# and the max is the largest number.

# shows the top few rows of the data in Melbourne data
print(melbourne_data.head())