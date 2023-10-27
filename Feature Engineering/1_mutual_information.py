# A great first step is to construct a ranking with a feature utility metric, a function measuring associations
# between a feature and the target. Then you can choose a smaller set of the most useful features to develop initially
# and have more confidence that your time will be well spent.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use("seaborn-whitegrid")

df = pd.read_csv("../input/autos.csv")
df.head()

# The scikit-learn algorithm for MI treats discrete features differently from continuous features. Consequently, you
# need to tell it which are which. As a rule of thumb, anything that must have a float dtype is not discrete.
# Categoricals (object or categorial dtype) can be treated as discrete by giving them a label encoding. (You can
# review label encodings in our Categorical Variables lesson.)

X = df.copy()
y = X.pop("price")

# Label encoding for categoricals
for colname in X.select_dtypes("object"):
    X[colname], _ = X[colname].factorize()

# All discrete features should now have integer dtypes (double-check this before using MI!)
discrete_features = X.dtypes == int



# Scikit-learn has two mutual information metrics in its feature_selection module: one for real-valued targets
# (mutual_info_regression) and one for categorical targets (mutual_info_classif). Our target, price, is real-valued
from sklearn.feature_selection import mutual_info_regression

def make_mi_scores(X, y, discrete_features):
    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores

mi_scores = make_mi_scores(X, y, discrete_features)
mi_scores[::3]  # show a few features with their MI scores

# Bar plot:
def plot_mi_scores(scores):
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")


plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores)

# As we might expect, the high-scoring curb_weight feature exhibits a strong relationship with price, the target.

sns.relplot(x="curb_weight", y="price", data=df);



# The fuel_type feature has a fairly low MI score, but as we can see from the figure, it clearly separates two price
# populations with different trends within the horsepower feature. This indicates that fuel_type contributes an
# interaction effect and might not be unimportant after all. Before deciding a feature is unimportant from its MI score,
# it's good to investigate any possible interaction effects -- domain knowledge can offer a lot of guidance here.

sns.lmplot(x="horsepower", y="price", hue="fuel_type", data=df);
