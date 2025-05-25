import os
import sys
import streamlit as st
import torch
import warnings

# Suppress specific warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', message='.*torch.cuda.amp.autocast.*')

# Add the tortoise-tts directory to the Python path
tortoise_dir = os.path.dirname(os.path.abspath(__file__))
if tortoise_dir not in sys.path:
    sys.path.insert(0, tortoise_dir)

from tortoise.api import TextToSpeech
import soundfile as sf
import tempfile

# Constants
VOICES_DIR = os.path.join(tortoise_dir, 'tortoise', 'voices')
PRESETS = ["ultra_fast", "fast", "standard", "high_quality"]

def get_available_voices():
    """Get list of available voice options"""
    voices = ["random"]  # Always include random
    if os.path.exists(VOICES_DIR):
        voices.extend([d for d in os.listdir(VOICES_DIR) if os.path.isdir(os.path.join(VOICES_DIR, d))])
    return voices

@st.cache_resource
def init_tts_model():
    try:
        st.info("Loading TTS model...")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = TextToSpeech(device=device)
        return model
    except Exception as e:
        st.error(f"Error initializing TTS model: {str(e)}")
        return None

def generate_audio(text, voice_name, preset):
    try:
        if 'tts' not in st.session_state:
            st.session_state.tts = init_tts_model()
            
        if st.session_state.tts is None:
            st.error("TTS model not initialized")
            return None
            
        with torch.inference_mode():
            audio = st.session_state.tts.tts(text, voice_name, preset)
            
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            
        return audio[0] if isinstance(audio, list) else audio
    except Exception as e:
        st.error(f"Error generating audio: {str(e)}")
        return None

def save_audio(audio_data, sample_rate=24000):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
            sf.write(tmp.name, audio_data, sample_rate)
            return tmp.name
    except Exception as e:
        st.error(f"Error saving audio: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="Tortoise TTS",
        page_icon="🐢",
        layout="wide"
    )

    st.title("🐢 Tortoise Text-to-Speech")
    st.write("Generate natural-sounding speech from text")

    if torch.cuda.is_available():
        st.success(f"Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        st.warning("Running on CPU (this will be slow)")

    # Input section
    text_input = st.text_area("Enter text to convert to speech:", height=150)
    
    col1, col2 = st.columns(2)
    with col1:
        voice_name = st.selectbox("Select voice:", get_available_voices())
    with col2:
        preset = st.selectbox("Select quality preset:", PRESETS)

    if st.button("Generate Speech"):
        if not text_input.strip():
            st.warning("Please enter some text")
            return

        with st.spinner("Generating speech..."):
            audio_data = generate_audio(text_input, voice_name, preset)
            
            if audio_data is not None:
                audio_file = save_audio(audio_data)
                if audio_file:
                    st.audio(audio_file)
                    st.download_button(
                        "Download audio",
                        open(audio_file, 'rb'),
                        file_name=f"tts_output.wav",
                        mime="audio/wav"
                    )

if __name__ == "__main__":
    main()
