import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the data from a .csv file
@st.cache(allow_output_mutation=True)
def load_data(filename):
    data = pd.read_csv(filename)
    return data

def recommend_movies(movie_title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = movies_df[movies_df['title'] == movie_title].index[0]
    
    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]
    
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the top 10 most similar movies
    return movies_df['title'].iloc[movie_indices]

# Load the data from a .csv file
movies_df = load_data('movies.csv')

# Set up the app layout
st.title('Movie Recommendation System')

movie_title = st.text_input('Enter a movie title', 'Toy Story (1995)')

if st.button('Recommend'):
    similar_movies = recommend_movies(movie_title)
    st.write('Recommended Movies:'+ ', '.join(similar_movies))
