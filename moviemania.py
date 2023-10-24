import streamlit as st
import pandas as pd

# Create a dictionary of movies and their genres (for demonstration)
movie_data=pd.read_csv("movies.csv")
movie_df = pd.DataFrame(movie_data)

# Create the Streamlit web app
st.title('Movie Recommendation System')

# Sidebar
st.sidebar.header('User Input')

# User input for selecting a genre
selected_genre = st.sidebar.selectbox('Select a Genre', movie_df['Genre'].unique())

# Display selected genre
st.sidebar.write(f'Selected Genre: {selected_genre}')

# Main content
st.header('Top Movies in Selected Genre')

# Filter movies by selected genre
filtered_movies = movie_df[movie_df['Genre'] == selected_genre]

# Display filtered movies
st.write(filtered_movies)

# Recommendation system logic (you should replace this with your recommendation algorithm)
# For demonstration, it recommends the first movie from the selected genre
if not filtered_movies.empty:
    recommendation = filtered_movies.iloc[0]['Movie']
    st.header('Movie Recommendation')
    st.write(f"We recommend watching: {recommendation}")

# Optionally, you can add more information about the recommended movie
# such as its description, poster, etc.

# Example: Movie description
# st.subheader('Movie Description')
# movie_description = "This is a great movie you should watch!"
# st.write(movie_description)

# Example: Movie poster
# st.subheader('Movie Poster')
# movie_poster_url = 'https://example.com/movie_poster.jpg'
# st.image(movie_poster_url, caption='Movie Poster', use_column_width=True)

