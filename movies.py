import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("movies_clean.csv")

# Streamlit app title
st.title("🎬 Movie Explorer App")

# Sidebar - Genre selection
genre_list = df["Genre"].unique()
selected_genre = st.sidebar.selectbox("Select a genre:", genre_list)

# Filter movies by selected genre
filtered_movies = df[df["Genre"] == selected_genre]

# Display filtered movies
st.subheader(f"Movies in Genre: {selected_genre}")
st.dataframe(filtered_movies)

# Bar chart of movie count per genre
st.subheader("Movies per Genre")
genre_counts = df["genres"].value_counts()

fig, ax = plt.subplots()
genre_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Genre")
ax.set_ylabel("Count")
st.pyplot(fig)
