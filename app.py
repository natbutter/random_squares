import streamlit as st
import numpy as np

# Function to generate random colors
def generate_random_color():
    color = "#{:02x}{:02x}{:02x}".format(np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
    return color

# Function to generate random numbers between 1 and 20
def generate_random_number():
    return np.random.randint(1, 21)

# Streamlit app
st.title("Random Color Squares")

# Create a 5x5 grid of squares
for i in range(5):
    row = st.columns(5)
    for j in range(5):
        color = generate_random_color()
        number = generate_random_number()
        with row[j]:
            st.markdown(f'<div style="background-color: {color}; text-align: center;">{number}</div>', unsafe_allow_html=True)


