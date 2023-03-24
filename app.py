import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=cb8f7da2a43b752ae829a693da8b29d1&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/original/" + poster_path
    return full_path


def recommend(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommend_movies_names = []
    recommend_movies_posters = []
    for i in distances[1:6]:
        movie_id = movies_df.iloc[i[0]].movie_id

        recommend_movies_names.append(movies_df.iloc[i[0]].title)
        # fetch poster from API
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies_names,recommend_movies_posters


movies_df = pickle.load(open('movies.pkl', 'rb'))
# movies_df = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.header('Recmovi: Movie Recommendation App')
movie_list = movies_df['title'].values
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list)

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
# cb8f7da2a43b752ae829a693da8b29d1
