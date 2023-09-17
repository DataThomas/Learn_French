import folium
import numpy as np
import pandas as pd
import speech_recognition as sr
import streamlit as st
from streamlit_folium import folium_static

# loading data
data = pd.read_csv("df_french.csv", delimiter=";")
df = pd.DataFrame(data)

# transforming data
df["Country"] = df["Country"].str.replace("\xa0", " ").str.strip()
df["French_Speakers"] = df.French_Speakers.str.replace(",", "").astype(int)
df["Percent"] = df.Percent.str.replace(",", "").astype(int)/100

def page_home():

    st.title("Why you should learn French")

    # Interesting about French Language
    st.text("Total Speakers:  270 million (2022)")


    # Sidebar for zoom level selection
    st.sidebar.header("Map Settings")
    zoom_level = st.sidebar.slider("Zoom Level", 1, 10, 2)

    # @st.cache_data
    def create_map(df, zoom_level):
        st.subheader("Map of French Speakers in Absolute Values")
        # Create a map 
        m = folium.Map(location=[0.000000, 5.000000], zoom_start=zoom_level, tiles="Stamen Terrain",
                    width=800, height=600)

        # Create a choropleth map
        folium.Choropleth(
            geo_data="https://datahub.io/core/geo-countries/r/0.geojson",  # GeoJSON file with country boundaries
            name='choropleth',
            data=df,
            columns=['Country', 'French_Speakers'],
            key_on='feature.properties.ADMIN',
            fill_color='YlGnBu',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='French Speakers by Country',
        ).add_to(m)

        # Add a layer control
        folium.LayerControl().add_to(m)

        return m

    # # Display the map using Streamlit
    # folium_static(m) 

    m = create_map(df, zoom_level)

    folium_static(m) 
    # st.write(m) 

    st.subheader("Map of French Speakers in Percent of Population")
    # Create a map centered around France
    m2 = folium.Map(location=[0.000000, 5.000000], zoom_start=zoom_level, tiles="Stamen Terrain",
                width=800, height=600)

    # Create a choropleth map
    folium.Choropleth(
        geo_data="https://datahub.io/core/geo-countries/r/0.geojson",  # GeoJSON file with country boundaries
        name='choropleth',
        data=df,
        columns=['Country', 'Percent'],
        key_on='feature.properties.ADMIN',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='French Speakers by Country',
    ).add_to(m2)

    # Add a layer control
    folium.LayerControl().add_to(m2)

    # Display the map using Streamlit
    folium_static(m2) 



def practice_french():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    vocab = {"a cat": "un chat",
             "a dog": "un chien",
             "the bed": "le lit",
             "an apple": "une pomme",
             "a bike": "un vélo"}
    
    image_urls = ["https://i.imgur.com/AyzqgfW.jpg?2",
                  "https://i.imgur.com/HdKhKdA.jpg?1",
                  "https://i.imgur.com/cfTxiU5.jpg",
                  "https://i.imgur.com/QjdqdtH.jpg"]

    #current_card = 0
    # Initialize the current card index using st.session_state
    if 'current_card' not in st.session_state:
        st.session_state.current_card = 0

    st.title("Practice your French")

    def display_card(card_index):
        english_word = list(vocab.keys())[card_index]
        french_word = vocab[english_word]
        image_url = image_urls[card_index]

        st.image(image_url, caption=f"Word: {english_word}")

        button_label = f"Click to Start - Vocab {card_index+1}"
        if st.button(button_label):
            # Use the default microphone as the audio source
            with sr.Microphone() as source:
                st.text("Please start speaking")
                try:
                    audio = recognizer.listen(source, timeout=10)  # Capture audio from the microphone for up to 10 seconds
                    st.text("Recognizing...")
                    user_input = recognizer.recognize_google(audio, language="fr-FR")  # Recognize speech in French
                    st.write("You said:", user_input)
                    if user_input.lower() == french_word.lower():
                        st.success("Congratulations! You got it right.")
                except sr.WaitTimeoutError:
                    st.write("No speech detected. Timeout exceeded.")
                except sr.UnknownValueError:
                    st.write("Speech Recognition could not understand the audio")
                except sr.RequestError as e:
                    st.write(f"Could not request results from Speech Recognition service; {e}")
    
    display_card(st.session_state.current_card)

    # Button to switch to the next card
    if st.button("Next Card"):
        st.session_state.current_card = (st.session_state.current_card + 1) % len(vocab)  # Move to the next card
        st.text("")  # Clear any previous recognition result
        display_card(st.session_state.current_card)

page = st.sidebar.selectbox("Select a page:", ("Home - Why Learn French", "Practice Speaking", "Other"))


if page == "Home - Why Learn French":
    page_home()
elif page == "Practice Speaking":
    practice_french()
else:
    page_home()