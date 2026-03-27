import pandas as pd

def clean_dataset():
    movies = pd.read_csv("dataset/tmdb_5000_movies.csv")

    # Select important columns
    movies = movies[['title', 'genres', 'keywords', 'overview']]


    # Remove null values
    movies = movies.dropna()

    # Convert text to lowercase
    movies['overview'] = movies['overview'].str.lower()

    # Remove special characters
    movies['overview'] = movies['overview'].str.replace('[^a-zA-Z ]', '', regex=True)

    # Create tags column
    movies['tags'] = movies['overview'] + " " + movies['genres'] + " " + movies['keywords']

    # Save cleaned dataset
    movies.to_csv("dataset/clean_movies.csv", index=False)

    return movies

if __name__ == "__main__":
    clean_dataset()
    print("Dataset cleaned and saved as clean_movies.csv")