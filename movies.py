import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Load the dataset
df = pd.read_csv("movies_clean.csv")

#Streamlit app title
st.title("🎬 Movie Explorer App")

#Sidebar - Genre selection
genre_lit = df["genres"].unique()
selected_genre = st.sidebar.selectbox("Select a genres:", genre_list)

#Filter movies by selected genre
filtered_movies = df[df["genres"] == selected genre]

#Display filtered movies
st.subheader(f"Movies in Genre: {selected_genre}")
st.dataframe(filtered_movies)

#Bar chart of movie count per genre
st.subheader("Movies per Genre")
genre_counts = df["genres"].valuecounts()
st.pyplot(fig)
