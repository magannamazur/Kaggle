import pandas as pd
reviews = pd.read_csv("../input/winemag-data-130k-v2.csv", index_col=0)

# You can use the dtype property to grab the type of a specific column
print(reviews.price.dtype)

# the dtypes property returns the dtype of every column in the DataFrame
print(reviews.dtypes)

# float64 means that it's using a 64-bit floating point number
# int64 means a similarly sized integer instead
# the columns consisting entirely of strings do not get their own type; they are instead given the object type

# to convert a column (int64 data type into a float64)of one type into another by using the astype() function
reviews.points.astype('float64')

# A DataFrame or Series index has its own dtype
print(reviews.index.dtype)