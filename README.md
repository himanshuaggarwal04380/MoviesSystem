# 🎬 Movie Stream — Intelligent Movie Recommendation System

<p align="center">
  <strong>Discover your next movie in seconds.</strong><br>
  A sleek Netflix-inspired movie recommendation app powered by content-based machine learning and TMDB.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/ML-Content%20Based-8A2BE2?style=for-the-badge" alt="Machine Learning">
  <img src="https://img.shields.io/badge/TMDB-API-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white" alt="TMDB">
</p>

---

## 🍿 What is Movie Stream?

**Movie Stream** is a content-based movie recommendation system that helps users find movies similar to a selected title.

Choose a movie → click **Recommend** → get a curated row of similar movies with posters.

The recommendation engine uses a precomputed **movie similarity matrix**, while the TMDB API is used to retrieve movie posters dynamically.

> **Think of it as:** *"I liked this movie. What should I watch next?"* — answered by machine learning.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **Smart Recommendations** | Finds movies most similar to your selected title |
| 🧠 **Content-Based ML** | Uses precomputed similarity scores to rank movies |
| 🎬 **TMDB Posters** | Fetches high-quality movie posters through TMDB |
| 🖼️ **Fallback Posters** | Keeps the UI working even when a poster is unavailable |
| ⚡ **Cached Data** | Streamlit caching reduces repeated data/API work |
| 🔄 **Loading Spinner** | Built-in Streamlit spinner while recommendations are generated |
| 🎨 **Netflix-Inspired UI** | Dark cinematic interface with red accent styling |
| 🖱️ **Interactive Movie Carousel** | Horizontally scroll through recommendations |
| 📱 **Wide Layout** | Designed for a clean desktop viewing experience |

---

## 🖥️ Preview

> Add your application screenshot here:

```text
docs/
└── screenshot.png
```

Then replace this section with:

```markdown
![Movie Stream Screenshot](docs/screenshot.png)
```

---

## 🧩 How It Works

The application follows a simple recommendation pipeline:

```text
                 ┌────────────────────┐
                 │   Select a Movie   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Find Movie Index   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Similarity Matrix  │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Rank Similar Movies│
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Fetch TMDB Posters │
                 └─────────┬──────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ 🎬 Recommended Movies    │
              └──────────────────────────┘
```

### Recommendation logic

For the selected movie:

1. Locate the movie's index in the movie DataFrame.
2. Retrieve its corresponding row from the similarity matrix.
3. Sort all movies by similarity score in descending order.
4. Skip the selected movie itself.
5. Return the top 10 similar movies.
6. Fetch their posters from TMDB when required.
7. Display the results in an interactive horizontal carousel.

---

## 🧠 Recommendation Engine

The core recommendation function is based on a precomputed similarity matrix.

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

The system then selects the highest-scoring movies:

```text
Selected Movie
      │
      ▼
Similarity Scores
      │
      ▼
Sort ↓
      │
      ▼
Top 10
      │
      ▼
Recommendations
```

This approach makes recommendation lookup fast because the expensive similarity computation has already been performed and stored.

---

## 📁 Project Structure

```text
MovieSystem/
│
├── 📂 data/
│   ├── movie_dict.pkl
│   ├── movies.pkl
│   └── similarity.pkl
│
├── 📂 .streamlit/
│   └── secrets.toml        # Local only — do NOT commit
│
├── 📄 app.py
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 .gitignore
├── 📄 .gitattributes
└── 📂 .venv/               # Local only
```

### Important data files

| File | Purpose |
|---|---|
| `movie_dict.pkl` | Serialized movie data used by the application |
| `movies.pkl` | Movie dataset |
| `similarity.pkl` | Precomputed movie-to-movie similarity matrix |

> `similarity.pkl` is a large file, so this project uses **Git LFS** for version control.

---

## 🛠️ Tech Stack

### Application

- 🐍 **Python**
- 🎈 **Streamlit**
- 🐼 **Pandas**
- 🌐 **Requests**

### Machine Learning / Data

- Content-based recommendation
- Precomputed similarity matrix
- Serialized `.pkl` data

### External Service

- 🎬 **TMDB API** for movie poster metadata

---

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd MovieSystem
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

### 4. Configure your TMDB API key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

The application reads it using:

```python
TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
```

**Never commit `secrets.toml` to GitHub.**

### 5. Start the application

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in your terminal, usually:

```text
http://localhost:8501
```

---

## 🔐 Security

The TMDB API key should **never be hardcoded** in `app.py`.

Use Streamlit secrets:

```python
TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
```

And keep this file out of Git:

```text
.streamlit/secrets.toml
```

The `.gitignore` should include:

```gitignore
.venv/
.idea/
.streamlit/secrets.toml
```

If an API key has previously been committed to a public repository, **rotate/revoke that key** and replace it with a new one.

---

## 📦 Git LFS

The project contains a large similarity matrix:

```text
similarity.pkl
```

Because the file is larger than GitHub's normal 100 MB per-file limit, it should be tracked with Git LFS.

Initialize Git LFS:

```bash
git lfs install
```

Track the similarity matrix:

```bash
git lfs track "data/similarity.pkl"
```

Then:

```bash
git add .
git commit -m "Add movie recommendation data"
git push
```

Verify:

```bash
git lfs ls-files
```

You should see:

```text
data/similarity.pkl
```

---

## ⚡ Performance

The application uses Streamlit caching:

```python
@st.cache_data(show_spinner=False)
```

This is used for:

- Loading the serialized movie data
- Fetching movie posters

Caching helps avoid unnecessary repeated work when Streamlit reruns the application.

Poster requests also use a short timeout:

```python
requests.get(..., timeout=2)
```

If TMDB is unavailable, the application falls back to a local fallback-image list instead of breaking the recommendation page.

---

## 🎨 UI Experience

Movie Stream uses a cinematic dark interface inspired by modern streaming platforms.

### Main experience

```text
🎬 Movie Stream

Unlimited movies,
TV shows, and more.

[ Search for a movie                         ] [ Recommend > ]

More Like This

┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ Poster │ │ Poster │ │ Poster │ │ Poster │ │ Poster │
│        │ │        │ │        │ │        │ │        │
└────────┘ └────────┘ └────────┘ └────────┘ └────────┘
```

The recommendation section uses a horizontally scrollable carousel so the results remain compact and visually focused.

---

## 🔄 Error Handling

The app is designed to remain usable when external resources fail.

### Missing data files

The application checks for:

```text
data/movie_dict.pkl
data/similarity.pkl
```

and stops with a clear error if they are missing.

### TMDB unavailable

If the TMDB API fails or a movie has no poster:

```text
TMDB
  │
  ├── Poster found ──► Display TMDB poster
  │
  └── Error/missing ─► Display fallback poster
```

This prevents poster failures from crashing the application.

---

## 🧪 Example Usage

1. Launch the app.
2. Select a movie such as **John Carter**.
3. Click **Recommend >**.
4. The application calculates the closest movies using the similarity matrix.
5. A loading spinner is displayed while recommendations are being generated.
6. The top 10 recommendations appear with movie posters.

---

## 🔮 Future Improvements

Possible upgrades for the next version:

- 🔎 Add a real movie search bar
- ⭐ Show ratings and release years
- 📝 Display movie descriptions
- 🎭 Add genre and cast information
- 🎞️ Add trailers using TMDB/YouTube metadata
- ❤️ Add favorites/watchlist functionality
- 👤 Add user profiles
- 📊 Add recommendation explanations
- 🤖 Experiment with hybrid recommendation models
- 📱 Improve mobile responsiveness
- ☁️ Deploy the application online
- 🗄️ Replace local pickle files with a scalable database/object store

---

## 🌐 Deployment

The application can be deployed to a cloud platform that supports Streamlit.

Before deployment:

- Add the required TMDB secret through the platform's secret-management system.
- Make sure the model/data files are accessible.
- Configure Git LFS if the deployment environment retrieves the large similarity matrix from Git.
- Never expose your API key in source code.

---

## ⚠️ Troubleshooting

### `ModuleNotFoundError`

Install dependencies:

```bash
pip install -r requirements.txt
```

### `Missing movie_dict.pkl`

Make sure:

```text
data/movie_dict.pkl
```

exists relative to `app.py`.

### `Missing similarity.pkl`

Make sure:

```text
data/similarity.pkl
```

exists and has been downloaded correctly through Git LFS.

If Git LFS is installed:

```bash
git lfs pull
```

### Posters are not appearing

Check:

- Internet connection
- TMDB API key
- TMDB API availability
- Movie IDs in the dataset

The app should use fallback images when poster retrieval fails.

---

## 📜 License

Add your preferred license here.

For example, if you choose MIT:

```text
MIT License
```

---

## 👨‍💻 Author

**Himanshu Aggarwal**

Built as a machine-learning movie recommendation project with Python and Streamlit.

---

<p align="center">
  🎬 <strong>Movie Stream</strong><br>
  <i>Pick a movie. Press recommend. Find your next watch.</i>
</p>

<p align="center">
  ⭐ If you found this project interesting, consider starring the repository!
</p>
