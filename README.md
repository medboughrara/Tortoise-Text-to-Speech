# Tortoise Text-to-Speech Web Interface

A Streamlit-based web interface for the Tortoise-TTS system, making it easy to generate high-quality speech from text using various voices and quality presets.

## Features

- User-friendly web interface using Streamlit
- Support for multiple preset voices
- Quality presets from ultra-fast to high-quality
- GPU acceleration support
- Easy text input and audio output
- Download generated audio files
- Real-time status updates and error handling

## Requirements

- Python 3.9+
- CUDA-capable GPU (recommended)
- Required Python packages (install using `pip install -r requirements.txt`):
  - torch
  - torchaudio
  - streamlit
  - soundfile
  - numpy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/medboughrara/Tortoise-Text-to-Speech.git
cd Tortoise-Text-to-Speech
```

2. Create and activate a virtual environment:
```bash
python -m venv tts_env
source tts_env/bin/activate  # On Windows: tts_env\Scripts\activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the web interface:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter text, select a voice and quality preset, then click "Generate Speech"

## Quality Presets

- **ultra_fast**: Fastest generation, lower quality
- **fast**: Quick generation with decent quality
- **standard**: Balanced speed and quality
- **high_quality**: Best quality, slower generation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
