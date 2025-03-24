# IMDB2024Project
IMDB 2024 Data Scraping and Visualizations
Project overview
This project focuses on extracting and analyzing movie data from IMDb for the year 2024. The task involves scraping data such as movie names, genres, ratings, voting counts, and durations from IMDb's 2024 movie list using Selenium. The data will then be organized genre-wise, saved as individual CSV files, and combined into a single dataset stored in an SQL database. Finally, the project will provide interactive visualizations and filtering functionality using Streamlit to answer key questions and allow users to customize their exploration of the dataset..

Features ✨
Interactive filtering by genre, duration, ratings, and voting counts

Top 10 Movies by rating and popularity

10+ visualizations including bar charts, scatter plots, and heatmaps

Dynamic recommendations based on user filters

Data export capability for filtered results

Dataset Structure 

The dataset contain these columns:

title: Movie name

genre: Primary genre

rating: IMDb rating (0-10)

votes: Number of votes

duration: Runtime in hours

Usage Guide 

Apply Filters using the sidebar controls

View filtered results in the main table

Explore visualizations below the data

Download filtered data using the sidebar button

Get recommendations by selecting specific genres

Project Structure
Copy
imdb-analysis/
├── IMDBvisual.py            # Main Streamlit application
├── movies.csv        # Dataset file
├── imdbproject.ipynb  # Data scraping code
└── README.md         # This file
Contributing
Contributions are welcome! Please open an issue or submit a pull request.
