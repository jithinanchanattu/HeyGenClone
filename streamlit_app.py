import streamlit as st
import os
from translate import translate_video
from speech_changer import overlay_voice_on_video

# Define Streamlit UI
st.title('HeyGenClone App')

uploaded_file = st.file_uploader("Upload a video", type=['mp4'])

if uploaded_file is not None:
    output_language = st.selectbox("Select output language", ["es", "fr", "de", "it", "pt", "pl", "tr", "ru"])  # Add more languages as needed

    if st.button("Process"):
        with st.spinner('Processing...'):
            # Save uploaded file
            file_path = os.path.join("uploads", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Process video
            output_filename = f"output_{uploaded_file.name}"
            translate_video(file_path, output_language, output_filename)  # Assuming translate_video function is defined in translate.py

            # Display output video
            st.video(output_filename)

            # Offer download link
            st.markdown(f"### [Download output video](/{output_filename})")

            # Delete uploaded file and output file after processing
            os.remove(file_path)
            os.remove(output_filename)
