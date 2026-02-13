import streamlit as st
import pandas as pd
from recommender import recommend

st.set_page_config(page_title="Music Recommender", layout="wide")

st.title("🎵 Music Recommendation System")
st.write("Select a song and get personalized music recommendations!")

# Load dataset
df = pd.read_csv("data/tracks_small.csv")

# Song dropdown
song_list = df["name"].dropna().unique()

selected_song = st.selectbox(
    "Select a Song",
    sorted(song_list)
)

# Recommend button
if st.button("Recommend"):

    recommendations = recommend(selected_song)

    st.subheader("Recommended Songs 🎧")

    for i, song in enumerate(recommendations, 1):
        st.write(f"{i}. {song}")
