import os
import pickle
import requests
import streamlit as st
import pandas as pd
import random
import streamlit.components.v1 as components

TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
MOVIE_PICKLE = os.path.join(os.path.dirname(__file__), "data/movie_dict.pkl")
SIM_PICKLE = os.path.join(os.path.dirname(__file__), "data/similarity.pkl")

LOGO_URL = "https://user-images.githubusercontent.com/75604769/163835573-52bbb215-2ca0-48ad-b610-57a9aae4750a.jpg"
BACKGROUND_IMG_URL = "https://editor.analyticsvidhya.com/uploads/76889recommender-system-for-movie-recommendation.jpg"

FALLBACK_IMAGES = [
    "https://via.placeholder.com/300x450/000000/FFFFFF?text=No+Poster",
    "https://placehold.co/300x450/141414/E50914?text=Movie",
]

st.set_page_config(page_title="Movie Stream", page_icon="🎬", layout="wide")

app_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                      url('{BACKGROUND_IMG_URL}') !important;
    background-size: cover !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
    color: #FFFFFF;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}}

[data-testid="stHeader"], .block-container {{
    background: transparent !important;
}}

div[data-baseweb="select"] > div {{
    background-color: rgba(51, 51, 51, 0.8) !important;
    border-color: #333333 !important;
    color: white !important;
    border-radius: 4px;
}}
div[data-baseweb="popover"] {{
    background-color: #141414 !important;
}}
div[data-baseweb="menu"] {{
    background-color: #333333 !important;
}}
div[data-testid="stMarkdownContainer"] p {{
    color: #e5e5e5;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
}}

.stButton > button {{
    background-color: #E50914 !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: bold !important;
    padding: 0.5rem 1.5rem !important;
    font-size: 16px !important;
    transition: all 0.2s ease-in-out;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}}
.stButton > button:hover {{
    background-color: #F40612 !important;
    transform: scale(1.02);
}}

.movie-navbar {{
    display: flex;
    align-items: center;
    padding: 10px 0px;
    margin-bottom: 20px;
}}
.nav-logo {{
    height: 40px;
    margin-right: 30px;
}}
.nav-link {{
    color: #e5e5e5;
    margin-right: 20px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 300;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
}}

.hero-title {{
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 10px;
    color: #fff;
    line-height: 1.1;
    text-shadow: 2px 2px 5px rgba(0,0,0,0.9);
}}
.hero-desc {{
    font-size: 1.2rem;
    color: #fff;
    margin-bottom: 30px;
    max-width: 600px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
}}

footer {{visibility: hidden;}}
#MainMenu {{visibility: hidden;}}
</style>
"""
st.markdown(app_css, unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def load_pickles():
    if not os.path.exists(MOVIE_PICKLE):
        st.error("Missing movie_dict.pkl")
        st.stop()
    if not os.path.exists(SIM_PICKLE):
        st.error("Missing similarity.pkl")
        st.stop()

    with open(MOVIE_PICKLE, "rb") as f:
        movies_raw = pickle.load(f)
    movies = movies_raw if isinstance(movies_raw, pd.DataFrame) else pd.DataFrame(movies_raw)

    with open(SIM_PICKLE, "rb") as f:
        similarity = pickle.load(f)

    if "poster_url" not in movies.columns:
        movies["poster_url"] = ""

    return movies.reset_index(drop=True), similarity

def get_fallback_image(movie_id):
    return FALLBACK_IMAGES[int(movie_id) % len(FALLBACK_IMAGES)]

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    """Fetch a movie poster from TMDB with a deterministic fallback."""

    fallback = get_fallback_image(movie_id)

    if not TMDB_API_KEY:
        return fallback

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "api_key": TMDB_API_KEY,
            "language": "en-US"
        }

        response = requests.get(url, params=params, timeout=2)
        response.raise_for_status()

        poster_path = response.json().get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except requests.RequestException:
        pass

    return fallback


def recommend(movie_title, movies, similarity, top_k=10):
    if movie_title not in movies["title"].values:
        return [], []
    idx = movies[movies["title"] == movie_title].index[0]
    sim_row = similarity[idx]
    distances = sorted(list(enumerate(sim_row)), key=lambda x: x[1], reverse=True)

    names, posters = [], []
    for i, _ in distances[1: top_k + 1]:
        row = movies.iloc[i]
        names.append(row["title"])

        poster = ""
        if "poster_url" in row.index and row.get("poster_url"):
            poster = row.get("poster_url")
        else:
            movie_id = row.get("movie_id") or row.get("id")
            poster = fetch_poster(movie_id) if movie_id else random.choice(FALLBACK_IMAGES)
        posters.append(poster)
    return names, posters

st.markdown(f"""
<div class="movie-navbar">
    <img src="{LOGO_URL}" class="nav-logo">
</div>
""", unsafe_allow_html=True)

try:
    movies, similarity = load_pickles()
except Exception as e:
    st.error(str(e))
    st.stop()

st.markdown('<div class="hero-title">Unlimited movies,<br>TV shows, and more.</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-desc">Select a movie below to get similar recommendations instantly.</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])
with col1:
    selected_movie = st.selectbox(
        "Search for a movie",
        movies["title"].values,
        index=0,
        label_visibility="collapsed"
    )
with col2:
    show_recommendations = st.button("Recommend >")

if show_recommendations:

    with st.spinner("Finding similar movies..."):

        names, posters = recommend(
            selected_movie,
            movies,
            similarity,
            top_k=10
        )

    st.write("### More Like This")

    if not names:
        st.warning("No recommendations found.")
    else:
        scroll_css = """
        <style>
        body { margin: 0; background: transparent; font-family: 'Helvetica Neue', Arial, sans-serif; }

        .movie-carousel {
            display: flex;
            overflow-x: auto;
            overflow-y: hidden;
            padding: 20px 0 20px 20px;
            gap: 10px;
            scroll-behavior: smooth;
        }

        .movie-carousel::-webkit-scrollbar { display: none; }
        .movie-carousel { -ms-overflow-style: none; scrollbar-width: none; }

        .card {
            flex: 0 0 auto;
            width: 160px;
            cursor: pointer;
            transition: transform 0.3s ease;
            position: relative;
        }
        .card:hover { transform: scale(1.1); z-index: 10; }
        .poster { width: 100%; height: 240px; object-fit: cover; border-radius: 4px; }
        .title { color: #e5e5e5; font-size: 13px; margin-top: 8px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; text-align: center; text-shadow: 1px 1px 2px rgba(0,0,0,0.8); }
        </style>
        """

        html_content = '<div class="movie-carousel">'
        for name, poster in zip(names, posters):
            safe_poster = poster if poster else "https://via.placeholder.com/160x240"
            safe_name = name.replace("'", "&apos;")
            card = f"""
            <div class="card" title="{safe_name}">
                <img class="poster" src="{safe_poster}" onerror="this.src='https://via.placeholder.com/160x240?text=N'">
                <div class="title">{safe_name}</div>
            </div>
            """
            html_content += card
        html_content += "</div>"

        full_html = f"<html><head>{scroll_css}</head><body>{html_content}</body></html>"
        components.html(full_html, height=320)