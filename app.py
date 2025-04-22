# app.py
import streamlit as st
from PIL import Image
from io import BytesIO
from demo import test_genomic_model

# Set up Streamlit app title and description
st.title('Genomic Interpreter')
st.write('Enter a 512 character DNA sequence and get the output.')

# Get user input
sequence_input = st.text_input('Enter 512 character sequence:')
if st.button('Generate Output'):
    if len(sequence_input) != 512:
        st.error('Please enter exactly 512 characters.')
    else:
        # Call function to get image output from model
        image_output = test_genomic_model(sequence_input)

        # Convert image data to PIL Image
        img = Image.open(BytesIO(image_output))

        # Display image output
        st.image(img, caption='Model Output', use_column_width=True)
