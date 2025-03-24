import streamlit as st
import pandas as pd
import plotly.express as px


# Set page title and layout
st.set_page_config(page_title="Movie Data Analysis", layout="wide")
st.title("Movie Data Analysis and Visualization")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("imdb_2024.csv")  # Replace with your dataset path

df = load_data()

# Sidebar for filters
st.sidebar.header("Filters")

# Genre filter
genre_filter = st.sidebar.multiselect("Select Genres", df["Genre"].unique())

# Duration filter
st.sidebar.write("### Duration (Hrs)")
duration_options = ["< 2 hrs", "2–3 hrs", "> 3 hrs", "all"]
duration_filter = st.sidebar.selectbox("Select Duration Range", duration_options)

# Rating filter
st.sidebar.write("### Ratings")
rating_filter = st.sidebar.slider("Select Minimum Rating", min_value=0.0, max_value=10.0, value=8.0)

# Voting counts filter
st.sidebar.write("### Voting Counts")
votes_filter = st.sidebar.number_input("Select Minimum Voting Counts", min_value=0, value=10000)

# Apply filters
filtered_df = df.copy()

# Genre filter
if genre_filter:
    filtered_df = filtered_df[filtered_df["Genre"].isin(genre_filter)]

# Duration filter
if duration_filter == "< 2 hrs":
    filtered_df = filtered_df[filtered_df["Duration"] < 120]
elif duration_filter == "2–3 hrs":
    filtered_df = filtered_df[(filtered_df["Duration"] >= 120) & (filtered_df["Duration"] <= 180)]
elif duration_filter == "> 3 hrs":
    filtered_df = filtered_df[filtered_df["Duration"] > 180]
elif duration_filter == "all":
    filtered_df = filtered_df

# Rating filter
filtered_df = filtered_df[filtered_df["Rating"] >= rating_filter]

# Voting counts filter
filtered_df = filtered_df[filtered_df["Votes"] >= votes_filter]

# Display filtered data
st.write("### Filtered Results")
st.dataframe(filtered_df)

# Download filtered data
st.sidebar.markdown("### Download Filtered Data")
st.sidebar.download_button(
    label="Download as CSV",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_movies.csv",
    mime="text/csv",
)

# Top 10 Movies by Rating and Voting Counts
st.write("### Top 10 Movies by Rating")
top_10_movies = filtered_df.nlargest(10, ["Rating"])
st.dataframe(top_10_movies[["Title", "Genre", "Rating", "Votes", "Duration"]])

st.write("### Top 10 Movies by Voting Counts")
top_10_movies = filtered_df.nlargest(10, ["Votes"])
st.dataframe(top_10_movies[["Title", "Genre", "Rating", "Votes", "Duration"]])

# Visualizations
st.write("## Visualizations")

# 1. Genre Distribution
st.write("### Genre Distribution")
genre_counts = filtered_df["Genre"].value_counts()
fig1 = px.bar(genre_counts, x=genre_counts.index, y=genre_counts.values, labels={"x": "Genre", "y": "Count"})
st.plotly_chart(fig1)

# 2. Average Duration by Genre
st.write("### Average Duration by Genre")
avg_duration = filtered_df.groupby("Genre")["Duration"].mean().reset_index()
fig2 = px.bar(avg_duration, x="Duration", y="Genre", orientation="h", labels={"Duration": "Average Duration", "Genre": "Genre"})
st.plotly_chart(fig2)

# 3. Voting Trends by Genre
st.write("### Voting Trends by Genre")
avg_votes = filtered_df.groupby("Genre")["Votes"].mean().reset_index()
fig3 = px.bar(avg_votes, x="Genre", y="Votes", labels={"Genre": "Genre", "Votes": "Average Votes"})
st.plotly_chart(fig3)

# 4. Rating Distribution
st.write("### Rating Distribution")
fig4 = px.histogram(filtered_df, x="Rating", nbins=20, labels={"Rating": "Rating"})
st.plotly_chart(fig4)

# 5. Genre-Based Rating Leaders
st.write("### Genre-Based Rating Leaders")
top_rated_movies = filtered_df.loc[filtered_df.groupby("Genre")["Rating"].idxmax()]
st.dataframe(top_rated_movies[["Title", "Genre", "Rating"]])

# 6. Most Popular Genres by Voting
st.write("### Most Popular Genres by Voting")
total_votes_by_genre = filtered_df.groupby("Genre")["Votes"].sum().reset_index()
fig5 = px.pie(total_votes_by_genre, values="Votes", names="Genre", title="Most Popular Genres by Voting")
st.plotly_chart(fig5)

# 7. Duration Extremes
st.write("### Duration Extremes")
shortest_movie = filtered_df.loc[filtered_df["Duration"].idxmin()]
longest_movie = filtered_df.loc[filtered_df["Duration"].idxmax()]
st.write("**Shortest Movie:**", shortest_movie["Title"], "| Duration:", shortest_movie["Duration"])
st.write("**Longest Movie:**", longest_movie["Title"], "| Duration:", longest_movie["Duration"])

# 8. Ratings by Genre (Heatmap)
st.write("### Ratings by Genre (Heatmap)")
heatmap_data = filtered_df.pivot_table(index="Genre", values="Rating", aggfunc="mean")
fig6 = px.imshow(heatmap_data, labels=dict(x="Genre", y="Rating", color="Average Rating"))
st.plotly_chart(fig6)

# # 9. Correlation Analysis: Ratings vs. Voting Counts
st.write("### Correlation Analysis: Ratings vs. Voting Counts")
fig7 = px.scatter(filtered_df, x="Rating", y="Votes", hover_data=["Title", "Genre"], trendline="ols", labels={"Rating": "Rating", "Votes": "Voting Counts"})
st.plotly_chart(fig7)

