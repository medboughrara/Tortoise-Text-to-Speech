@echo off
set CUDA_LAUNCH_BLOCKING=0
set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
call tts_env\Scripts\activate
streamlit run app_new.py