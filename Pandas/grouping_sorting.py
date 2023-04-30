import pandas as pd
reviews = pd.read_csv("../input/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# for each of these groups, we grabbed the points() column and counted how many times it appeared
print(reviews.groupby('points').points.count())

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