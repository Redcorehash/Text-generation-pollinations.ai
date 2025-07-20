import streamlit as st
import requests
import json  # Import the json module

# Function to fetch available models from Pollinations API
def get_available_models():
        response = requests.get("https://text.pollinations.ai/models")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response
        models = response.json()
        
        return models
  
# Function to generate text using Pollinations API
def generate_text(prompt, model_name):
        payload = {"prompt": prompt, "model": model_name}
        response = requests.post("https://text.pollinations.ai/generate", json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses

        data  = response.json() # Parse response as JSON
        text = data.get("output", "")  # Safely get the "output"

        return text



# Streamlit app
st.title("Text Generation with Pollinations AI")

# Model selection
available_models = get_available_models()

if available_models:
    model_names = [model["name"] for model in available_models]  # Extract model names

    selected_model = st.selectbox("Select a Model", model_names)

    # Text input for the prompt
    prompt = st.text_area("Enter your prompt:", "Write a short story about a cat who goes on an adventure.")

    # Generate button
    if st.button("Generate Text"):
        if prompt:
            with st.spinner("Generating text..."):
                generated_text = generate_text(prompt, selected_model)

            if generated_text:
                st.subheader("Generated Text:")
                st.write(generated_text)
        else:
            st.warning("Please enter a prompt.")
else:
    st.error("Could not retrieve available models. Check your internet connection and the Pollinations AI API.")
