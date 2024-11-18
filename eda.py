# eda.py
from imports import *

def run_exploratory_data_analysis():
    st.markdown("## Exploratory Data Analysis")
    st.markdown("""
    The 2020 United States presidential election was held on **November 3, 2020**. The major candidates were incumbent 
    Republican President Donald Trump and Democratic former Vice President Joe Biden. In the months leading up to the 
    election, social media played a significant role in shaping public opinion, with platforms like Twitter serving as a 
    key battleground for discussions, endorsements, and criticism.
    """)

    st.markdown("**Why Twitter?**")
    st.markdown("""
    Social media platforms like Facebook and Twitter have transformed how we interact and share news. As of June 2019,
    Twitter had over 348M users posting 500M tweets daily, enabling users to influence trends and shape news coverage.
    Twitter has become increasingly important in electoral campaigning, with politicians and parties actively using
    the platform. This rise in political activity on Twitter has attracted researchers' interest, making election
    prediction based on Twitter data a popular field. Researchers now analyze citizen sentiment to estimate candidate
    performance in elections ([Garcia et al., 2019](https://dl.acm.org/doi/pdf/10.1145/3339909)).
    """)
  
    # Streamlit radio button to select between 'Global' and 'USA'
    view = st.radio("Select View", ['Global_popularity', 'USA_popularity'])
    # Filter data based on the selected view
    if view == "USA_popularity":  # USA View
        img = Image.open('png/trump_biden_popularity_US.png')
        # Additional Conclusion Section
        conclusion = f"""
            <div style='text-align: justify;'>
                This bar chart reveals important insights into the relative popularity of Donald Trump and
                Joe Biden on Twitter during the 2020 U.S. presidential election. A total of <strong>394,400</strong> tweets 
                were recorded, with <strong>213,263</strong> tweets using the Trump hashtag and <strong>181,137</strong> 
                tweets associated with the Biden hashtag. These figures indicate the level of public interest and the extent
                of discussions surrounding each candidate's campaign in the <strong>{view}</strong> dataset.
            </div>
        """

    else:  # Global View
        img = Image.open('png/trump_biden_popularity_global.png')
        conclusion = f"""
            <div style='text-align: justify;'>
                This bar chart reveals important insights into the relative popularity of Donald Trump and
                Joe Biden on Twitter during the 2020 U.S. presidential election. A total of <strong>796,527</strong> tweets 
                were recorded, with <strong>442,748</strong> tweets using the Trump hashtag and <strong>353,779</strong> 
                tweets associated with the Biden hashtag. These figures indicate the level of public interest and the extent
                of discussions surrounding each candidate's campaign in the <strong>{view}</strong> dataset.
            </div>
        """
    st.markdown("**Twitter Popularity % - Trump vs Biden**")
    # Display the chart in Streamlit
    st.image(img, caption="Popularity Analysis - Trump vs Biden", use_column_width=True)
    st.markdown(conclusion, unsafe_allow_html=True)

    # Adding space between the paragraph and the chart
    st.markdown("<br><br>", unsafe_allow_html=True)

    view2 = st.radio("Select View", ['Global_daily', 'USA_daily'])
    # Filter data based on the selected view
    if view2 == "USA_daily":  # USA View
        img = Image.open('png/trump_biden_daily_US.png')

    else:  # Global View
        img = Image.open('png/trump_biden_daily_global.png')

    st.image(img, caption="Daily Tweet Posted - Trump vs Biden", use_column_width=True)
    # Additional Conclusion Section
    st.markdown("""
        <p style='text-align: justify;'>
            The spikes in tweet activity on <strong>October 23</strong>, <strong>November 4</strong>, and <strong>November 7</strong>, 2020, reflect pivotal
            moments in the 2020 U.S. presidential election. The October 23 spike corresponded to the final
            debate between Donald Trump and Joe Biden, which significantly engaged voters on social media.
            The peak on November 4 occurred the day after the election as results began to unfold, prompting
            widespread discussion. Finally, the surge on November 7 followed the announcement of Joe Biden's
            victory, highlighting the mass mobilization of public sentiment on Twitter.
        </p>
    """, unsafe_allow_html=True)

    # Adding space between the paragraph and the chart
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Streamlit select slider to select between 'Global' and 'USA'
    view3 = st.radio('Select View', options=['Global_hourly', 'USA_hourly'])
    # Filter data based on the selected view
    if view3 == "USA_hourly":  # USA View
        img = Image.open('png/trump_biden_hourly_US.png')
        conclusion = f"""
            <div style='text-align: justify;'>
                In the USA dataset, tweet activity peaks between 01:00-02:00 AM, which could be related to
                post-event discussions, late-night media coverage, or breaking news updates. These hours often
                see active conversations around political events such as debate reactions or campaign
                announcements, especially when critical moments occur late in the evening.  
            </div>
        """
    else:  # Global View
        img = Image.open('png/trump_biden_hourly_global.png')
        conclusion = f"""
            <div style='text-align: justify;'>
                In the global dataset, tweet activity shows a significant spike between 16:00-17:00, marking the
                first time that Joe Biden's tweet volume surpasses Donald Trump's. This time window likely
                corresponds to moments when people worldwide are active on social media, particularly in the late
                afternoon or after work hours. 
            </div>
        """
    
    st.image(img, caption="Hourly Tweet Posted - Trump vs Biden", use_column_width=True)
    # Additional Conclusion Section
    st.markdown(conclusion, unsafe_allow_html=True)
