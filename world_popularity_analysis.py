# world_popularity_analysis.py
from imports import *
import choropleth_map

def run_world_popularity_analysis(df):

    st.subheader("World Popularity Analysis")

    # Sort top 10 countries
    df = df.sort_values(by='total_tweet_count', ascending=False)
    # The top 10 countries based on total tweet counts
    top_countries = df.iloc[1:].head(10)
    # Set the position of bars on the x-axis
    bar_width = 0.25
    x = range(len(top_countries))
    # Create a figure for the bar chart
    plt.figure(figsize=(12, 6))
    # Plot Trump tweets
    plt.bar(x, top_countries['trump_count'], width=bar_width, label='Trump Tweets', color='red', align='center')
    # Plot Biden tweets
    plt.bar([p + bar_width for p in x], top_countries['biden_count'], width=bar_width, label='Biden Tweets', color='blue', align='center')
    # Plot Total tweets
    plt.bar([p + bar_width*2 for p in x], top_countries['total_tweet_count'], width=bar_width, label='Total Tweets', color='gray', align='center')
    # Adding labels and title
    plt.xlabel('Country', fontsize=14, color='white')
    plt.ylabel('Tweet Count', fontsize=14, color='white')
    # plt.title('Top 10 Countries Tweet Counts: Trump vs Biden vs Total', fontsize=16, color='white', weight='bold')
    plt.xticks([p + bar_width for p in x], top_countries['country'], rotation=90, color='white')
    plt.legend(facecolor='white', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)  # Add gridlines
    # Change tick values to white
    plt.tick_params(axis='x', colors='white')  # X-axis ticks
    plt.tick_params(axis='y', colors='white')  # Y-axis ticks
    # Streamlit display
    st.pyplot(plt, transparent=True)
    # Clear the figure after displaying
    plt.clf()

    unique_countries = sorted(list(set(df['country'].unique())))
    selected_country = st.selectbox('Select country', unique_countries)

    # Calculate percentage for selected country
    trump_percentage = df.loc[df['country'] == selected_country, 'trump_percentage'].values[0]
    biden_percentage = df.loc[df['country'] == selected_country, 'biden_percentage'].values[0]

    # Calculate country_tweet_count / global_tweet_count
    country_global_percentage = df.loc[df['country'] == selected_country, 'total_percentage'].values[0]

    ### Row A
    st.markdown(f'### {selected_country}')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Trump", f'{trump_percentage}%')

    with col2:
        st.metric("Biden", f'{biden_percentage}%')

    with col3:
        st.metric("Country/World", f'{country_global_percentage}%')


    ### Row B
    st.markdown('### Map')
    draw_choropleth(df)

    ### Row C
    most_df = load_data("most_df.csv")
    # Add a selectbox for selecting either "Trump" or "Biden"
    selected_candidate = st.selectbox('Select Candidate', ['Trump', 'Biden'])

    # Dynamically filter the DataFrame based on the selected candidate
    if selected_candidate == 'Trump':
        filtered_df = most_df[most_df['candidate'] == 'Trump']
    else:
        filtered_df = most_df[most_df['candidate'] == 'Biden']

    # Display the Top 5 Most Liked Tweets
    st.markdown('### Top 5 Most Liked Tweets')
    # Top 10 most liked tweets for the selected country
    top_liked_tweets = filtered_df[filtered_df['country'] == selected_country].nlargest(5, 'likes')
    # Display the dataframe without index and extend it to fill the page
    st.dataframe(
        top_liked_tweets[['tweet', 'likes']],  # Display only the 'tweet' and 'likes' columns
        hide_index=True,  # Hide the index numbers
        use_container_width=True  # Extend the table to fill the page width
    )

    # Display the Top 5 Most Retweeted Tweets
    st.markdown('### Top 5 Most Retweeted Tweets')
    # Select top 5 most retweeted tweets for the selected country
    top_retweeted_tweets = filtered_df[filtered_df['country'] == selected_country].nlargest(5, 'retweet_count')

    # Display the dataframe
    st.dataframe(
        top_retweeted_tweets[['tweet', 'retweet_count']],  # Display 'tweet' and 'retweet_count' columns
        hide_index=True,  # Hide index numbers
        use_container_width=True  # Extend the table to fill the page width
    )
