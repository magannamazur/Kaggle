import pandas as pd
path = "../input/winemag-data-130k-v2.csv"
reviews = pd.read_csv(path, index_col=0)
pd.set_option('display.max_rows', 5)
print(reviews)

# The two ways of selecting a specific Series out of a DataFrame
print(reviews.country)
print(reviews['country'])

# to drill down to a single specific value, we need only use the indexing operator [] once more:
print(reviews['country'][0])

# index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm.
# first row
print(reviews.iloc[0])
# To get a full column
print(reviews.iloc[:,0])

# to select the country column from just the first, second, and third row, we would do:
print(reviews.iloc[:3, 0])
first_descriptions = reviews.iloc[: 10]["description"]
desc = reviews.description
first_descriptions= desc.head(10)
reviews.loc[:9, "description"]
#  first 10 values from the description column in reviews

# Or, to select just the second and third entries, we would do:
reviews.iloc[1:3, 0]

# It's also possible to pass a list:
# [row], [column]
# : - all
reviews.iloc[[0, 1, 2], 0]

# This will start counting forwards from the end of the values. So for example here are the last five elements
# of the dataset.
print(reviews.iloc[-5:])

#  label-based selection. In this paradigm, it's the data index value, not its position, which matters.
print(reviews.loc[0, 'country'])
print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

# more visible way:
cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

# first 100 raws for country and variety
cols = ['country', 'variety']
df = reviews.loc[:99, cols]

#

cols_idx = [0, 11]
df = reviews.iloc[:100, cols_idx]

# Choosing between loc and iloc
# When choosing or transitioning between loc and iloc, there is one "gotcha" worth keeping in mind,
# which is that the two methods use slightly different indexing schemes.
# iloc uses the Python stdlib indexing scheme, where the first element of the range is included
# and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively.
# So 0:10 will select entries 0,...,10.
# Why the change? Remember that loc can index any stdlib type: strings, for example.
# If we have a DataFrame with index values Apples, ..., Potatoes, ..., and we want to select
# "all the alphabetical fruit choices between Apples and Potatoes", then it's a lot more convenient
# to index df.loc['Apples':'Potatoes'] than it is to index something like df.loc['Apples', 'Potatoet']
# (t coming after s in the alphabet).

# Manipulating the index
new_rew = reviews.set_index("title")
print(new_rew)

# Conditional selection true/false
print(reviews.country == 'Italy')

# shows only italian wines
print(reviews.loc[reviews.country == 'Italy'])

# italians with rang over 80 points
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])

# or italian or over 90 points
print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])

# isin
print(reviews.loc[reviews.country.isin(['Italy', 'France'])])

# isnull, notnull
print(reviews.loc[reviews.price.notnull()])

# Assigning data
reviews['critic'] = 'everyone'

# iterable value
reviews['index_backwards'] = range(len(reviews), 0, -1)