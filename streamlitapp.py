# streamlitapp.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from analysis import load_metadata, canonicalize_dates, clean_core, pubs_per_year, top_journals, top_words_in_column

# CONFIGURATION
DATA_PATH = r"C:\Users\ROBERT\Desktop\final-final-project-python\cord19_data\cleaned_metadata.csv"  

st.set_page_config(
    page_title="CORD-19 Explorer",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# HEADER
st.title("CORD-19 Data Explorer")
st.markdown(
    """
    Explore COVID-19 research publications from the **CORD-19 dataset**.  
    Use filters in the sidebar to explore trends by year, journal, or keyword.  
    ---
    """
)

# LOAD DATA
@st.cache_data
def load_data(path):
    return pd.read_csv(path, low_memory=False)

df = load_data(DATA_PATH)

# SIDEBAR FILTERS
st.sidebar.header("Filters")

years = sorted(df['year'].dropna().unique())
if years:
    start, end = st.sidebar.select_slider(
        "Select year range",
        options=years,
        value=(min(years), max(years))
    )
else:
    start, end = (None, None)

journal_filter = st.sidebar.multiselect(
    "Journal (top 50)",
    options=df['journal'].dropna().unique()[:50],
    default=[]
)

# APPLY FILTERS
filtered = df.copy()
if start and end:
    filtered = filtered[(filtered['year'] >= start) & (filtered['year'] <= end)]
if journal_filter:
    filtered = filtered[filtered['journal'].isin(journal_filter)]

st.subheader(f"Showing {len(filtered):,} records")

# CARDS
col1, col2, col3 = st.columns(3)

col1.metric("Total Publications", f"{len(df):,}")
col2.metric("Unique Journals", df['journal'].nunique())
col3.metric("Avg. Abstract Length", round(df['abstract_word_count'].mean(), 1))

# CHART 1: Publications per year
st.subheader(" Publications per Year")
pubs = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
pubs.plot(kind='bar', ax=ax, color="skyblue")
ax.set_title("Publications per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# CHART 2: Top Journals
st.subheader("Top Journals")
top_journals_data = filtered['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
top_journals_data.plot(kind='barh', ax=ax2, color="lightgreen")
ax2.set_title("Top 10 Journals by Publications")
ax2.set_xlabel("Count")
ax2.set_ylabel("Journal")
st.pyplot(fig2)

# DATA TABLE
st.subheader("Sample Records")
st.dataframe(filtered[['title', 'publish_time', 'journal']].head(50))
st.markdown(f"**Showing {len(filtered):,} records out of {len(df):,} total.**")