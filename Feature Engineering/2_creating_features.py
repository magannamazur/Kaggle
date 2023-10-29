# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import seaborn as sns

# plt.style.use("seaborn-whitegrid")
# plt.rc("figure", autolayout=True)
# plt.rc(
#     "axes",
#     labelweight="bold",
#     labelsize="large",
#     titleweight="bold",
#     titlesize=14,
#     titlepad=10,
# )

accidents = pd.read_csv("../input/accidents.csv")
autos = pd.read_csv("../input/autos.csv")
concrete = pd.read_csv("../input/concrete.csv")
customer = pd.read_csv("../input/customer.csv")

###### Mathematical Transforms

autos["stroke_ratio"] = autos.stroke / autos.bore

autos["displacement"] = (
    np.pi * ((0.5 * autos.bore) ** 2) * autos.stroke * autos.num_of_cylinders
)

# If the feature has 0.0 values, use np.log1p (log(1+x)) instead of np.log
accidents["LogWindSpeed"] = accidents.WindSpeed.apply(np.log1p)

# Plot a comparison
# fig, axs = plt.subplots(1, 2, figsize=(8, 4))
# sns.kdeplot(accidents.WindSpeed, shade=True, ax=axs[0])
# sns.kdeplot(accidents.LogWindSpeed, shade=True, ax=axs[1]);


###### Counts
# In Traffic Accidents are several features indicating whether some roadway object was near the accident. This will
# create a count of the total number of roadway features nearby using the sum method:
roadway_features = ["Amenity", "Bump", "Crossing", "GiveWay",
    "Junction", "NoExit", "Railway", "Roundabout", "Station", "Stop",
    "TrafficCalming", "TrafficSignal"]
accidents["RoadwayFeatures"] = accidents[roadway_features].sum(axis=1)

accidents[roadway_features + ["RoadwayFeatures"]].head(10)

# This will count how many components are in a formulation with the dataframe's built-in greater-than gt method:

components = [ "Cement", "BlastFurnaceSlag", "FlyAsh", "Water",
               "Superplasticizer", "CoarseAggregate", "FineAggregate"]
concrete["Components"] = concrete[components].gt(0).sum(axis=1)

concrete[components + ["Components"]].head(10)

# concrete["Components"] = concrete[[ "Cement", "BlastFurnaceSlag", "FlyAsh", "Water",
#                "Superplasticizer", "CoarseAggregate", "FineAggregate"]].gt(0).sum(axis=1)

##### Building-Up and Breaking-Down Features

# separate
customer[["Type", "Level"]] = (  # Create two new features
    customer["Policy"]           # from the Policy feature
    .str                         # through the string accessor
    .split(" ", expand=True)     # by splitting on " "
                                 # and expanding the result into separate columns
)

customer[["Policy", "Type", "Level"]].head(10)

# join
autos["make_and_style"] = autos["make"] + "_" + autos["body_style"]
autos[["make", "body_style", "make_and_style"]].head()


##### Group Transforms

# aggregation
customer["AverageIncome"] = (
    customer.groupby("State")  # for each state
    ["Income"]                 # select the income
    .transform("mean")         # and compute its mean
)

customer[["State", "Income", "AverageIncome"]].head(10)

# Other handy methods include max, min, median, var, std, and count

customer["StateFreq"] = (
    customer.groupby("State")
    ["State"]
    .transform("count")
    / customer.State.count()
)

customer[["State", "StateFreq"]].head(10)

# If you're using training and validation splits, to preserve their independence, it's best to create a grouped feature
# using only the training set and then join it to the validation set. We can use the validation set's merge method
# after creating a unique set of values with drop_duplicates on the training set:



# Create splits
df_train = customer.sample(frac=0.5)
df_valid = customer.drop(df_train.index)

# Create the average claim amount by coverage type, on the training set
df_train["AverageClaim"] = df_train.groupby("Coverage")["ClaimAmount"].transform("mean")

# Merge the values into the validation set
df_valid = df_valid.merge(
    df_train[["Coverage", "AverageClaim"]].drop_duplicates(),
    on="Coverage",
    how="left",
)

df_valid[["Coverage", "AverageClaim"]].head(10)

##### Interaction with a Categorical

ames = pd.read_csv("../input/ames.csv")
X = ames.copy()
y = X.pop("SalePrice")
# One-hot encode Categorical feature, adding a column prefix "Cat"
X_new = pd.get_dummies(ames.Categorical, prefix="Cat")

# Multiply row-by-row
X_new = X_new.mul(ames.Continuous, axis=0)

# Join the new features to the feature set
X = X.join(X_new)