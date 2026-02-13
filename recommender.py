import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/tracks_small.csv")

# Keep only needed columns
FEATURES = [
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo"
]

# Clean data
df = df.dropna(subset=["name"])
df[FEATURES] = df[FEATURES].fillna(0)

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[FEATURES])


# Recommendation function
def recommend(song_name, n=10):

    if song_name not in df["name"].values:
        return ["Song not found in dataset"]

    # Get song index
    idx = df[df["name"] == song_name].index[0]

    # Get similarity scores (on-demand)
    song_vector = scaled_features[idx].reshape(1, -1)
    similarity_scores = cosine_similarity(song_vector, scaled_features)[0]

    # Get top matches
    similar_indices = similarity_scores.argsort()[-(n+1):-1][::-1]

    # Return song + artist
    recommendations = []

    for i in similar_indices:
        song = df.iloc[i]["name"]
        artist = df.iloc[i]["artists"]
        recommendations.append(f"{song} — {artist}")

    return recommendations
