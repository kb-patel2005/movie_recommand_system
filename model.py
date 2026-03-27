import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned dataset
movies = pd.read_csv("dataset/clean_movies.csv")

# Create CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

# Convert tags into vectors
vectors = cv.fit_transform(movies['tags']).toarray()

# Compute similarity matrix
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
    except IndexError:
        return []

    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)),
                        reverse=True,
                        key=lambda x: x[1])[1:6]

    recommended = []

    for i in movie_list:
        movie_data = movies.iloc[i[0]]   # ✅ define here

        recommended.append({
            "title": movie_data['title'],       # ✅ use dict style (safer)
            "overview": movie_data['overview']
        })

    return recommended

# Example usage
if __name__ == "__main__":
    print(recommend("Avatar"))