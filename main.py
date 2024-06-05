import streamlit as st
import whisper
import tempfile

st.title("Audio Transcriber")

# Upload audio file with Streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

model = whisper.load_model("base")


if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")

        # Save the uploaded file temporarily to disk
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(audio_file.read())
            temp_file_path = temp_file.name
        
        # Transcribe the temporary file
        transcription = model.transcribe(temp_file_path)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])
        
        # Clean up temporary file
        import os
        os.remove(temp_file_path)
    else:
        st.sidebar.error("Please upload an audio file")

st.sidebar.header("Play Original Audio File")
if audio_file is not None:
    st.sidebar.audio(audio_file)