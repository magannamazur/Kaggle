import pandas as pd
reviews = pd.read_csv("../input/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# groupby, the order of the rows is dependent on the values in the index, not in the data.

# for each of these groups, we grabbed the points() column and counted how many times it appeared
# dataframe
print(reviews.groupby('points').points.count())
print(reviews.groupby('points').size())

# value_counts() display the result in descending order so that the first element is the most frequently-occurring element.
# Excludes NA values by default. for series
print(reviews.groupby('points').points.value_counts())

# to get the cheapest wine in each point value category, we can do the following
print(reviews.groupby('points').price.min())

# selecting the name of the first wine reviewed from each winery in the dataset
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))


# here's how we would pick out the best wine by country and province
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))

# agg(), which lets you run a bunch of different functions on your DataFrame simultaneously
print(reviews.groupby(['country']).price.agg([len, min, max]))

# Multi-indexes
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)
mi = countries_reviewed.index
print(type(mi))

# converting back to a regular index, the reset_index() method:
print(countries_reviewed.reset_index())

# To get data in the order want it in we can sort it ourselves - sort_values()
countries_reviewed = countries_reviewed.reset_index()
print(countries_reviewed.sort_values(by='len'))

# sort_values() defaults to an ascending sort, where the lowest values go first
print(countries_reviewed.sort_values(by='len', ascending=False))

# To sort by index values, use the companion method sort_index()
print(countries_reviewed.sort_index())

# you can sort by more than one column at a time
print(countries_reviewed.sort_values(by=['country', 'len']))

# the column names
print(reviews.columns.values)

# a Series whose index is a MultiIndexof {country, variety} pairs.
# For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}.
# Sort the values in the Series in descending order based on wine count.
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending = False)
print(country_variety_counts)