import requests
import streamlit as st
import pandas as pd
from requests.auth import HTTPDigestAuth
import matplotlib.pyplot as plt

# Set the URL and API key
url = "https://data.tidbcloud.com/api/v1beta/app/dataapi-jjREhvLj/endpoint/inventory"

# Make the API request
response = requests.get(url, auth=HTTPDigestAuth('OgbvDm6y', '3678e5c9-71c5-45a0-89ae-faecffda97da'))

# Check the response status code
if response.status_code == 200:
    # Extract inventory data from response
    data = response.json()['data']['rows']
    labels = [inventory['name'] for inventory in data]
    quantities = [inventory['quantity'] for inventory in data]

    # Create pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(quantities, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.title('Inventory')

    # Display chart in Streamlit app
    st.pyplot(fig1)
else:
    # Display an error message if the request fails
    st.error(f"Error: {response}")
