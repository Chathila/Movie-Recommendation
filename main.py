import pandas as pd
#the bag of words method
#the library scikit learn is used for machine learnt aspect
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import requests

movies = pd.read_csv('movies_dataset.csv') #reads from the csv file

#creates the new dataframe that we are going to train our ML model
movies_dataframe = movies[['id','title','genre','overview']]
movies_dataframe['description']= movies_dataframe['overview'] + movies_dataframe['genre']
training_dataframe = movies_dataframe.drop(columns = ['overview','genre'])



'''CountVectorizer is a tool for creating a BoW representation of text data.
max_features=10000 because we have 10000 movies in our dataset
stop_words='English' removes common English stopwords, which are often discarded in BoW representations'''
cv = CountVectorizer(max_features=10000, stop_words='english') # an object of class CountVectorizer is cv

"""the variable vector will hold a NumPy array that represents the document-term matrix based on the
'description' column of your training_dataframe. Each row in vector corresponds to a 
description, and each column represents a word from the vocabulary, with values indicating word 
counts in each description."""
data = training_dataframe['description'].values.astype('U')
vector = cv.fit_transform(data).toarray()

"""Going to use cosine angle similarity to find the similiar movies.we can imagine every movie to be
a vector in a 3d vector in a cartisean plane. if the angle between the 2 vectors is small the movies
can be consider to be similar, and i am going to filter for the top 5 similar movies to the movie 
given by the user. Movie_similarity is a matrix where each cell (i, j) contains the cosine similarity between 
movie i and movie j, as computed based on their descriptions"""
movie_similarity = cosine_similarity(vector)

def get_movie_poster(movieID):
    url = "https://api.themoviedb.org/3/movie//{}?api_key=b6661c17a56ebdaef713ebf2167d0b38".format(movieID)
    data = requests.get(url)
    data = data.json()
    pathToPoster = data['poster_path']
    
    fullPathToPoster = "https://image.tmdb.org/t/p/w500/" + pathToPoster
    return fullPathToPoster

def get_movie_details(movieID):
    url = "https://api.themoviedb.org/3/movie//{}?api_key=b6661c17a56ebdaef713ebf2167d0b38".format(movieID)
    response = requests.get(url)
    data = response.json()
    genresAPI = data.get("genres")
    genres = [genre["name"] for genre in genresAPI]
    releaseDate = data.get("release_date")
    matching_movie = movies_dataframe[movies_dataframe['id'] == movieID]
    description = matching_movie.iloc[0]['overview']
    return genres, releaseDate, description
    
def reccomender(movie,numRecommendations):
    id = training_dataframe[training_dataframe['title']== movie].index[0]
    similarity_list = list(enumerate(movie_similarity[id]))
    sorted_similarity_list = sorted(similarity_list, key=lambda x: x[1], reverse=True)
    recommendation = []
    posters = []
    movie_ids = []
    for i in sorted_similarity_list[1:numRecommendations+1]:
        id = training_dataframe.loc[i[0]]['id']
        movie_ids.append(id)
        recommendation.append(training_dataframe.loc[i[0]]['title'])
        posters.append(get_movie_poster(id))
    return recommendation,posters,movie_ids

pickle.dump(training_dataframe, open('movies_list.pkl','wb'))









