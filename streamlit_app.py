# Required Libraries
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = st.secrets['thingspeak']['channel1']

# Streamlit App
def main():
    st.title("ThingSpeak Data Visualization")
    
    # Fetch data from ThingSpeak
    URL = f"https://api.thingspeak.com/channels/2183188/feeds.json?api_key={api_key}&results=100"
    response = requests.get(URL)
    data = response.json()
    
    # Process data
    df = pd.DataFrame(data['feeds'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    
    # Assuming the field name is "field1", you can modify this as per your ThingSpeak channel fields.
    if 'field1' in df.columns:
        st.sidebar.write(df[['created_at', 'field1']])
        
        # Plot data
        fig, ax = plt.subplots()
        ax.plot(df['created_at'], df['field1'])
        ax.set(xlabel='Time', ylabel='Value', title='ThingSpeak Data for Field1')
        ax.grid()
        st.pyplot(fig)
    else:
        st.write("Field1 not found in the fetched data. Please adjust the field name accordingly.")

if __name__ == "__main__":
    main()
