import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("../input/winemag-data-130k-v2.csv", index_col=0)

# Summary function
print(reviews.points.describe())

# mean
print(reviews.points.mean())

# median
print(reviews.points.median())

# unique values
print(reviews.taster_name.unique())

# list of unique values and how often they occur in the dataset
print(reviews.taster_name.value_counts())

# Maps // rechanging the data
#1
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

#2
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

#3
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean

#4
reviews.country + " - " + reviews.region_1

print(reviews.head())

# a variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
print(bargain_idx, bargain_wine)

# Is a wine more likely to be "tropical" or "fruity"? Create a Series descriptor_counts counting how many times
# each of these two words appears in the description column in the dataset. (For simplicity, let's ignore
# the capitalized versions of these words.)

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
print(descriptor_counts)

# A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars.
# Any other score is 1 star.
# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should
# automatically get 3 stars, regardless of points.
# Create a series `star_ratings` with the number of stars corresponding to each review in the dataset.
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')

print(star_ratings)