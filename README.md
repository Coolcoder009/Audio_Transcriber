# Audio_Transcriber   

Audio Transcriber is a web application that transcribes audio files using the Whisper model. Users can upload an audio file in various formats and get the transcribed text displayed on the web interface.

## Installation

1. Clone the repository 
```bash 
git clone <repository-url>
cd <repository-directory>
```

2. To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

4. Running the Application
To start the application, run:
```bash
streamlit run main.py 
``` 
This will start the Streamlit server, and the application will be accessible at http://localhost:8501.

## How It Works
### Frontend
The frontend of the application is built using Streamlit. It provides a simple user interface where users can:
<ul>
<li>Upload an audio file.</li>
<li>Transcribe the uploaded audio.</li>
<li>Play the original audio file.</li>
</ul>

### Backend
The backend of the application is powered by Streamlit and Whisper. The main components are:

### Model Loading
The Whisper model is loaded when the application starts.

### Audio Transcription
Users can upload an audio file in .wav, .mp3, or .m4a format. When the "Transcribe Audio" button is clicked, the audio file is sent to the backend for transcription.
The backend reads the audio file and transcribes it using the Whisper model.
The transcribed text is then displayed on the web interface.

### File Handling
The application allows users to upload audio files directly through the interface. The uploaded file is temporarily saved, processed for transcription, and then deleted after processing.

### Example Usage
Upload an Audio File: Click on the "Upload Audio" button and select a file in .wav, .mp3, or .m4a format.<br>
Transcribe the Audio: Click on the "Transcribe Audio" button in the sidebar to start the transcription process. The transcribed text will be displayed on the main page.<br> 
Play the Original Audio: Use the audio player in the sidebar to listen to the uploaded audio file.



