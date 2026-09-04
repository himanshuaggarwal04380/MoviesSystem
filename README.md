🎬 Movie Stream — Content-Based Movie Recommendation System

<p align="center">
  <strong>Discover your next movie with intelligent, content-based recommendations.</strong><br>
  A Netflix-inspired Streamlit application that finds movies similar to what you already love.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/TMDB-Movie%20Posters-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white" alt="TMDB">
</p>

✨ Overview

Movie Stream is an interactive movie recommendation web app built with Python and Streamlit. Select a movie and the application instantly returns a carousel of movies with similar content.

Instead of relying on user ratings or viewing history, the system uses a content-based recommendation approach. A precomputed similarity matrix compares movies using their processed metadata/tags, allowing recommendations to be generated quickly at runtime.

Movie posters are retrieved dynamically from The Movie Database (TMDB) API, with fallback images used when a poster cannot be loaded.

🎯 What the Project Does

                    ┌─────────────────────┐
                    │   User selects a    │
                    │       movie         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Find movie index in │
                    │   movie metadata    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Read precomputed    │
                    │ similarity scores   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Rank most similar   │
                    │      movies         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Fetch TMDB posters  │
                    │   + show carousel   │
                    └─────────────────────┘

🚀 Features

Feature

Description

🎞️ Movie Selection

Choose a movie from the available catalog using an interactive selector.

🧠 Content-Based Recommendations

Finds movies with similar metadata/tags rather than depending on user ratings.

⚡ Fast Inference

Uses a precomputed similarity matrix instead of recalculating similarity for every request.

🖼️ Dynamic Posters

Retrieves movie posters from TMDB when local poster URLs are unavailable.

🎨 Netflix-Inspired UI

Dark cinematic background, bold typography, red action buttons and poster cards.

↔️ Horizontal Carousel

Recommendations are presented in a scrollable movie-card layout.

💾 Cached Data

Streamlit caching reduces repeated loading and API requests.

🛡️ Poster Fallbacks

Placeholder images keep the interface usable when a poster is missing or unavailable.

🛠️ Tech Stack

Python — application logic

Streamlit — interactive web interface

Pandas — movie-data handling

NumPy — similarity-matrix processing

Requests — TMDB API requests

Pickle — loading precomputed recommendation artifacts

TMDB API — movie poster retrieval

HTML/CSS — custom movie carousel and visual styling

📁 Project Structure

MovieSystem/
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Git ignore rules
│
├── data/
│   ├── movie_dict.pkl         # Movie lookup metadata
│   ├── movies.pkl             # Processed movie dataset
│   └── similarity.pkl         # Precomputed movie-to-movie similarity matrix
│
└── .venv/                     # Local virtual environment (not required in Git)

Dataset artifacts

The bundled movies.pkl contains 4,806 movies with the following fields:

movie_id

title

tags

The similarity.pkl artifact contains a 4,806 × 4,806 similarity matrix used to retrieve recommendations efficiently.

⚙️ Getting Started

1. Clone the repository

git clone https://github.com/himanshuaggarwal04380/MovieSystem.git
cd MovieSystem

2. Create a virtual environment

Windows

python -m venv .venv
.venv\Scripts\activate

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure TMDB

The application uses TMDB to retrieve movie posters.

For a safer setup, store the API key as an environment variable instead of committing it directly to source control.

Windows PowerShell

$env:TMDB_API_KEY="YOUR_TMDB_API_KEY"

macOS / Linux

export TMDB_API_KEY="YOUR_TMDB_API_KEY"

Then configure app.py to read the environment variable:

TMDB_API_KEY = os.getenv("TMDB_API_KEY", "")

Security note: Never publish a real API key in a public GitHub repository. If an API key has already been exposed, rotate/revoke it from your TMDB account.

5. Run the application

streamlit run app.py

Streamlit will provide a local URL, normally similar to:

http://localhost:8501

Open it in your browser and start exploring movies.

🧠 Recommendation Logic

The recommendation engine is implemented in recommend() inside app.py.

At a high level:

The selected movie title is located in the movie dataset.

Its corresponding row is retrieved from the similarity matrix.

Movies are paired with their similarity scores.

Scores are sorted from highest to lowest.

The selected movie itself is skipped.

The top 10 similar movies are returned.

Posters are obtained from existing poster URLs or TMDB.

Results are rendered as a horizontal carousel.

Conceptually:

Selected Movie
      ↓
Movie Index
      ↓
Similarity Row
      ↓
Sort by Similarity
      ↓
Top 10 Matches
      ↓
TMDB Poster Lookup
      ↓
Movie Carousel

Why content-based recommendation?

A content-based system recommends items according to the characteristics of the selected item. This makes it useful when you want an immediate “More Like This” experience without requiring a large collection of user ratings or interaction history.

🎨 UI Highlights

The application uses custom CSS to create a cinematic streaming-service style interface:

Dark full-screen background

Netflix-inspired red accent color

Large hero heading

Custom Streamlit select box styling

Responsive movie cards

Hover scaling effect

Horizontal scrolling recommendation carousel

Poster fallback handling

🔌 TMDB Integration

The application calls the TMDB movie endpoint to obtain poster information for recommended movies.

The poster flow is:

Movie ID
   ↓
TMDB API Request
   ↓
poster_path
   ↓
TMDB Image URL
   ↓
Movie Card

If TMDB does not return a poster or the request fails, the application displays a fallback image instead.

TMDB is an external service and is not included in this project.

📦 Dependencies

The current project requires:

streamlit
pandas
requests
numpy

Install them with:

pip install -r requirements.txt

🧪 Example Usage

Launch the application.

Select a movie such as Avatar.

Click Recommend >.

The system analyzes the precomputed similarity scores.

The 10 highest-ranked similar movies are displayed.

Scroll horizontally through the recommendation cards.

📸 Screenshots

Add screenshots of the running application here when publishing the project:

screenshots/
├── home.png
└── recommendations.png

Example Markdown:

![Movie Stream Home](screenshots/home.png)
![Movie Recommendations](screenshots/recommendations.png)

🔮 Future Improvements

The project can be extended into a more complete movie discovery platform with:

🔎 Movie search instead of a fixed selector

🎭 Genre-based filtering

⭐ IMDb/TMDB ratings and release information

🎬 Trailer integration

📝 Movie descriptions and cast information

👤 User accounts and personalized watchlists

❤️ Favorites / liked movies

🤝 Collaborative filtering

🧬 Hybrid recommendation model

📊 Recommendation analytics

☁️ Cloud deployment

🔐 Secure environment-based API configuration

🧩 Possible Architecture Evolution

A future production-oriented version could separate the application into:

Frontend / Streamlit
        │
        ▼
Recommendation Service
        │
        ├── Content-Based Model
        ├── Collaborative Model
        └── Hybrid Ranking
        │
        ▼
Movie Database ───────► TMDB API

This would make the recommendation engine easier to test, scale and reuse independently from the Streamlit interface.

👨‍💻 Author

Himanshu Aggarwal

GitHub: @himanshuaggarwal04380

📄 License

This project is intended for educational and learning purposes.

Movie metadata/poster content obtained through TMDB is subject to the applicable TMDB terms and attribution requirements.

<p align="center">
  <strong>🍿 Pick a movie. Discover something similar. Enjoy the next watch.</strong>
</p>