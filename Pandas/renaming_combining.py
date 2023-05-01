import pandas as pd
#pd.set_option('display.max_rows', 5)
pd.options.display.width = 0
reviews = pd.read_csv("../input/winemag-data-130k-v2.csv", index_col=0)

# Renaming
# to change the points column in our dataset to score
print(reviews.rename(columns={'points': 'score'}))

# rename() lets you rename index or column values by specifying a index or column keyword parameter,
print(reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}))

# set_index() is usually more convenient for index
# index of country
print(reviews.set_index('country'))

# Both the row index and the column index can have their own name attribute - rename_axis()
# index name = wines
# column name = fields
print(reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns'))

################
# Combining
# concat(), join(), and merge()

canadian_youtube = pd.read_csv("../input/CAvideos.csv")
british_youtube = pd.read_csv("../input/GBvideos.csv")

# The simplest combining method is concat()
print(pd.concat([canadian_youtube, british_youtube]))

# join() lets you combine different DataFrame objects which have an index in common
# pull down videos that happened to be trending on the same day in both Canada and the UK
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

print(left.join(right, lsuffix='_CAN', rsuffix='_UK'))
print(canadian_youtube.set_index(['title', 'trending_date']).
      join(british_youtube.set_index(['title', 'trending_date']), lsuffix='_CAN', rsuffix='_UK'))