import streamlit as st
import pickle
from main import reccomender
import requests

with open("movies_list.pkl", "rb") as file:
    movies = pickle.load(file)  

st.header("Having trouble finding a good movie to watch?")
selected_movie = st.selectbox("Select a movie from the dropdown menu",movies['title'])

if st.button("Show Recommendation"):
    recommendations,posters = reccomender(selected_movie)  # Assuming this returns a list of movie titles as recommendations
    columns = st.columns(5)

    for i, recommendations[0] in enumerate(recommendations):
        with columns[i % 5]:  # Ensure that you don't exceed the number of columns (limit to 5 columns)
            st.markdown(
                f"<div style='display: flex; flex-direction: column; align-items: center;'>"
                f"    <p style='text-align: center;'>{recommendations[i]}</p>"
                f"    <div style='margin-top: 10px; text-align: center;'>"
                f"        <img src='{posters[i]}' style='width: 100%; max-width: 170px;'>"
                f"    </div>"
                f"</div>",
                unsafe_allow_html=True)
            #st.image(posters[i])
            

