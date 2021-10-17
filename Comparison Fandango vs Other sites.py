import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




Fandango_data = pd.read_csv("./06-Capstone-Project/fandango_scrape.csv")
All_sites_data = pd.read_csv("./06-Capstone-Project/all_sites_scores.csv")
# united data
all_data = pd.merge(Fandango_data, All_sites_data, how='inner', on='FILM')

# Normalize the data
all_data[['RottenTomatoes', 'Metacritic','RottenTomatoes_User']] = all_data[['RottenTomatoes',
          'Metacritic', 'RottenTomatoes_User']] / 10

all_data[['RottenTomatoes', 'Metacritic','IMDB', 'Metacritic_User',
          'RottenTomatoes_User']] = all_data[['RottenTomatoes',
          'Metacritic', 'IMDB', 'Metacritic_User', 'RottenTomatoes_User']] / 2
# change columns names
all_data = all_data.rename({'FILM': 'Film_name', 'STARS': 'Fandango_rt',
                            'RATING': 'Fandango_user_rt', 'VOTES': 'Fandango_votes_num',
                            'RottenTomatoes': 'RottenTomatoes_rt', 'RottenTomatoes_User': 'RottenTomatoes_User_rt',
                            'Metacritic': 'Metacritic_rt', 'Metacritic_User': 'Metacritic_User_rt',
                            'IMDB': 'IMDb_user_rt', 'Metacritic_user_vote_count': 'Metacritic_votes_num',
                            'IMDB_user_vote_count': 'IMDb_votes_num'}, axis=1)

# add year column (from the film column)
def Year(str):
    Year = str[-6:]
    Year = Year.replace('(', '')
    Year = Year.replace(')', '')
    return Year


all_data["Year"] = all_data["Film_name"].apply(Year)
# set film name the index
all_data = all_data.set_index("Film_name")


# plot comparing the distributions of normalized ratings across all sites
fig, ax = plt.subplots(figsize=(6, 8), dpi=150)
IMDb_kde = sns.kdeplot(data=all_data,x='IMDb_user_rt', clip=[0, 5], fill=True, palette='Set1',label='IMDB Rating')
Metacritic_kde = sns.kdeplot(data=all_data, x='Metacritic_rt', clip=[0, 5], fill=True, label='Metacritic Rating')
Metacritic_user_kde = sns.kdeplot(data=all_data, x='Metacritic_User_rt', clip=[0, 5], fill=True, label='Metacritic User Rating')
fan_kde = sns.kdeplot(data=all_data, x='Fandango_rt', clip=[0, 5], fill=True, label='Fandango Rating')
fan_user_kde = sns.kdeplot(data=all_data, x='Fandango_user_rt', clip=[0, 5], fill=True, label='Fandango User Rating')
RT_kde = sns.kdeplot(data=all_data, x='RottenTomatoes_rt', clip=[0, 5], fill=True, label='RottenTomatoes Rating')
RT_user_kde = sns.kdeplot(data=all_data, x='RottenTomatoes_User_rt', clip=[0, 5], fill=True, label='RottenTomatoes User Rating')
plt.title("Comparing the distributions of normalized ratings across all sites")
plt.legend(loc=(0.01, 0.61))
plt.ylim(0, 1)
plt.xlabel("Stars Rating")
plt.show()

# The distribution of RT critic ratings against the STARS displayed by Fandango
fig, ax = plt.subplots(figsize=(6, 8), dpi=150)
fan_kde = sns.kdeplot(data=all_data, x='Fandango_rt', clip=[0, 5], fill=True, label='Fandango Rating')
RT_kde = sns.kdeplot(data=all_data, x='RottenTomatoes_rt', clip=[0, 5], fill=True, label='RottenTomatoes Rating')
plt.title("The distribution of RT critic ratings against the STARS displayed by Fandango")
plt.legend(loc=(0.008, 0.87))
plt.ylim(0, 1)
plt.xlabel("Stars Rating")
plt.show()

# histplot comparing all normalized scores
final_data = all_data[['Fandango_rt', 'Fandango_user_rt', 'RottenTomatoes_rt',
                       'RottenTomatoes_User_rt', 'Metacritic_rt', 'Metacritic_User_rt',
                       'IMDb_user_rt']]
fig, ax = plt.subplots(figsize=(6, 8), dpi=150)
histplot = sns.histplot(data=final_data, bins=50)
plt.title("Histplot comparing all normalized scores")
plt.xlabel("Stars Rating")
plt.show()

# A clustermap thow the difference in bad movies
sns.clustermap(final_data, col_cluster=False, figsize=(12, 8))
plt.legend(loc=(1.05, 0.87))
plt.show()

# worst films by RT
worst_films = final_data.nsmallest(10, 'RottenTomatoes_rt')
print(worst_films)
fig, ax = plt.subplots(figsize=(10,5),dpi=150)
sns.kdeplot(data=worst_films,clip=[0,5],shade=True,palette='Set1')
plt.title("The worst movies")
plt.show()


