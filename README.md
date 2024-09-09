# File Summarizer

**File Summarizer** is a desktop application that allows you to transcribe audio files and generate concise summaries of the transcribed text. The tool leverages OpenAI's Whisper for speech-to-text transcription and Hugging Face’s Transformer model for text summarization. The app comes with a simple GUI built using `Tkinter`, making it user-friendly and easy to use.

## Features

- **Audio Transcription**: Automatically converts speech from audio files into text using the Whisper model.
- **Text Summarization**: Generates a concise summary of the transcribed text using Hugging Face's transformer models.
- **Supported Formats**: Supports MP3, MP4, and WAV audio formats for transcription.
- **File Conversion**: Automatically converts MP3 and MP4 files to WAV format using `ffmpeg`.
- **Graphical User Interface**: Easy-to-use interface for selecting files and viewing summaries.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## How It Works

1. **File Selection**: Choose an audio file in MP3, MP4, or WAV format using the provided file selector.
2. **Transcription**: The application transcribes the selected audio file into text using the Whisper model.
3. **Summarization**: The transcribed text is summarized to provide a concise version of the content.
4. **Display**: The summary is displayed in the application window for easy viewing.

## Installation

### Prerequisites

- Python 3.x
- The following Python libraries are required:
  - `whisper`
  - `ffmpeg-python`
  - `transformers`
  - `torch`
  - `tkinter`

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/file-summarizer.git
    cd file-summarizer
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install ffmpeg** (if not already installed):
    - On **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to your system PATH.
    - On **macOS**: Install via Homebrew:
      ```bash
      brew install ffmpeg
      ```
    - On **Linux**:
      ```bash
      sudo apt update
      sudo apt install ffmpeg
      ```

4. **Run the application**:
    ```bash
    python combined.py
    ```
    
## Usage

1. **Select a File**: Click the "Select File" button and choose an MP3, MP4, or WAV file.
2. **Summarize**: Press the "Summarize" button to transcribe the file and generate a summary.
3. **View Results**: The summarized text will be displayed in the main window.

## Screenshots

### Main Interface
<img width="804" alt="Screenshot 2024-09-09 at 12 48 20 PM" src="https://github.com/user-attachments/assets/13606315-0157-4ff4-a6b7-b0f313ba1bda">


### Contact Us
<img width="399" alt="Screenshot 2024-09-09 at 12 48 32 PM" src="https://github.com/user-attachments/assets/a649fd25-e230-43a9-b904-b87166338a9f">


## File Structure

