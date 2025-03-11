import streamlit as st
import re

# Set page configuration
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

# Custom CSS for slightly darker light purple background
st.markdown(
    """
    <style>
    body {
        background-color: #D8BFD8; /* Thistle Purple */
        color: black; /* Black text for readability */
    }
    .stApp {
        background-color: #D8BFD8;
    }
    .stTextInput>div>div>input {
        background-color: white !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔐 Password Strength Meter🚀")
st.markdown("""
## 🔍 Welcome to the ultimate password strength meter!
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
We will give you helpful tips to create a **Strong Password** 🔒
""")

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("✖ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password): 
        score += 1      
    else:
        feedback.append("✖ Password should contain both upper and lower case characters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("✖ Password should contain at least one digit.")

    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("✖ Password should contain at least one special character (!@#$%&*).")   
    
    if score == 4:
        feedback.append("✅ Your password is strong! 🎉")
    elif score == 3:
        feedback.append("🌕 Your password is medium strength. It could be stronger.")     
    else:
        feedback.append("🔴 Your password is weak. Please make it stronger.")   

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip) 
else:
    st.info("Please enter your password to get started.")     
