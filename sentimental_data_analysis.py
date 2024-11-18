# sentimental_data_analysis.py
from imports import *

# Function to handle tweet analysis and display results
def run_sentimental_analysis(df):
    st.subheader("US Sentiment Analysis")

    # Sentiment analysis for Trump and Biden
    trump_pos_percentage = df.iloc[0]['Trump']
    trump_neu_percentage = df.iloc[1]['Trump']
    trump_neg_percentage = df.iloc[2]['Trump']  

    biden_pos_percentage = df.iloc[0]['Biden']
    biden_neu_percentage = df.iloc[1]['Biden']
    biden_neg_percentage = df.iloc[2]['Biden']

    # Display sentiment metrics for Trump and Biden
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Trump - Positive", f'{trump_pos_percentage:.2f}%')
    with col2:
        st.metric("Trump - Neutral", f'{trump_neu_percentage:.2f}%')
    with col3:
        st.metric("Trump - Negative", f'{trump_neg_percentage:.2f}%')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Biden - Positive", f'{biden_pos_percentage:.2f}%')
    with col2:
        st.metric("Biden - Neutral", f'{biden_neu_percentage:.2f}%')
    with col3:
        st.metric("Biden - Negative", f'{biden_neg_percentage:.2f}%')

    img = Image.open('png/sentiment_comparison.png')
    st.image(img, caption="Average Daily Sentiment Scores - Trump vs Biden", use_column_width=True)

    conclusion = f"""
    <div style='text-align: justify;'>
    This graph shows the change in tweet sentiment for Trump and Biden over time. Biden's sentiment curve
    shows a strong increase, especially as it approaches November, which can likely be explained by the
    positive media coverage during the election period. Trump's sentiment, on the other hand, remains
    generally lower but experiences a spike in October. This period coincides with Trump’s diagnosis with
    Covid-19 and the intensification of his campaign. However, towards the end, while Biden's sentiment peaks
    again, Trump's sentiment declines. This reflects the fluctuations in public support as election day
    approaches.
    </div>
    """
    st.markdown(conclusion, unsafe_allow_html=True)

    # Adding space between the paragraph and the chart
    st.markdown("<br><br>", unsafe_allow_html=True)

    img = Image.open('png/sentiment_and_vote_comparison.png')
    st.image(img, caption="Average Daily Sentiment Scores - Trump vs Biden", use_column_width=True)

    conclusion = f"""
    <div style='text-align: justify;'>
    This graph compares tweet sentiment for Trump and Biden with the 2020 election results by state. While
    both candidates generally have positive sentiment scores, they don’t always align with the vote outcomes.
    In states like Florida, Arizona, and Georgia, Trump had more favorable sentiment, but Biden won the vote.
    In swing states like Pennsylvania and Michigan, sentiment and votes were more closely matched. The data
    shows that while social media sentiment offers some insights, it doesn’t consistently reflect actual voter
    behavior.
    </div>
    """
    st.markdown(conclusion, unsafe_allow_html=True)

    # Adding space between the paragraph and the chart
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Most liked and retweeted tweets sentiment (optional part, display data from csv)
    most_us_df = load_data("csv/most_us_df.csv")
    most_us_df = most_us_df.drop_duplicates(subset='tweet')
    st.markdown('### Top 3 Most Liked Tweet Sentiment')
    top_liked_tweets = most_us_df.nlargest(3, 'likes')
    st.dataframe(top_liked_tweets[['tweet', 'likes', 'sentiment']], hide_index=True, use_container_width=True)
    
    st.markdown('### Top 3 Most Retweeted Tweet Sentiment')
    top_retweeted_tweets = most_us_df.nlargest(3, 'retweet_count')
    st.dataframe(top_retweeted_tweets[['tweet', 'retweet_count', 'sentiment']], hide_index=True, use_container_width=True)

    # Collect user tweets for sentiment analysis
    if 'tweets_data' not in st.session_state:
        st.session_state.tweets_data = []  # Initialize the list to store tweets and sentiment scores

    # Input for user to enter tweets
    tweet_input = st.text_area("Enter a tweet for sentiment analysis:")

    # Button to trigger sentiment analysis
    if st.button("Analyze Sentiment"):
        if tweet_input:
            # Analyze sentiment
            sentiment, score = analyze_sentiment(tweet_input)

            # Display sentiment result
            st.write(f"Sentiment: {sentiment}")
            st.write(f"Sentiment Score: {score:.2f}")

            # Save the tweet, sentiment, and score to the session state list
            st.session_state.tweets_data.append({
                'tweet': tweet_input,
                'sentiment': sentiment,
                'score': score
            })
            # Clear the input field after processing
            st.session_state.tweet_input = ""  # Optional: reset the input field

    # Display the DataFrame of user-entered tweets and their sentiment
    if st.session_state.tweets_data:
        # Create a DataFrame to store the tweet data
        df_tweets = pd.DataFrame(st.session_state.tweets_data)
        
        # Show the DataFrame in Streamlit
        st.markdown("### User-Submitted Tweets and Sentiment")
        st.dataframe(df_tweets, hide_index=True, use_container_width=True)
