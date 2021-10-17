import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

All_sites_data = pd.read_csv("./06-Capstone-Project/all_sites_scores.csv")

# Exploring the Fandango data
print(All_sites_data.columns)
print(All_sites_data.head())
print(All_sites_data.info())
print(round(All_sites_data.describe(), 1))


# Printing scatterplot exploring the relationship between RT Critic reviews and RT User reviews.
fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
RottenTomatoes_scatter = sns.scatterplot(x="RottenTomatoes", y="RottenTomatoes_User", data=All_sites_data)
plt.title("The relationship between RT Critic reviews and RT User reviews")
plt.xlabel("RT Critic reviews")
plt.ylabel("RT User reviews")
plt.xlim(0,105)
plt.ylim(0,100)
plt.tight_layout()
plt.show()

# Create a new Rotten_Tomatoes dataframe
Rotten_Tomatoes = All_sites_data[["FILM", "RottenTomatoes", "RottenTomatoes_User"]]
Rotten_Tomatoes["Rating_diff"] = round(All_sites_data["RottenTomatoes"] - All_sites_data["RottenTomatoes_User"], 1)

# calculate the mean Absolute of rating diff column
Rotten_Tomatoes["abs_RT_Rating_diff"] = Rotten_Tomatoes["Rating_diff"].abs()


# Plot the distribution of the differences between RT Critics Score and RT User Score
fig, Rotten_Tomatoes_displot = plt.subplots(figsize=(5, 10), dpi=150)
sns.histplot(data=Rotten_Tomatoes, x='Rating_diff',bins=25, edgecolor='black', lw=2, kde=True)
plt.title("Rotten Tomatoes - The difference between Critics Score and User Score")
plt.xlabel("Rating difference ")
plt.ylim(0, 35)
plt.show()

# a distribution plot that showing the absolute value difference between Critics and Users on Rotten Tomatoes
fig, Rotten_Tomatoes_displot = plt.subplots(figsize=(5, 10), dpi=150)
sns.histplot(data=Rotten_Tomatoes, x='abs_RT_Rating_diff',bins=25, edgecolor='black', lw=2, kde=True)
plt.title("Rotten Tomatoes - Abs difference between Critics Score and User Score")
plt.xlabel("Rating difference ")
plt.ylim(0, 35)
plt.show()

# top 5 movies users rated higher than critics on average
higher_user_rating = Rotten_Tomatoes.sort_values("Rating_diff")[:5]
print(higher_user_rating[["FILM", "Rating_diff"]])

# top 5 movies critics scores higher than users on average
higher_critics_rating = Rotten_Tomatoes.sort_values("Rating_diff",ascending=False)[:5]
print(higher_critics_rating[["FILM", "Rating_diff"]])

# Printing scatterplot exploring the relationship between RT Critic reviews and RT User reviews on MetaCritic.
fig, ax = plt.subplots(figsize=(7, 3), dpi=150)
MetaCritic_scatter = sns.scatterplot(x="Metacritic", y="Metacritic_User", data=All_sites_data)
plt.title("The relationship between Metacritic Critic reviews and Metacritic User reviews")
plt.xlabel("Metacritic Critic reviews")
plt.ylabel("Metacritic User reviews")
plt.ylim(0, 10)
plt.xlim(0, 100)
plt.tight_layout()
plt.show()


# a scatterplot for the relationship between vote counts on MetaCritic versus vote counts on IMDB.
fig, ax = plt.subplots(figsize=(7, 3), dpi=150)
IMDb_scatter = sns.scatterplot(x="Metacritic_user_vote_count", y="IMDB_user_vote_count", data=All_sites_data)
plt.title("The relationship between vote counts on MetaCritic versus vote counts on IMDB.")
plt.xlabel("Metacritic user vote count")
plt.ylabel("IMDb user vote count")
plt.ylim(0, 350000)
plt.xlim(0,2500)
plt.tight_layout()
plt.show()

# highest IMDB user vote count
print(All_sites_data.sort_values("IMDB_user_vote_count", ascending=False)[:1])
print(All_sites_data.iloc[14])

# highest Metacritic user vote count
print(All_sites_data.sort_values("Metacritic_user_vote_count", ascending=False)[:1])
print(All_sites_data.iloc[88])