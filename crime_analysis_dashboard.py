import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
data = pd.read_csv('State-wise Sexual Assault (Detailed) 1999-2013.csv')

# Sidebar filters
st.sidebar.header("Filter Data")
year = st.sidebar.multiselect("Select Year", sorted(data['Year'].unique()))
state = st.sidebar.multiselect("Select State/UT", sorted(data['State/UT'].unique()))
relationship = st.sidebar.multiselect("Select Offender Relationship", 
                                      sorted(data.columns[3:]))  # Assuming offender relationships start from the 4th column

# Filter data based on sidebar selections
filtered_data = data.copy()
if year:
    filtered_data = filtered_data[filtered_data['Year'].isin(year)]
if state:
    filtered_data = filtered_data[filtered_data['State/UT'].isin(state)]
if relationship:
    filtered_data = filtered_data[['State/UT', 'Year'] + relationship]

# Display filtered data
st.write("Filtered Data", filtered_data)

# Visualizations
st.header("Yearly Trend of Sexual Assault Cases")
fig1 = px.line(filtered_data, x="Year", y="Number of Cases by Offender Relationship", color="State/UT")
st.plotly_chart(fig1)

st.header("State-wise Distribution of Cases")
fig2 = px.bar(filtered_data, x="State/UT", y="Number of Cases by Offender Relationship", color="Year")
st.plotly_chart(fig2)

