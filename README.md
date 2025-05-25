# 🐢 TorToiSe Text-to-Speech

A powerful and user-friendly web interface for Tortoise TTS, making it easy to generate high-quality speech from text using various voices and quality presets.

Tortoise is a state-of-the-art text-to-speech system built with the following priorities:

1. Strong multi-voice capabilities with highly realistic prosody
2. Natural-sounding intonation and expression
3. Easy-to-use web interface for quick speech generation

This repository provides:
- Complete Tortoise TTS inference code
- Custom Streamlit web interface
- Multiple voice options and quality presets
- CUDA acceleration support

Based on the original work: [Tortoise: A Fast Text-to-Speech System](https://arxiv.org/abs/2305.07243)

## 🌟 Features

- **Advanced Speech Synthesis**
  - Multi-voice capability with realistic prosody
  - Natural-sounding intonation and expression
  - Support for long-form text
  - Voice customization options

- **User-Friendly Interface**
  - Clean, intuitive Streamlit web UI
  - Real-time status updates
  - Direct audio playback in browser
  - Easy audio file downloads

- **Performance Optimization**
  - CUDA acceleration support
  - Multiple quality presets
  - Efficient memory management
  - Batch processing capability

- **Quality Options**
  - Ultra-fast mode for quick results
  - Standard mode for balanced performance
  - High-quality mode for best results

## 💻 Requirements

- Python 3.9 or later
- CUDA-capable GPU (recommended)
- 8GB+ RAM (16GB+ recommended)
- Windows, Linux, or macOS

## Hugging Face space

Try Tortoise TTS instantly on [Hugging Face Spaces](https://huggingface.co/spaces/Manmay/tortoise-tts).  
*Note: For best performance, duplicate the Space and add a GPU. CPU-only spaces are not supported.*

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/medboughrara/Tortoise-Text-to-Speech.git
cd Tortoise-Text-to-Speech
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv tts_env

# Activate virtual environment
# On Windows:
.\tts_env\Scripts\activate
# On Linux/Mac:
source tts_env/bin/activate
```

### 3. Install Dependencies

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

### 4. Download Voice Samples

1. Create `tortoise/voices` directory if it doesn't exist
2. Download voice samples from the [official Tortoise TTS voices repository](https://github.com/neonbjb/tortoise-tts-voices)
3. Extract voice samples to `tortoise/voices` directory

## 🎯 Usage

### Starting the Web Interface

```bash
streamlit run app.py
```

The interface will be available at [http://localhost:8501](http://localhost:8501)

### Using the Interface

1. Enter your text in the text area
2. Choose a voice from the available options
3. Select a quality preset:
   - **Ultra Fast**: Quick results, lower quality
   - **Fast**: Good balance for shorter texts
   - **Standard**: Recommended for most uses
   - **High Quality**: Best results, slower generation
4. Click "Generate Speech" and wait for processing
5. Play the generated audio directly in browser
6. Download the audio file if desired

### Quality Presets Guide

| Preset | Speed | Quality | Use Case |
|--------|--------|----------|-----------|
| Ultra Fast | ⚡️⚡️⚡️ | ⭐️ | Quick testing |
| Fast | ⚡️⚡️ | ⭐️⭐️ | Short texts |
| Standard | ⚡️ | ⭐️⭐️⭐️ | General use |
| High Quality | 🐢 | ⭐️⭐️⭐️⭐️ | Production |

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request
- Enter your text, select a voice and preset, and click **Generate Speech**.

### Command-line Usage

Generate speech from the terminal:

```bash
python tortoise/do_tts.py --text "I'm going to speak this" --voice random --preset fast
```

## 🔧 Troubleshooting

### Common Issues

1. **CUDA/GPU Issues**
   - Ensure you have a compatible NVIDIA GPU
   - Install latest NVIDIA drivers
   - Verify CUDA installation with `nvidia-smi`

2. **Memory Issues**
   - Try lower quality presets
   - Process shorter text segments
   - Close other GPU-intensive applications

3. **Voice Sample Issues**
   - Verify voice samples are in correct directory
   - Check file permissions
   - Ensure file names match expected format

### Error Messages

- `CUDA out of memory`: Reduce batch size or text length
- `No module named 'torch'`: Reinstall PyTorch
- `Voice not found`: Check voice sample installation

## ✨ Acknowledgments

- Original Tortoise TTS implementation by [neonbjb](https://github.com/neonbjb)
- Voice samples from various contributors
- Built with [Streamlit](https://streamlit.io/)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Happy synthesizing!*
