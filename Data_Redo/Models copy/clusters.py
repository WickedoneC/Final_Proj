import sys
import pandas as pd
import altair as alt
import streamlit as st

df = pd.read_csv('/Users/wickedbear/Coding/Projects/Final_Proj/Data_Redo/Models copy/cleaned_df2.csv')

cols_drop = ['Unnamed: 0']
df.drop(columns=cols_drop, inplace=True)

mdf = df[["Moody's Rating"]]

ndf = pd.read_csv('/Users/wickedbear/Coding/Projects/Final_Proj/Data_Redo/Models copy/ntr.csv')
ndf.drop(columns=cols_drop, inplace=True)

o = df[["Moody's Rating"]]
dfw = df.drop("Moody's Rating", axis=1)
dfc = df

data_rankings = {'Aaa': 0,
                 'Aa1': 1,
                 'Aa2': 2,
                 'Aa3': 3,
                 'A1': 4,
                 'A2': 5,
                 'A3': 6,
                 'Baa1': 7,
                 'Baa2': 8,
                 'Baa3': 9,
                 'Ba1': 10,
                 'Ba2': 11,
                 'Ba3': 12,
                 'B1': 13,
                 'B2': 14,
                 'B3': 15,
                 'WR': 16
                 }

dfc["Moody's Rating"] = dfc["Moody's Rating"].replace(data_rankings)

y = df["Moody's Rating"]
X = df.drop("Moody's Rating", axis=1)

from sklearn.cluster import KMeans

k_means = KMeans(n_clusters=16, random_state=12)
k_means.fit(X)
cluster_assignments = k_means.predict(X)


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# data_train, data_test, target_train, target_test = train_test_split(X, y,
#                                                                     test_size = 0.25, random_state=123)
# Instantiate and fit a RandomForestClassifier
# forest_2 = RandomForestClassifier(n_estimators = 5, max_features= 10, max_depth= 2)
# forest_2.fit(data_test, target_test)
# cluster_assignments = forest_2.predict(X)

r = pd.DataFrame(cluster_assignments)
r["Predicted Rating"] = r[0]
r.drop(0, axis=1, inplace=True)

inv_map = {v: k for k, v in data_rankings.items()}

(o["Moody's Rating"] == r["Predicted Rating"]).value_counts()

p = o.replace(data_rankings)

test_val = p["Moody's Rating"] - r["Predicted Rating"]
mean_diff_rating = test_val.mean()
# mean_diff_rating

r["Predicted Rating"] = r["Predicted Rating"].replace(inv_map)
p["Moody's Rating"] = p["Moody's Rating"].replace(inv_map)

ndf = ndf.drop(columns="Names")
names_x = pd.concat([ndf, X], axis=1)
rx = pd.concat([r, names_x], axis=1)

ticker_list = list(rx["Ticker"].unique())



st.title('Credit Analysis')
hlist = st.multiselect('Select a ticker:', ticker_list)

st.write('')
if len(hlist) > 0:

    q = pd.DataFrame()
    for thing in hlist:
        z = rx.loc[rx["Ticker"] == thing]
        q = pd.concat([q, z], ignore_index=True)



    q


# mean_diff_rating