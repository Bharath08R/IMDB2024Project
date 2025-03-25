# IMDB2024Project
IMDB 2024 Data Scraping and Visualizations

streamlit app link
https://v7aq2pbhm5rxpnkw64rpke.streamlit.app/

# Comprehensive Movie Data Analysis and Visualization Using Streamlit

## Introduction
In this article, we will explore a Python code snippet that utilizes Streamlit, a powerful library for creating web applications, to analyze and visualize movie data. The code allows users to filter movies based on various criteria such as genre, duration, ratings, and voting counts, while also providing insightful visualizations to enhance data understanding.

## Key Concepts
The code leverages several key concepts:
- **Streamlit**: A framework for building interactive web applications in Python.
- **Pandas**: A data manipulation library that allows for easy data handling and analysis.
- **Plotly Express**: A library for creating interactive visualizations.
- **Data Filtering**: The ability to refine datasets based on user-defined criteria.
- **Caching**: Streamlit's caching mechanism to optimize data loading.

## Code Structure
The code is structured into several sections:
1. **Setup**: Importing necessary libraries and configuring the Streamlit page.
2. **Data Loading**: Loading the movie dataset using Pandas.
3. **User Interface**: Creating a sidebar for user input filters.
4. **Data Filtering**: Applying filters based on user selections.
5. **Data Display**: Showing filtered results and providing options to download the data.
6. **Visualizations**: Generating various plots to visualize the data.


## Features ✨
Interactive filtering by genre, duration, ratings, and voting counts
Top 10 Movies by rating and popularity
10+ visualizations including bar charts, scatter plots, and heatmaps
Data export capability for filtered results
Dataset Structure 

## The dataset contain these columns:
* title: Movie name
* genre: Primary genre
* rating: IMDb rating (0-10)
* votes: Number of votes
* duration: Runtime in minutes

## Usage Guide 
Apply Filters using the sidebar controls
View filtered results in the main table
Explore visualizations below the data
Download filtered data using the sidebar button

## Project Structure
- IMDBvisual.py            # Main Streamlit application
- movies.csv        # Dataset file
- imdbproject.ipynb  # Data scraping code
- README.md         # This file

## Contributions are welcome! Please open an issue or submit a pull request.
