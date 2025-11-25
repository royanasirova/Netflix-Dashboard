import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('netflix1.csv')
st.set_page_config(page_title='Netflix Dashboard', layout='wide')
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Descriptives','Genres','Country'])
if page == 'Descriptives':
    st.title('Netflix Dataset Overview')
    st.write('General statistics and distribution of Netflix content')
    st.dataframe(df.describe(include ='all'))
    st.subheader('Content Type Distribution')
    fig1 = px.histogram(df, x='type', color='type', title='Content Types')
    st.plotly_chart(fig1)
    st.subheader('Release Year Distribution')
    fig2 = px.histogram(df, x='release year', nbins=30, title='Release Years')
    st.plotly_chart(fig2)

elif page == 'Genres':
    st.title('Genre Analysis')
    st.subheader('Top Genres by Count')
    df['listed in']=df['listed in'].astype(str)
    genres = df['listed in'].str.split(', ').explode()
    top_genres = genres.value_counts().reset_index()
    top_genres.columns = ['Genre', 'Count']
    fig3 = px.bar(top_genres.head(15), x='Genre', y='Count', title='Top 15 Genres')
    st.plotly_chart(fig3)

elif page=='Country':
    st.title('Country-wise Content')
    df['country'] = df['country'].astype(str)
    country_counts = df['country'].str.split(', ').explode().value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']
    fig4 = px.bar(country_counts.head(15), x='Country', y='Count', title='Top 15 Countries by Content Count')
    st.plotly_chart(fig4)

