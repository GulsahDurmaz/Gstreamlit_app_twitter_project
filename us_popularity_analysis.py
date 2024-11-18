# us_popularity_analysis.py
from imports import *

def run_us_popularity_analysis(df):

    st.subheader("US Popularity Analysis")

    ### Row A - Map
    voting_df = load_data("csv/voting.csv")
    voting_df.columns = voting_df.columns.str.strip()

    # df = load_data("csv/state_percentage_analysis.csv")
    # df['state'] = df['state'].astype(str)

    # Add a selectbox for selecting either "Tweets Popularity Map" or "Voting Result Map"
    view = st.radio("Select View", ['Tweets US Popularity Map', 'Voting Result Map'])

    st.markdown('### Map')
    # Streamlit radio button to select between 'Global' and 'USA'

    if view == "Tweets US Popularity Map":
        map_data = df.sort_values(by='state', ascending=True)
        map_data['difference'] = df['trump_count'] - df['biden_count']
        
    else:  # Global View
        map_data = voting_df.sort_values(by='state', ascending=True)
        map_data['difference'] = voting_df['trump_vote'] - voting_df['biden_vote']        
 
    # Normalize the difference for color mapping
    map_data['color'] = map_data['difference'].apply(lambda x: max(min(x, 100), -100))  # Cap between -100 and 100

    # Create a choropleth map
    fig = px.choropleth(
        map_data,
        locationmode='USA-states',
        locations='state_code',
        color='color',
        color_continuous_scale=[(1, 'red'), (0, 'blue')],
        range_color=[-100, 100],  # Adjust this range based on your data
        scope="usa",
        # title='Biden vs Trump Tweet Percentages by State',
        hover_name='state',  # Show the state code on hover
        hover_data={
            'trump_percentage': True,  # Display Trump percentage
            'biden_percentage': True,   # Display Biden percentage
            'color': False              # Do not display the difference
        }
    )
    # Update layout for better visualization with a transparent background
    fig.update_layout(
        # title_font=dict(size=16, color='white'),
        paper_bgcolor='rgba(255, 255, 255, 0)',  # Set paper background color to transparent
        geo=dict(bgcolor='rgba(255, 255, 255, 0)'),  # Set geo background color to transparent
        coloraxis_showscale=False,  # Hide the color scale (legend)
    )

    # Display the figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    conclusion = f"""
    <div style='text-align: justify;'>
    Correlation between Twitter Popularity and Election Results: -0.67. The analysis shows an
    interesting contrast between the Twitter popularity of Trump and Biden and the actual election
    results. On the Twitter popularity map, we observe that Trump was more popular in coastal states,
    while Biden’s popularity peaked in more inland areas. This aligns with the geographical distribution
    of social media activity, where coastal states tend to have higher engagement, potentially due to
    their urban populations. However, when we compare this with the actual election results, the pattern
    flips. Trump won most of the inland states, while Biden was more successful in coastal regions.
    The correlation of <strong>-0.67</strong> indicates a moderate negative relationship between Twitter popularity
    and actual election results—meaning that in some areas, higher Twitter popularity for one candidate
    didn't translate into votes for that candidate in the election.
    </div>
    """
    st.markdown(conclusion, unsafe_allow_html=True)

    # Adding space between the paragraph and the chart
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    img = Image.open('png/state_percentage_analysis.png')
    st.image(img, caption="State Percentage Analysis - Trump vs Biden", use_column_width=True)

    conclusion = f"""
    <div style='text-align: justify;'>
    The analysis reveals a moderate negative correlation between Trump and Biden's Twitter popularity and
    the actual 2020 election outcomes. In states like Texas and Florida, Trump had higher tweet percentages,
    but the election results were closer than expected. Conversely, in swing states like Pennsylvania,
    Michigan, and Georgia, despite Trump’s tweet dominance, Biden secured electoral wins. This suggests
    that social media popularity did not consistently translate into votes, highlighting a disparity between
    online activity and actual voter behavior.
    </div>
    """
    st.markdown(conclusion, unsafe_allow_html=True)
    
    # Adding space between the paragraph and the chart
    st.markdown("<br><br>", unsafe_allow_html=True)

    unique_states = sorted(list(set(df['state'].unique())))
    selected_state = st.selectbox('Select state', unique_states)

    # Calculate percentage for selected state
    trump_percentage = df.loc[df['state'] == selected_state, 'trump_percentage'].values[0]
    biden_percentage = df.loc[df['state'] == selected_state, 'biden_percentage'].values[0]
    # Calculate US percentage
    # trump_percentage_US = df.loc[df['state'] == 'US', 'trump_percentage'].values[0]
    # biden_percentage_US = df.loc[df['state'] == 'US', 'biden_percentage'].values[0]

    # Calculate state_tweet_count / US_tweet_count
    state_US_percentage = df.loc[df['state'] == selected_state, 'total_percentage'].values[0]

    ### Row A
    st.markdown(f'### {selected_state}')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Trump", f'{trump_percentage}%')

    with col2:
        st.metric("Biden", f'{biden_percentage}%')

    with col3:
        st.metric("state/World", f'{state_US_percentage}%')
   


    ### Row C
    most_us_df = load_data("csv/most_us_df.csv")
    # Add a selectbox for selecting either "Trump" or "Biden"
    selected_candidate = st.selectbox('Select Candidate', ['Trump', 'Biden'])

    # Dynamically filter the DataFrame based on the selected candidate
    if selected_candidate == 'Trump':
        filtered_df = most_us_df[most_us_df['candidate'] == 'Trump']
    else:
        filtered_df = most_us_df[most_us_df['candidate'] == 'Biden']

    # Display the Top 5 Most Liked Tweets
    st.markdown('### Top 5 Most Liked Tweets')
    # Top 10 most liked tweets for the selected state
    top_liked_tweets = filtered_df[filtered_df['state'] == selected_state].nlargest(5, 'likes')
    # Display the dataframe without index and extend it to fill the page
    st.dataframe(
        top_liked_tweets[['tweet', 'likes']],  # Display only the 'tweet' and 'likes' columns
        hide_index=True,  # Hide the index numbers
        use_container_width=True  # Extend the table to fill the page width
    )

    # Display the Top 5 Most Retweeted Tweets
    st.markdown('### Top 5 Most Retweeted Tweets')
    # Select top 5 most retweeted tweets for the selected state
    top_retweeted_tweets = filtered_df[filtered_df['state'] == selected_state].nlargest(5, 'retweet_count')

    # Display the dataframe
    st.dataframe(
        top_retweeted_tweets[['tweet', 'retweet_count']],  # Display 'tweet' and 'retweet_count' columns
        hide_index=True,  # Hide index numbers
        use_container_width=True  # Extend the table to fill the page width
    )
