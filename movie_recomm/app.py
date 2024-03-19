import streamlit as st
import pandas as pd
import pickle
import requests
def fetch_poster(movie_id):
    response= requests.get("https://api.themoviedb.org/3/movie/{}?api_key=f9087c57cd87131a54517f5f247fb6d7&language=en-US".format(movie_id))
    data= response.json()
    return  "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    mid= moviess[moviess['title']==movie].index[0]
    distances= similarity[mid]
    movies_list= sorted(list(enumerate(distances)),reverse=True, key= lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id= moviess.iloc[i[0]].id
        recommended_movies.append(moviess.iloc[i[0]].title)
    # return recommended_movies
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

mdict= pickle.load(open("C:\\Users\\nayak\\Desktop\\movie_recomm\\movies_dict.pkl",'rb'))
moviess= pd.DataFrame(mdict)
similarity = pickle.load(open("C:\\Users\\nayak\\Desktop\\movie_recomm\\similarity.pkl","rb"))
st.title('Movie Recommender System')
selectedmoviename = st.selectbox(
    'How would you like to be contacted?',
    moviess['title'].values)

if st.button('recommend'):
    # reccomendations= recommend(selectedmoviename)

    # for i in reccomendations:
        # st.write(i)
    names, posters=recommend(selectedmoviename)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])