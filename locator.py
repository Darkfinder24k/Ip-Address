import streamlit as st
import os
import random
import platform

# Fake hacked messages
hacked_messages = [
    "HACKED! Your data is mine!",
    "Warning: Unauthorized access detected!",
    "Your phone will self-destruct in 10 seconds...",
    "April Fools! But seriously, be careful!",
    "System breach detected! All files compromised!",
    "You shouldn't have opened this app..."
]

# Session state for tracking messages
if 'message_count' not in st.session_state:
    st.session_state.message_count = 0

st.title("Chat App")
user_input = st.text_input("Send a message:")

if st.button("Send") and user_input:
    # Display hacked message randomly
    fake_message = random.choice(hacked_messages)
    st.warning(fake_message)
    
    # Increment message count
    st.session_state.message_count += 1

    # If 20 messages are sent, trigger shutdown option
    if st.session_state.message_count >= 20:
        st.error("Critical Error! Click below to shut down...")
        
        if st.button("Confirm Shutdown"):
            try:
                system_platform = platform.system()
                if system_platform == "Windows":  # Windows shutdown
                    os.system("shutdown /s /t 5")
                elif system_platform == "Linux":  # Linux shutdown
                    os.system("shutdown -h now")
                elif system_platform == "Darwin":  # macOS shutdown
                    os.system("sudo shutdown -h now")
                elif system_platform == "Android":  # Android (ADB required)
                    os.system("adb shell reboot -p")
                else:
                    st.error("Shutdown not supported on this OS.")
            except Exception as e:
                st.error(f"Shutdown failed: {e}")
