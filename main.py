# streamlit.py
from imports import *
import eda
# import world_popularity_analysis
import us_popularity_analysis
import sentimental_data_analysis
import dataset

# Configure the Streamlit page
st.set_page_config(page_title="2020 US Presidential Election Dashboard",
                   page_icon=":bar_chart:",
                   initial_sidebar_state="expanded")

# Apply custom styles
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header('US Presidential Election Dashboard `2020`')

# country_percentage_analysis_df = load_data("country_percentage_analysis.csv")
state_percentage_analysis_df = load_data("csv/state_percentage_analysis.csv")
state_percentage_analysis_df['state'] = state_percentage_analysis_df['state'].astype(str)

# sentiment analysis csv files
sentiment_general_df = load_data("csv/sentiment_general.csv")

# Initialize page state
if 'page' not in st.session_state:
    st.session_state.page = 'Exploratory Data Analysis'  # Default page

# Sidebar buttons for page navigation
if st.sidebar.button("Exploratory Data Analysis"):
    st.session_state.page = 'Exploratory Data Analysis'

# if st.sidebar.button("World Popularity Analysis"):
#     st.session_state.page = 'World Popularity Analysis'

if st.sidebar.button("US Popularity Analysis"):
    st.session_state.page = 'US Popularity Analysis'

if st.sidebar.button("Sentimental Data Analysis"):
    st.session_state.page = 'Sentimental Data Analysis'

if st.sidebar.button("Dataset"):
    st.session_state.page = 'Dataset'

# Display content based on the active page
if st.session_state.page == 'Exploratory Data Analysis':
    eda.run_exploratory_data_analysis()  # Call the function from eda.py

# elif st.session_state.page == 'World Popularity Analysis':
#     world_popularity_analysis.run_world_popularity_analysis(country_percentage_analysis_df)  # Call the function from world_popularity_analysis.py

elif st.session_state.page == 'US Popularity Analysis':
    us_popularity_analysis.run_us_popularity_analysis(state_percentage_analysis_df)  # Call the function from us_popularity_analysis.py

elif st.session_state.page == 'Sentimental Data Analysis':
    sentimental_data_analysis.run_sentimental_analysis(sentiment_general_df)  # Call the function from sentimental_data_analysis.py
    
elif st.session_state.page == 'Dataset':
    dataset.run_dataset()

# Sidebar footer
st.sidebar.markdown('''
---
Created with ❤️ by [Gulsah Durmaz](https://github.com/GulsahDurmaz).
''')