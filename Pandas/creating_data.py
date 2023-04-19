import pandas as pd

# DataFrame
DF = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(DF)

# DataFrame for string
DF_string = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(DF_string)

# DataFrame with index

DF_index = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
                         'Sue': ['Pretty good.', 'Bland.']},
                        index=['Product A', 'Product B'])
print(DF_index)

# Series
S = pd.Series([1, 2, 3, 4, 5])
print(S)

# Serie with index and name
S_indexname = pd.Series([30, 35, 40],
                        index=['2015 Sales', '2016 Sales', '2017 Sales'],
                        name='Product A')
print(S_indexname)