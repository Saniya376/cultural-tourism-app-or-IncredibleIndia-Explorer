import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# -------------------- Page Config --------------------
st.set_page_config(page_title="Incredible India: Culture & Tourism Explorer", layout="wide")

# -------------------- Logo & Styling --------------------
logo = Image.open("logo.png")  # Ensure logo.png is in the same folder
st.image(logo, width=150)

st.markdown(
    """
    <style>
    .main {
        background-color: #f4f4f9;
    }
    h1, h2, h3 {
        color: #003366;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Incredible India: Culture & Tourism Explorer")

st.markdown("""
Welcome! 🇮🇳  
Discover traditional art forms, vibrant festivals, hidden cultural gems, and promote responsible tourism.

**Tourism Columns:**
""")

# -------------------- Load Data --------------------
heritage_df = pd.read_csv("data/cultural_heritage_2021.csv.csv")
tourism_df = pd.read_csv("data/Tourist Arrival Statistics.csv")

# -------------------- Debug Column Names --------------------
st.write("Tourism Columns:")
st.write(list(tourism_df.columns))

# -------------------- Tabs --------------------
tab1, tab2, tab3 = st.tabs(["🏛 Heritage Sites", "📊 Tourist Trends", "💡 Insights"])

with tab1:
    st.subheader("🕌 Cultural Heritage Sites")
    st.write("A collection of cultural heritage sites across India.")
    st.dataframe(heritage_df)

    # FIXED COLUMN NAME ERROR HERE
    site_counts = heritage_df['City Name'].value_counts().reset_index()
    site_counts.columns = ['City Name', 'Count']

    bar_chart = alt.Chart(site_counts).mark_bar().encode(
        x=alt.X('City Name', title='City'),
        y=alt.Y('Count', title='Number of Heritage Sites'),
        tooltip=['City Name', 'Count'],
        color=alt.value('#006699')
    ).properties(
        width=700,
        height=400,
        title='Number of Heritage Sites by City'
    )
    st.altair_chart(bar_chart, use_container_width=True)

with tab2:
    st.subheader("📈 Tourist Arrival Trends")
    st.write("Trends in foreign tourist and NRI arrivals from 1981 to 2017.")

    # Clean up columns just in case
    tourism_df.columns = tourism_df.columns.str.strip()

    # Convert 'Year' to string if needed
    tourism_df['Year'] = tourism_df['Year'].astype(str)

    # Foreign Tourist Arrivals line chart
    fta_chart = alt.Chart(tourism_df).mark_line(point=True).encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('FTAs (in millions):Q', title='Number of Foreign Tourists (millions)'),
        tooltip=['Year', 'FTAs (in millions)']
    ).properties(
        title='Foreign Tourist Arrivals Over the Years'
    )
    st.altair_chart(fta_chart, use_container_width=True)

    # NRI Arrivals chart
    nri_chart = alt.Chart(tourism_df).mark_area(opacity=0.6).encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('NRI Arrivals (in millions):Q', title='Number of NRI Tourists (millions)'),
        tooltip=['Year', 'NRI Arrivals (in millions)'],
        color=alt.value('#FFA07A')
    ).properties(
        title='NRI Tourist Arrivals Over the Years'
    )
    st.altair_chart(nri_chart, use_container_width=True)

with tab3:
    st.subheader("💡 Key Insights & Recommendations")
    st.markdown("""
    - 🟢 States like Maharashtra, Tamil Nadu, and Uttar Pradesh have the highest number of cultural heritage sites.
    - 🔺 Tourist arrivals peaked around the mid-2010s, showing consistent interest in Indian heritage.
    - 🔍 North-Eastern states have fewer tourist visits — these are high-potential unexplored regions.
    - 📢 Promote eco-tourism and offbeat destinations to reduce pressure on mainstream sites.
    - 🌐 Integrate digital storytelling and interactive guides using AR/VR to enhance cultural experiences.
    """)



