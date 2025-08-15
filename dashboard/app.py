import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Career Trends Dashboard", layout="wide")
st.title("📊 Career Trends Dashboard")

# Paths
RAW_PATH = "data/raw/jobs.csv"
CLEANED_PATH = "data/cleaned/jobs_cleaned.csv"

# Load data
df = None
if os.path.exists(CLEANED_PATH):
    st.write("✅ Loading cleaned data...")
    df = pd.read_csv(CLEANED_PATH)
elif os.path.exists(RAW_PATH):
    st.write("⚠️ Cleaned data not found. Loading raw data instead...")
    df = pd.read_csv(RAW_PATH)
else:
    st.error("❌ No CSV file found. Please check your data folder.")

# If data is loaded
if df is not None and not df.empty:
    st.write(f"**Total Records:** {len(df)}")

    # Show first few rows
    st.subheader("Preview of Data")
    st.dataframe(df.head())

    # Show basic stats if salary column exists
    if "salary" in df.columns:
        st.subheader("Salary Statistics")
        st.write(df["salary"].describe())

    # If datePosted exists, convert to datetime
    date_col_candidates = ["datePosted", "posted_date", "date_posted", "Posted Date"]
    date_col = None
    for col in date_col_candidates:
        if col in df.columns:
            date_col = col
            df[col] = pd.to_datetime(df[col], errors="coerce")
            break

    if date_col:
        st.subheader("Jobs Over Time")
        jobs_over_time = df.groupby(df[date_col].dt.date).size().reset_index(name="count")
        st.line_chart(jobs_over_time.set_index(date_col)["count"])
    else:
        st.warning("⚠️ No valid date column found. Skipping time trend chart.")
else:
    st.warning("No data to display.")
