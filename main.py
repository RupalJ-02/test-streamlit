# main.py
import streamlit as st
import pandas as pd
from preprocessor import load_data, filter_data

# Load the data
data_file = 'State wise Sexual Assault (Detailed) 1999 - 2013.csv'
data = load_data(data_file)

# Streamlit App Layout
st.title("State-wise Sexual Assault Analysis (1999 - 2013)")
st.write("This dashboard provides a detailed state-wise account of sexual assault cases from 1999 to 2013, focusing on victim-offender relationships.")

# Sidebar Filters
st.sidebar.header("Filter Data")
year = st.sidebar.selectbox("Select YEAR", sorted(data['YEAR'].unique()), index=0)
state = st.sidebar.selectbox("Select State/UT", sorted(data['State/UT'].unique()), index=0)

# Filter the data
filtered_data = filter_data(data, year=year, state=state)

# Display filtered data
st.subheader(f"Data for {state} in {year}")
st.dataframe(filtered_data)

# Summary statistics
st.write("### Summary Statistics")
summary = filtered_data.describe()
st.write(summary)

# Visualization
st.write("### Number of Cases by Offender Relationship")
relationship_columns = [col for col in filtered_data.columns if col not in ['State/UT', 'YEAR']]
relationship_counts = filtered_data[relationship_columns].sum()

# Plot the data
st.bar_chart(relationship_counts)

