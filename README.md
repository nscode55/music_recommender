# 🎵 Music Recommendation System

A Machine Learning–based Music Recommendation System that suggests songs based on audio similarity using Spotify track features.

This project uses content-based filtering and cosine similarity to recommend songs similar to a user-selected track. It is deployed with an interactive Streamlit web application.

---

## 📌 Project Overview

Music streaming platforms contain millions of songs, making it difficult for users to discover music tailored to their preferences.

This system analyzes Spotify audio features such as danceability, energy, tempo, and valence to generate personalized music recommendations.

---

## 🚀 Features

* 🎧 Content-based music recommendations
* 📊 Audio feature similarity analysis
* ⚡ On-demand cosine similarity (memory efficient)
* 🖥️ Interactive Streamlit web interface
* 🎤 Displays song + artist recommendations
* 📁 Works with large Spotify datasets

---

## 🧠 Machine Learning Concepts Used

* Content-Based Filtering
* Feature Scaling (Standardization)
* Cosine Similarity
* Vector Similarity Search

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Streamlit**

---

## 📂 Dataset

Spotify Tracks Dataset (Kaggle)

Dataset contains:

* Track name
* Artists
* Popularity
* Danceability
* Energy
* Loudness
* Tempo
* Valence
* Acousticness
* Instrumentalness

---

## 🏗️ System Architecture

1. User selects a song
2. System extracts audio features
3. Features are standardized
4. Cosine similarity is computed
5. Top similar songs are retrieved
6. Recommendations displayed in UI

---

## 📁 Project Structure

```
music-recommender/
│
├── data/
│   └── tracks.csv
│
├── recommender.py      # ML recommendation logic
├── app.py              # Streamlit UI
├── requirements.txt
└── README.md
```

---

###  Install Dependencies

```bash
pip install -r requirements.txt
```

---

###  Run Application

```bash
streamlit run app.py
```

## ⭐ Acknowledgements

* Spotify Dataset — Kaggle
* Scikit-learn Documentation
* Streamlit Community

---

## 📜 License

This project is open-source and available under the MIT License.
