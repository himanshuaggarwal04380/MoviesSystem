<div align="center">

# 🎬 Movie Stream

### Your next movie is one recommendation away.

A cinematic, Netflix-inspired **content-based movie recommendation system** built with Python and Streamlit.

<br>

[![Live Demo](https://img.shields.io/badge/🚀%20LIVE%20DEMO-Movie%20Stream-E50914?style=for-the-badge)](https://moviessystem.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=for-the-badge&logo=github)](https://github.com/himanshuaggarwal04380/MoviesSystem)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![TMDB](https://img.shields.io/badge/TMDB-API-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white)](https://www.themoviedb.org/)

<br>

**🌐 Live:** https://moviessystem.streamlit.app/  
**💻 Source:** https://github.com/himanshuaggarwal04380/MoviesSystem

</div>

---

## 🍿 What is Movie Stream?

**Movie Stream** is a movie recommendation web application that answers one simple question:

> **"I liked this movie. What should I watch next?"**

Select a movie, press **Recommend**, and the application finds the **10 most similar movies** using a precomputed similarity matrix. Posters are retrieved dynamically through the **TMDB API**, with fallback images used when a poster cannot be loaded.

The result is a fast, visual recommendation experience with a dark streaming-platform-inspired interface.

---

## ✨ What Makes It Special?

| Feature | What it does |
|---|---|
| 🎯 **Smart Recommendations** | Finds movies closest to your selected movie |
| 🧠 **Content-Based ML** | Uses movie similarity rather than random recommendations |
| ⚡ **Fast Lookup** | Uses a precomputed similarity matrix |
| 🎬 **TMDB Integration** | Dynamically retrieves movie posters |
| 🖼️ **Fallback System** | Shows fallback posters when TMDB data is unavailable |
| 🔄 **Loading Spinner** | Displays an animated Streamlit loader while generating recommendations |
| 🎨 **Cinematic UI** | Dark background with a streaming-service-inspired design |
| 🖱️ **Movie Carousel** | Horizontally scroll through recommendations |
| 💾 **Streamlit Caching** | Avoids unnecessary repeated data/API operations |
| ☁️ **Live Deployment** | Available online through Streamlit Community Cloud |

---

## 🚀 Try It Now

### 🎬 Live Demo

**👉 [Open Movie Stream](https://moviessystem.streamlit.app/)**

No Python installation.  
No setup.  
Just open the website, select a movie, and discover something new.

---

## 🖥️ How It Works

The application follows this pipeline:

```text
                     🎬 USER
                       │
                       ▼
              ┌─────────────────┐
              │  Select a Movie │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Find Movie ID  │
              └────────┬────────┘
                       │
                       ▼
          ┌──────────────────────────┐
          │  Similarity Matrix      │
          │  Precomputed ML Scores  │
          └────────────┬─────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Rank Similarity │
              │    Scores ↓     │
              └────────┬────────┘
                       │
                       ▼
               🏆 TOP 10 MOVIES
                       │
                       ▼
          ┌──────────────────────────┐
          │       TMDB API           │
          │     Fetch Posters        │
          └────────────┬─────────────┘
                       │
                       ▼
             🎞️ MOVIE CAROUSEL
```

### Recommendation flow

When a user selects a movie:

1. The movie title is located in the dataset.
2. Its index is obtained.
3. The corresponding row from the similarity matrix is retrieved.
4. Movies are sorted by similarity score.
5. The selected movie itself is skipped.
6. The top 10 similar movies are selected.
7. Posters are retrieved from TMDB.
8. Results are displayed in a horizontal carousel.

---

## 🧠 Recommendation Engine

The core recommendation system uses a **precomputed similarity matrix**.

Conceptually:

```python
idx = movies[movies["title"] == movie_title].index[0]

sim_row = similarity[idx]

distances = sorted(
    list(enumerate(sim_row)),
    key=lambda x: x[1],
    reverse=True
)
```

The highest similarity scores represent movies that are considered most similar to the selected title.

### Why precompute the similarity?

Instead of calculating movie-to-movie similarity every time a user clicks **Recommend**, the similarity matrix is generated beforehand and stored as:

```text
data/similarity.pkl
```

This allows the application to perform recommendation lookup quickly at runtime.

---

## 🎨 User Experience

Movie Stream is designed around a simple interaction:

```text
        🎬 Movie Stream

     Unlimited movies,
     TV shows, and more.

 ┌─────────────────────────────────┐
 │ Search / Select a movie         │
 └─────────────────────────────────┘

                    ┌──────────────┐
                    │ Recommend > │
                    └──────────────┘

          ✨ More Like This

 ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
 │       │ │       │ │       │ │       │ │       │
 │ 🎬    │ │ 🎬    │ │ 🎬    │ │ 🎬    │ │ 🎬    │
 │Poster │ │Poster │ │Poster │ │Poster │ │Poster │
 │       │ │       │ │       │ │       │ │       │
 └───────┘ └───────┘ └───────┘ └───────┘ └───────┘
```

The interface includes:

- Netflix-inspired dark styling
- Red recommendation button
- Movie selector
- Animated loading spinner
- Horizontal recommendation carousel
- Hover effects on movie cards
- TMDB poster integration
- Fallback posters for failed requests

---

## 🛠️ Tech Stack

### Frontend / Application

- 🐍 **Python**
- 🎈 **Streamlit**
- 🐼 **Pandas**
- 🌐 **Requests**
- 🌐 HTML/CSS embedded inside the Streamlit interface

### Machine Learning / Data

- 🧠 Content-based recommendation
- 📊 Precomputed movie similarity matrix
- 📦 Pickle serialization

### External API

- 🎬 **TMDB API** — used for movie poster information

### Deployment

- ☁️ **Streamlit Community Cloud**
- 🐙 **GitHub**
- 📦 **Git LFS**

---

## 📁 Project Structure

```text
MoviesSystem/
│
├── 📂 data/
│   ├── movie_dict.pkl
│   ├── movies.pkl
│   └── similarity.pkl
│
├── 📂 .streamlit/
│   └── secrets.toml          # Local only — never commit
│
├── 📄 app.py                 # Main Streamlit application
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md              # Project documentation
├── 📄 .gitignore             # Ignored files/secrets
├── 📄 .gitattributes         # Git LFS configuration
│
└── 📂 .venv/                 # Local virtual environment
```

### Data files

| File | Purpose |
|---|---|
| `movie_dict.pkl` | Serialized movie data |
| `movies.pkl` | Movie dataset |
| `similarity.pkl` | Precomputed movie-to-movie similarity matrix |

> `similarity.pkl` is a large file and is stored using **Git LFS**.

---

## ⚡ Performance

The application uses Streamlit caching:

```python
@st.cache_data(show_spinner=False)
```

Caching is used for:

- Loading the movie dataset
- Loading the similarity matrix
- Fetching movie posters

This reduces repeated processing when Streamlit reruns the application.

Poster requests also use:

```python
timeout=2
```

so a slow/unavailable TMDB request does not unnecessarily block the application.

If TMDB fails, the application automatically falls back to predefined poster images.

---

## 🔐 API Security

The TMDB API key should **never be stored directly inside `app.py`**.

Use Streamlit secrets:

```python
TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
```

Local development:

```text
.streamlit/
└── secrets.toml
```

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

Make sure `.gitignore` contains:

```gitignore
.venv/
.idea/
.streamlit/secrets.toml
```

### ⚠️ Important

If an API key has ever been exposed in a public repository, rotate/revoke it and create a new one.

---

## 📦 Git LFS

The recommendation model contains a large similarity matrix:

```text
data/similarity.pkl
```

Because it is larger than GitHub's standard 100 MB file limit, the project uses **Git Large File Storage (Git LFS)**.

Initialize LFS:

```bash
git lfs install
```

Track the file:

```bash
git lfs track "data/similarity.pkl"
```

Commit and push:

```bash
git add .
git commit -m "Update recommendation model"
git push
```

Check tracked LFS files:

```bash
git lfs ls-files
```

Expected:

```text
data/similarity.pkl
```

If cloning the project and the large file appears as an LFS pointer:

```bash
git lfs pull
```

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/himanshuaggarwal04380/MoviesSystem.git
cd MoviesSystem
```

### 2. Create a virtual environment

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure TMDB

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

### 5. Start Movie Stream

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## ☁️ Deployment

This project is already deployed using **Streamlit Community Cloud**.

### Live application

👉 **https://moviessystem.streamlit.app/**

The deployment uses:

```text
GitHub Repository
       │
       ▼
Streamlit Community Cloud
       │
       ├── app.py
       ├── requirements.txt
       ├── data/
       └── Git LFS
              │
              ▼
        🌍 Public Web App
```

The TMDB API key is supplied through Streamlit's secret-management system rather than committed to the repository.

---

## 🧪 Example

Suppose the user selects:

```text
Interstellar
```

The application:

```text
Interstellar
     │
     ▼
Similarity Matrix
     │
     ▼
Rank Movies
     │
     ├── Movie A
     ├── Movie B
     ├── Movie C
     ├── Movie D
     └── ...
     │
     ▼
Top 10 Recommendations
     │
     ▼
TMDB Posters
     │
     ▼
🎬 Movie Carousel
```

---

## 🛡️ Error Handling

Movie Stream is designed to degrade gracefully.

### Missing model/data files

The app checks for required files such as:

```text
data/movie_dict.pkl
data/similarity.pkl
```

and displays an error instead of silently failing.

### TMDB poster unavailable

If:

- the API request fails,
- the movie has no poster,
- the API key is unavailable, or
- the request times out,

the application displays a fallback image.

### No recommendations

If the selected title cannot be found in the dataset, the application displays:

```text
No recommendations found.
```

---

## 🔮 Future Improvements

The current system can be expanded with:

- 🔎 Fuzzy movie search
- ⭐ Movie ratings
- 📅 Release years
- 🎭 Genres and cast
- 📝 Movie descriptions
- 🎞️ Trailers
- ❤️ Watchlist / Favorites
- 👤 User profiles
- 📊 Recommendation explanations
- 🤖 Hybrid recommendation algorithms
- 📱 Improved mobile UI
- 🗄️ Scalable database/model storage
- 📈 Recommendation analytics

---

## 📌 Project Status

```text
🟢 Application        LIVE
🟢 Recommendation    Working
🟢 TMDB Integration   Working
🟢 GitHub Repository  Public
🟢 Git LFS            Configured
🟢 Cloud Deployment   Active
```

---

## 👨‍💻 Author

### Himanshu Aggarwal

Built with Python, Streamlit, machine learning, and a little love for movies. 🎬

**Project:** [MoviesSystem on GitHub](https://github.com/himanshuaggarwal04380/MoviesSystem)  
**Live Demo:** [Movie Stream](https://moviessystem.streamlit.app/)

---

<div align="center">

### 🍿 Pick a movie.  
### ⚡ Get recommendations.  
### 🎬 Find your next watch.

<br>

**⭐ If you like the project, consider starring the repository!**

</div>
