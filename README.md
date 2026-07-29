# 🎬 Movie Recommendation System

A Netflix-inspired Movie Recommendation System built with **Python** and **Streamlit**. The application recommends similar movies based on the user's selection using a content-based recommendation algorithm and displays movie posters fetched from The Movie Database (TMDB).

---

## 🚀 Features

- Recommend movies similar to the selected movie.
- Beautiful Netflix-style user interface.
- Fetches movie posters dynamically using the TMDB API.
- Fast recommendations using a precomputed similarity matrix.
- Simple and interactive Streamlit web application.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Pickle
- Requests
- TMDB API

---

## 📂 Project Structure

```
MovieSystem/
│
├── app.py                 # Main Streamlit application
├── movie_dict.pkl         # Movie metadata
├── similarity.pkl         # Similarity matrix
├── movies.pkl             # Movie dataset
├── requirements.txt       # Python dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/MovieSystem.git
cd MovieSystem
```

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📖 How It Works

1. The movie dataset is loaded from `movie_dict.pkl`.
2. A precomputed similarity matrix (`similarity.pkl`) is loaded.
3. When a user selects a movie, the system finds the most similar movies.
4. Movie posters are fetched from the TMDB API.
5. The recommendations are displayed in the Streamlit interface.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
screenshots/home.png
screenshots/recommendations.png
```

---

## 📦 Dataset

The project uses a preprocessed movie dataset along with a similarity matrix generated offline.

---

## 🔑 TMDB API

Movie posters are fetched using The Movie Database (TMDB) API.

To use your own API key, replace the value of:

```python
TMDB_API_KEY = "YOUR_API_KEY"
```

inside `app.py`.

---

## 📌 Future Improvements

- Movie search
- Genre filtering
- IMDb ratings
- Trailer support
- User authentication
- Collaborative filtering
- Hybrid recommendation system

---

## 👨‍💻 Author

**Himanshu Aggarwal**

GitHub: https://github.com/himanshuaggarwal04380

---

## 📄 License

This project is intended for educational and learning purposes.