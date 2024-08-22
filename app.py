import streamlit as st  # Streamlit for web app
import plotly.express as px  # Plotly Express for data visualization
import pandas as pd  # Pandas for data manipulation

gapminder = px.data.gapminder()  # Load the dataset

st.title("Gapminder Data Visualization App")  # Set the app title


st.write("Top 10 Countries by Population:")  # Section title
st.dataframe(gapminder.head(10))  # Display top 10 countries

st.write("Summary Statistics:")  # Section title
st.write(gapminder.describe())  # Display summary statistics

year = st.selectbox("Select a Year:", gapminder["year"].unique())  
# Create drop-down menu

filtered_data =gapminder[gapminder["year"] == year]  # Filter data by selected year

fig = px.scatter(filtered_data,  # Create scatter plot
                 x="gdpPercap",  # X-axis: GDP per capita
                 y="lifeExp",  # Y-axis: Life expectancy
                 color="continent",  # Color: Continent
                 hover_data=["country"])  # Hover data: Country


st.plotly_chart(fig)  # Display the plot
