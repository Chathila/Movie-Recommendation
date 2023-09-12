import streamlit as st
import pickle
from main import reccomender
import numpy as np

with open("movies_list.pkl", "rb") as file:
    movies = pickle.load(file)  

st.header("Having trouble finding a good movie to watch?")
selected_movie = st.selectbox("Select a movie from the dropdown menu",movies['title'])

if st.button("Show Recommendation"):
    recommendations,posters = reccomender(selected_movie)  # Assuming this returns a list of movie titles as recommendations
    for i, recommendation in enumerate(recommendations):
    
        st.write(recommendation)  # Display the movie title on the left
        
        # Create a container next to the title
        col1, col2 = st.columns([1, 2])
        
        # Display the poster in col1
        with col1:
            st.markdown(
                f'''<div>
                        <img src="{posters[i]}" style="width: 50%; max-width: 220px; height: auto;">
                    </div>
                ''',
                unsafe_allow_html=True
            )
           
        
        # Display the "More Info" button in col2
        with col2:
            with st.container():
                st.markdown(
                    f"""
                    <div style="border: 2px solid #FAFAFA;border-radius: 10px; padding: 10px;">
                        <p>Description: Description for {recommendation}</p>
                        <p>Release Date: Release date for {recommendation}</p>
                        <a href="TRAILER_URL">Watch Trailer</a>
                    </div>
                    """,
                    unsafe_allow_html= True)
        
            