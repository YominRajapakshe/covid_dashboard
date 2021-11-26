from Libraries import *
import streamlit as st

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("http://wp.bssnews.net/wp-content/uploads/2020/05/GettyImages-1209679043.jpg")
    }
   .sidebar .sidebar-content {
        background: url("http://wp.bssnews.net/wp-content/uploads/2020/05/GettyImages-1209679043.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('🦠 Covid-19 Data and Statistics Visualization Dashboard 💉😷')
st.sidebar.title('Adjust your Parameters of the Covid Dashboard')

countries = ['United States', 'United Kingdom', 'Australia', 'China', 'Egypt', 'Sri Lanka', 'France', 'Canada', 'India', 'Brazil', 'Denmark', 'Turkey', 'Vietnam', 'Argentina', 'Mexico', 'Japan']
data_types = ['cases', 'deaths', 'recovered']

country_code = {'Sri Lanka': 'lk', 'United States': 'us', 'United Kingdom': 'gb',
                'China': 'cn', 'India': 'in', 'Mexico': 'mx', 'Denmark': 'dk', 'Brazil': 'br', 'France': 'fr', 'Vietnam': 'vn', 'Argentina': 'ar', 'Japan': 'jp', 'Canada': 'ca', 'Turkey': 'tr', 'Australia': 'au', 'Egypt': 'eg'}

data_types = ['cases', 'deaths', 'recovered']
country = st.sidebar.selectbox('Select the Country', countries)

days = st.sidebar.slider('Select the no. of Days', min_value=1, max_value=100)
data_type = st.sidebar.multiselect('Select the data types', data_types)

total_cases = get_historic_cases(country, str(days))
total_deaths = get_historic_deaths(country, str(days))
total_recoveries = get_historic_recoveries(country, days)
total_df = pd.concat([total_cases, total_deaths, total_recoveries], axis=1).astype(int)

daily_cases = get_daily_cases(country, str(days))
daily_deaths = get_daily_deaths(country, str(days))
daily_recoveries = get_daily_recoveries(country, str(days))
daily_df = pd.concat([daily_cases, daily_deaths, daily_recoveries], axis=1).astype(int)

yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)

col1, col2 = st.columns(2)
col1.metric(label="Selected Country", value=country)
col2.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")

col1, col2, col3 = st.columns(3)
col1.metric('Total Cases', yesterday_cases)
col2.metric('Total Deaths', yesterday_deaths)
col3.metric('Total Recovered', yesterday_recoveries)

st.line_chart(daily_df[data_type])

st.video('https://www.youtube.com/watch?v=5DGwOJXSxqg')

st.title('How to prevent Covid-19 Virus?')

st.write('> Always wash your hands with soap or santitizers for 20 seconds.')
st.write('> Always wear a mask when you are leaving your house to go anywhere.')
st.write('> Have a distance of 2 meters from other people for saftey reasons.')
st.write('> Get vaccinated with the vaccine that the goverment has released.')
st.write('> Do exercises and have a nutrious meal in order to stay healthy.')
st.write('> Follow and respect the rules given by the goverment to your country.')
st.write('> Improve your immunity system in order to prevent the Covid-19 virus.')
