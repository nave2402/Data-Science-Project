import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Upload the Fandango data
Fandango_data = pd.read_csv("./06-Capstone-Project/fandango_scrape.csv")

# Exploring the Fandango data
print(Fandango_data.head())
print(Fandango_data.info())
print(round(Fandango_data.describe(), 1))


# Printing the scatterplot (the relationship between popularity of a film and it's rating)
fig, ax = plt.subplots(figsize=(7, 3), dpi=150)
Fandango_scatter = sns.scatterplot(x="RATING", y="VOTES", data=Fandango_data)
plt.title("Relationship between popularity of a film and it's rating")
plt.xlabel("User Rating")
plt.ylabel("Votes Number")
plt.tight_layout()
plt.show()

# Checking the correlation stars with rating
Fandango_correlation = Fandango_data.corr()
print(Fandango_correlation)


# Special function for export the tear from the FILM column
def Year(str):
    Year = str[-6:]
    Year = Year.replace('(', '')
    Year = Year.replace(')', '')
    return Year


# Activate the function and create a new column
Fandango_data["YEAR"] = Fandango_data["FILM"].apply(Year)

# Counting how many movies there were each year)
print(Fandango_data["YEAR"].value_counts())

# Printing the barplot (Show how many movies there were each year)
fig, ax = plt.subplots(figsize=(7, 3), dpi=150)
sns.histplot(data=Fandango_data, x='YEAR', hue='YEAR', edgecolor='black', lw=2)
plt.title("Movie per Year")
plt.xlabel("Year")
plt.ylabel("Amount of movies")
plt.ylim(0, 500)
plt.tight_layout()
plt.show()

# Sort the top 10 number of votes
print(Fandango_data.sort_values("VOTES", ascending=False)[:10])
# Sort and remove all rows where the number of votes is equal to zero
fan_reviewed = Fandango_data[Fandango_data['VOTES'] > 0]

# Printing a KDEplot that compering between the true rating vs stars display
fig, ax = plt.subplots(figsize=(8, 4), dpi=150)
fan_kde = sns.kdeplot(data=fan_reviewed, x='RATING', clip=[0, 5], fill=True, label='True Rating')
fan_kde = sns.kdeplot(data=fan_reviewed, x='STARS', clip=[0, 5], fill=True, label='Stars Display')
plt.title("True Rating vs Stars Display")
plt.legend(loc=(0.008, 0.84))
plt.tight_layout()
plt.show()

# Create a new column in a new dataframe that show the difference between the stars rating and the true rating
fan_reviewed["STARS_DIFF"] = round(fan_reviewed["STARS"]-fan_reviewed["RATING"], 1)
# Defines a new index (film name)
fan_reviewed = fan_reviewed.set_index("FILM")

# Printing a countplot to display the number of times a certain difference occurs
fig, ax = plt.subplots(figsize=(8, 4), dpi=150)
sns.countplot(x='STARS_DIFF', data=fan_reviewed,palette='magma')
plt.title("The difference between site ranking for user ratings")
plt.xlabel("Rating difference")
plt.show()

# Showing the exceptional result
print(fan_reviewed[fan_reviewed['STARS_DIFF'] == 1])
