# Import necessary libraries
import streamlit as st
from transformers import pipeline, set_seed

# Load the GPT-2 text generation pipeline
generator = pipeline('text-generation', model='gpt2')  # You can also try 'gpt2-medium', 'gpt2-large'
set_seed(42)  # Ensures consistent output for the same input

# Streamlit Web App Title
st.title("Next Sentence Prediction using Generative AI")

# Instructions
st.write("This app uses GPT-2 to generate the next possible sentence(s) based on your input.")

# Input box for the user to enter a sentence
input_text = st.text_input("Enter your sentence here:", placeholder="e.g., The sun was setting over the hills")

# When user enters input, generate next sentences
if input_text:
    st.subheader("Generated Sentences:")

    # Generate 3 next sentence predictions (max 50 tokens)
    outputs = generator(
        input_text,
        max_length=50,              # Total length (input + generated text)
        num_return_sequences=3,     # Generate 3 variations
        do_sample=True,             # Enables randomness/creativity
        temperature=0.7             # Controls randomness (0.7 = balanced)
    )

    # Display each generated sentence
    for i, output in enumerate(outputs):
        generated = output['generated_text']
        st.write(f"**{i+1}.** {generated}")