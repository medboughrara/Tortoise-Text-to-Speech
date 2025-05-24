# Tortoise TTS Setup and Usage

This repository contains a setup of Tortoise TTS, a text-to-speech system implemented in Python. This implementation includes the necessary configurations and dependencies for running on Windows with CUDA support.

## Setup Information

- Python environment: Python 3.10
- CUDA version: CUDA 12.1
- PyTorch version: 2.1.0+cu121

## Key Dependencies

- torch==2.1.0+cu121
- numpy==1.24.3
- transformers==4.31.0
- tokenizers==0.13.3
- einops==0.4.1
- librosa==0.9.1
- And other supporting packages

## Project Structure

The project contains:
- `tortoise-tts/`: Main package directory
- `tts_env/`: Virtual environment
- Various example audio files and demonstration outputs

## Usage

Basic usage example:
```python
python tortoise/do_tts.py --text "Your text here" --voice random --preset fast
```

## Features

- Multiple voice options available
- Fast inference preset for quicker generation
- CUDA support for GPU acceleration
- Example outputs in various styles

## License

This project uses the original Tortoise TTS license. See the LICENSE file in the tortoise-tts directory for more details.
