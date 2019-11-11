import numpy, pandas
import matplotlib.pyplot as plot

header = ["UserId", "MovieId", "Rating", "Timestamp"]

df = pandas.read_csv("ml-100k/u.data", sep='\t', names=header)

user_count = df.UserId.unique().shape[0]
movie_count = df.MovieId.unique().shape[0]

print("Kullanıcı sayısı:", user_count, "\nFilm sayısı:", movie_count)

print(df.head())