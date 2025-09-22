# analysis.py
"""
Reusable helpers for CORD-19 metadata analysis.
"""

import pandas as pd
from collections import Counter
import re

def load_metadata(path, nrows=None):
    """Load CORD-19 metadata CSV safely."""
    return pd.read_csv(path, nrows=nrows, low_memory=False, on_bad_lines='skip')

def detect_columns(df):
    """Return a dict of candidate columns for title/date/journal/abstract/authors."""
    candidates = {}
    candidates['date_candidates'] = [c for c in df.columns if 'publish' in c.lower() or 'date' in c.lower()]
    candidates['title_candidates'] = [c for c in df.columns if 'title' in c.lower() or 'name' in c.lower()]
    candidates['journal_candidates'] = [c for c in df.columns if 'journal' in c.lower()]
    candidates['abstract_candidates'] = [c for c in df.columns if 'abstract' in c.lower() or 'summary' in c.lower() or 'description' in c.lower()]
    candidates['authors_candidates'] = [c for c in df.columns if 'author' in c.lower() or 'creator' in c.lower()]
    return candidates

def canonicalize_dates(df, date_col=None):
    """Create 'publish_time' and 'year' columns from selected date_col (auto-detect if None)."""
    if date_col is None:
        for c in df.columns:
            if 'publish' in c.lower() or 'date' in c.lower():
                date_col = c
                break
    if date_col is None:
        raise ValueError("No suitable date column found.")
    df['publish_time'] = pd.to_datetime(df[date_col], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

def clean_core(df, title_col, abstract_col=None, drop_missing=True):
    """Drop rows missing title/publish_time and add abstract_word_count and normalized title."""
    if drop_missing:
        df = df.dropna(subset=[title_col, 'publish_time']).copy()
    df['title'] = df[title_col].astype(str)
    if abstract_col and abstract_col in df.columns:
        df['abstract'] = df[abstract_col].fillna("").astype(str)
    else:
        df['abstract'] = ""
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))
    return df

def pubs_per_year(df):
    return df['year'].value_counts().sort_index()

def top_journals(df, journal_col, n=10):
    return df[journal_col].dropna().value_counts().head(n)

def top_words_in_column(df, col, min_len=3, top_n=25):
    text = " ".join(df[col].dropna().astype(str)).lower()
    words = re.findall(r'\b[a-z]{%d,}\b' % min_len, text)
    return Counter(words).most_common(top_n)
