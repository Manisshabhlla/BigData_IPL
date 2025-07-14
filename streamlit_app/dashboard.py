import streamlit as st
from google.cloud import bigquery

client = bigquery.Client()

st.set_page_config(layout="wide")
st.title("🏏 IPL Match Performance Analyzer")

# Sidebar
season = st.sidebar.selectbox("Select Season", list(range(2008, 2024)))
view = st.sidebar.radio("View", ["Top Batsmen", "Top Bowlers", "Team Wins", "Home vs Away"])

# Queries
if view == "Top Batsmen":
    q = f"""
    SELECT batsman, SUM(batsman_runs) AS runs
    FROM `your-project.ipl_dataset.ipl_deliveries`
    JOIN `your-project.ipl_dataset.ipl_matches` USING (match_id)
    WHERE season = {season}
    GROUP BY batsman ORDER BY runs DESC LIMIT 10
    """
    df = client.query(q).to_dataframe()
    st.subheader(f"Top Batsmen - {season}")
    st.bar_chart(df.set_index("batsman"))

elif view == "Top Bowlers":
    q = f"""
    SELECT bowler, COUNT(*) AS wickets
    FROM `your-project.ipl_dataset.ipl_deliveries`
    JOIN `your-project.ipl_dataset.ipl_matches` USING (match_id)
    WHERE dismissal_kind NOT IN ('run out', 'retired hurt') AND season = {season}
    GROUP BY bowler ORDER BY wickets DESC LIMIT 10
    """
    df = client.query(q).to_dataframe()
    st.subheader(f"Top Bowlers - {season}")
    st.bar_chart(df.set_index("bowler"))

elif view == "Team Wins":
    q = f"""
    SELECT winner, COUNT(*) as wins
    FROM `your-project.ipl_dataset.ipl_matches`
    WHERE season = {season}
    GROUP BY winner ORDER BY wins DESC
    """
    df = client.query(q).to_dataframe()
    st.subheader(f"Team Wins - {season}")
    st.bar_chart(df.set_index("winner"))

elif view == "Home vs Away":
    q = f"""
    SELECT h.team, h.home_or_away, COUNT(*) AS matches,
           SUM(CASE WHEN m.winner = h.team THEN 1 ELSE 0 END) AS wins
    FROM `your-project.ipl_dataset.ipl_matches` m
    JOIN `your-project.ipl_dataset.ipl_home_away` h
    ON m.team1 = h.team AND m.venue = h.venue
    WHERE m.season = {season}
    GROUP BY h.team, h.home_or_away
    ORDER BY team, home_or_away
    """
    df = client.query(q).to_dataframe()
    st.subheader(f"Home vs Away Performance - {season}")
    st.dataframe(df)
