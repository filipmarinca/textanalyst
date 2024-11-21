import streamlit as st
import pandas as pd
import docx2txt


def import_data(file):
    """Read a CSV file and return a DataFrame."""
    return pd.read_csv(file)  # Return DataFrame from the CSV file.


def main():
    """Run the main function for the Streamlit app."""
    st.title("Text Analyzer")  # Set the title of the app.

    uploaded_file = st.file_uploader("Choose a file", type=["txt", "doc", "docx"])
    # File uploader widget for text and Word files.

    if uploaded_file is not None:  # Check if a file was uploaded.
        if uploaded_file.type == "text/plain":  # Check if the file is plain text.
            text = uploaded_file.read().decode("utf-8")
            # Read and decode the text file.
        else:  # If the file is a Word document.
            text = docx2txt.process(uploaded_file)  # Extract text from .docx file.

        num_chars = len(text)  # Calculate number of characters.
        num_words = len(text.split())  # Calculate number of words.
        num_sentences = text.count(". ") + text.count("? ") + text.count("! ")
        # Calculate number of sentences.

        st.write("Number of characters:", num_chars)  # Display number of characters.
        st.write("Number of words:", num_words)  # Display number of words.
        st.write("Number of sentences:", num_sentences)  # Display number of sentences.


if __name__ == "__main__":  # Check if script is run directly.
    main()  # Execute main function.
