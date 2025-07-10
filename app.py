
import streamlit as st
import pandas as pd
import pickle
import difflib

# Load the dataset and similarity matrix
movies_data = pd.read_csv('movies_data.csv')
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favorite one based on genre and production country.")

# Input box for user
movie_name = st.text_input("Enter your favorite movie title:")

# When user clicks the recommend button
if st.button("Recommend"):
    list_of_all_titles = movies_data['TITLE'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles, n=1, cutoff=0.5)

    if find_close_match:
        close_match = find_close_match[0]
        st.success(f"Showing recommendations for: **{close_match}**")

        # Get index of the movie
        index_of_movie = movies_data[movies_data.TITLE == close_match]['index'].values[0]

        # Get similarity scores
        similarity_score = list(enumerate(similarity[index_of_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.subheader("🎥 Recommended Movies:")

        i = 1
        for movie in sorted_similar_movies[1:11]:  # skip the first (itself)
            index = movie[0]
            title = movies_data[movies_data.index == index]['TITLE'].values[0]
            st.write(f"{i}. {title}")
            i += 1
    else:
        st.error("❌ No close match found. Please try again or check spelling.")
