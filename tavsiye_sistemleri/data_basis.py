import numpy, pandas
import matplotlib.pyplot as plot

header = ["UserId", "MovieId", "Rating", "Timestamp"]

df = pandas.read_csv("ml-100k/u.data", sep='\t', names=header)

def show():
    """Veri kümesinin feature sayılarını ve ilk 5 satırını gösterir.
    Kitapta Kod 2.1."""
    print("Kullanıcı sayısı:", df.UserId.unique().shape[0], "\nFilm sayısı:", df.MovieId.unique().shape[0])

    print(df.head())

def plt():
    """Plot'u ayarlar, hangi dereceden kaç adet basıldığını gösterir.
    Kitapta Kod 2.2."""
    plot.rc("font", size=10) # Check the doc
    df.Rating.value_counts(sort=False).plot(kind="bar")
    plot.title("Değerlendirme Dağılımı")
    plot.xlabel("Değer")
    plot.ylabel("Beğeni Sayısı")

    plot.show()

def avg():
    df_avg = pandas.DataFrame(round(df.groupby('MovieId')['Rating'].mean(),2))
    df_avg['DsTemp'] = pandas.DataFrame(df.groupby('MovieId')['Rating'].count())
    df_avg.columns = ['AvgRating', '#Rating']
    return df_avg.sort_values('#Rating', ascending=False)
