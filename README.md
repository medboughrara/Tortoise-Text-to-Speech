# TorToiSe Text-to-Speech

A user-friendly web interface for Tortoise TTS, making it easy to generate high-quality speech from text using various voices and quality presets.

Tortoise is a text-to-speech program built with the following priorities:

1. Strong multi-voice capabilities.
2. Highly realistic prosody and intonation.
   
This repo contains all the code needed to run Tortoise TTS in inference mode, along with a custom Streamlit web interface for easy text-to-speech generation.

Based on the original work: https://arxiv.org/abs/2305.07243

## 🌟 Features

- **Multi-voice synthesis** with highly realistic prosody
- **User-friendly web interface** built with Streamlit
- **CUDA-accelerated** processing for faster generation
- **Multiple quality presets** from fast to high-quality

## Web Interface

A local web UI is available for easy text-to-speech generation:

```bash
streamlit run app.py
```

This will start a local server at http://localhost:8501 where you can:
- Input your text
- Choose from available voices
- Select quality presets
- Generate and play audio directly in your browser

## Hugging Face space

Try Tortoise TTS instantly on [Hugging Face Spaces](https://huggingface.co/spaces/Manmay/tortoise-tts).  
*Note: For best performance, duplicate the Space and add a GPU. CPU-only spaces are not supported.*

## Installation

### 1. Clone the repository

>>>>>>> 5a9cbb614d1e83e065d8ce76c0403d1dd5fc0802
```bash
git clone https://github.com/medboughrara/Tortoise-Text-to-Speech.git
cd Tortoise-Text-to-Speech
```

### 2. Install dependencies

It is **highly recommended** to use a virtual environment:

```bash
python -m venv tts_env
tts_env\Scripts\activate  # On Windows
source tts_env/bin/activate  # On Linux/Mac

# Install requirements
pip install -r requirements.txt
```

## Usage

1. Start the web interface:

pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Download voice samples

Make sure the `tortoise/voices` directory exists and contains voice samples.  
You can find official voices in the [Tortoise TTS voices repo](https://github.com/neonbjb/tortoise-tts-voices).

## Usage

### Run the Web UI

>>>>>>> 5a9cbb614d1e83e065d8ce76c0403d1dd5fc0802
```bash
streamlit run app.py
```

<<<<<<< HEAD
2. Open your browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter text, select a voice and quality preset, then click "Generate Speech"

## Quality Presets

- **ultra_fast**: Fastest generation, lower quality
- **fast**: Quick generation with decent quality
- **standard**: Balanced speed and quality
- **high_quality**: Best quality, slower generation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
=======
- Open [http://localhost:8501](http://localhost:8501) in your browser.
- Enter your text, select a voice and preset, and click **Generate Speech**.

### Command-line Usage

Generate speech from the terminal:

```bash
python tortoise/do_tts.py --text "I'm going to speak this" --voice random --preset fast
```

## Troubleshooting

- **App stuck on loading:**  
  - Ensure your GPU drivers and CUDA are properly installed.
  - Check that the `tortoise/voices` directory exists and is populated.
  - Run Streamlit with debug logging:  
    `streamlit run --logger.level=debug app.py`
  - Check the terminal for error messages.

- **Shape errors or CUDA errors:**  
  - Make sure your PyTorch and CUDA versions are compatible.
  - Try using a different voice or preset.

## Citation

If you use this project in your research, please cite the [manuscript](https://arxiv.org/abs/2305.07243).

## Acknowledgements

- Inspired by Mojave desert flora and fauna.
- Thanks to Patrick von Platen for guides on wav2vec dataset setup.

## Contact

- GitHub: [medboughrara](https://github.com/medboughrara)
- Email: boughraramouhamed1@gmail.com

---

*Happy synthesizing!*
>>>>>>> 5a9cbb614d1e83e065d8ce76c0403d1dd5fc0802
