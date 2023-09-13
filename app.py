import streamlit as st
import pickle
from main import reccomender, get_movie_details
import numpy as np

with open("movies_list.pkl", "rb") as file:
    movies = pickle.load(file)  

numbers = [1,2,3,4,5,6,7,8,9,10]

st.markdown(f"<p style='font-size: 45px; font-weight: bold;margin-bottom: 10px;margin-top: 20px;'>Having trouble finding a good movie to watch?</p>", unsafe_allow_html=True)
selected_movie = st.selectbox("Select a movie from the dropdown menu",movies['title'])
numRecommendations = st.selectbox("Type in the number of recommendations you need",(numbers))

if st.button("Show Recommendation"):
    recommendations,posters, recommended_IDs = reccomender(selected_movie, numRecommendations)  # Assuming this returns a list of movie titles as recommendations

    st.markdown(f"<p style='font-size: px; font-weight: bold;margin-bottom: 10px;margin-top: 20px;'>Showing movies similar to : {selected_movie}</p>", unsafe_allow_html=True)

    for  i, recommendation in enumerate(recommendations):
    
        title_html = f"<p style='font-size: 30px; font-weight: bold;margin-bottom: 10px;margin-top: 20px;'>{i+1}. {recommendation}</p>"
        st.markdown(title_html, unsafe_allow_html=True)
        
        # Create a container next to the title
        col1, col2 = st.columns([1, 2])
        
        # Display the poster in col1
        with col1:
            st.markdown(
                f'''<div>
                        <img src="{posters[i]}" style="width: 100%; max-width: 300px; height: auto;">
                    </div>
                ''',
                unsafe_allow_html=True
            )
 
        genres, releaseDate, description= get_movie_details(recommended_IDs[i])
        genre_string =  ", ".join(genres)
        str_recommendation = str(recommendation)+ " trailer"
        str_recommendation = str_recommendation.replace(" ","+")
        Yt_search = "https://www.youtube.com/results?search_query=" + str_recommendation
        
        with col2:
            with st.container():
                st.markdown(
                    f"""
                    <div style="border: 4px solid #FAFAFA;border-radius: 10px; padding: 10px;">
                        <p style='font-size: 22px; font-weight: bold;margin-bottom: 10px;margin-top: 20px;'>Release Date: <p> {releaseDate}</p>
                        <p style='font-size: 22px; font-weight: bold;margin-bottom: 10px;margin-top: 20px;'> Genres: <p> {genre_string}</p>
                        <p style='font-size: 22px; font-weight: bold;margin-bottom: 10px;margin-top: 20px;'>Description:<p> {description}</p>
                        <a href={Yt_search}>Watch Trailer</a>
                    </div>
                    """,
                    unsafe_allow_html= True)
        
            
            
