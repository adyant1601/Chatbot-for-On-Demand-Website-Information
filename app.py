import requests
import streamlit as st
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# GUI for user input
st.title("NIT Trichy Bot")
input_data = st.text_input("Enter your Query")
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"  # Chrome-specific User-Agent string
}

if st.button("Get Response"):
    response = requests.post("https://cf37-34-151-81-214.ngrok-free.app/predict",
			     json={'query': input_data},
			     verify=False, headers=headers)
    
    try:
        json_response = response.json()
        # Display the response as an h2-like title
        st.markdown(f"## {json_response['response']}")
    except ValueError:
        st.write("Error: Response is not JSON format")
