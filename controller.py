import pandas as pd
from model import recommend

# Load cleaned dataset
movies = pd.read_csv("dataset/clean_movies.csv")

def get_movies():
    return movies['title'].values

def get_recommendations(movie):
    return recommend(movie)

