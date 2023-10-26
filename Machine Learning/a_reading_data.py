import pandas as pd
# file_name = melb_data
def read_data(file_name):
    file_path = f'../input/{file_name}.csv'
    data = pd.read_csv(file_path)
    return data

def read_data_dropna(file_name):
    # dropna drops missing values (think of na as "not available")
    return read_data(file_name).dropna(axis=0)

def read_data_describe(file_name):
    # dropna drops missing values (think of na as "not available")
    return read_data(file_name).describe()
