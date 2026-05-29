import pandas as pd

d = pd.read_csv('movies.csv')
print(d.head(11))  # print(d), to print the entire data


Film = d.groupby('Film').groups
print(Film)


Genre = d.groupby(['Film','Genre']).groups
print(Genre)

for i in Genre:
    print(i)

total_rotten_tomato_and_Audience_score_percentage = d.groupby('Film').agg(
    movies = ('Film' , 'count'),
    Rotten_tomato_max = ('Rotten Tomatoes %' , 'max'),
    Audience_score_count = ('Audience score %' , 'count')
).reset_index()
print(total_rotten_tomato_and_Audience_score_percentage) # to filter the data