import pandas as pd
path = "../input/winemag-data-130k-v2.csv"
wine_reviews = pd.read_csv(path)
# print(wine_reviews)

# how large the resulting DataFrame is:
print(wine_reviews.shape)

# head() - grabs the first five rows
print(wine_reviews.head())

# To make pandas use the column for the index, we can specify an index_col
wine_reviews_index = pd.read_csv(path, index_col=0)
print(wine_reviews_index.head())

# To save this DataFrame to disk as a csv file with the name wine_index.csv
wine_reviews_index.to_csv('wine_index.csv')