import os
import google.generativeai as genai
from apikey import google_gemini_api_key  

# Configure the API key (use the variable, not a string literal)
genai.configure(api_key=google_gemini_api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

# Streamlit app setup
import streamlit as st

st.set_page_config(layout="wide")
st.title("AI Blog Companion")
st.subheader('Craft your blog with AI')

with st.sidebar:
    st.title("Blog details")
    st.subheader("Enter details of the blog you want to generate")
    
    # Collect user inputs
    blog_title = st.text_input("Title")
    keywords = st.text_input("Keywords (comma separated)")
    num_words = st.slider("Number of words", min_value=200, max_value=1000, step=50)
    # num_images = st.number_input("Number of images", min_value=1, max_value=2)

    # Construct system instruction with f-string
    system_instruction = (
        f"Generate a comprehensive, engaging blog post titled '{blog_title}' "
        f"that includes the following keywords: {keywords}. "
        f"The blog should be approximately {num_words} words in length, "
        "suitable for an online audience. Ensure the content is original, "
        "informative, and maintains a consistent tone throughout."
    )

    # Button to generate the blog
    submit_button = st.button("Generate blog")

# Handle the button click and generate blog
if submit_button:
    # Send the system instruction
    response = chat_session.send_message(system_instruction)

    # Debug: Print the response to understand its structure
    # st.write(response)  # This will print the entire response object to inspect its fields

    # Assuming the text is contained in response.text or similar field
    # Update this line based on the actual structure of the response
    if hasattr(response, 'text'):  # Check if 'text' is an attribute
        st.write(response.text)
    else:
        st.write("The response object does not contain a 'text' attribute. Inspect the response above.")
