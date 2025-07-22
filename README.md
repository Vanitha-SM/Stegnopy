# Steganography Toolkit

A modular command-line application to hide and extract secret messages in images, text, and audio files using LSB and whitespace steganography techniques.

## Features

- **Image Steganography** (PNG, BMP, JPEG)  
  Embed and extract messages by modifying the least significant bits of pixel data.
- **Text Steganography**  
  Hide messages in plain text via single vs. double spaces between words.
- **Audio Steganography** (WAV)  
  Conceal messages in the least significant bits of audio samples.
- **Delimiter-based extraction**  
  Automatically detects end of hidden message using a built-in delimiter.
- **Simple CLI interface**  
  Interactive prompts guide you through hiding or extracting messages.

https://github.com/user-attachments/assets/f54cb0f4-8480-475e-a5e5-70bda7148809



## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/steganography-toolkit.git
   cd steganography-toolkit
   ```

2. **Create and activate a virtual environment** (recommended)  
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main application and follow the prompts:

```bash
python main.py
```

You will see a menu:

```
=== Steganography Toolkit ===
1. Image Steganography
2. Text Steganography
3. Audio Steganography
4. Exit
```

### 1) Image Steganography

- **Hide a message**  
  1. Select option `1`.  
  2. Choose `1` to hide.  
  3. Enter path to cover image (e.g., `samples/test_image.png`).  
  4. Enter your secret message.  
  5. Enter output path (e.g., `output/hidden.png`).  

- **Extract a message**  
  1. Select option `1`.  
  2. Choose `2` to extract.  
  3. Enter path to stego image (`output/hidden.png`).  
  4. Read your hidden message.

### 2) Text Steganography

- **Hide a message**  
  1. Select option `2`.  
  2. Choose `1` to hide.  
  3. Paste or type your cover text.  
  4. Enter your secret message.  
  5. The program outputs the stego text (also saved to `output/stego_text.txt`).

- **Extract a message**  
  1. Select option `2`.  
  2. Choose `2` to extract.  
  3. Paste or type the stego text.  
  4. Read your hidden message.

### 3) Audio Steganography

- **Hide a message**  
  1. Select option `3`.  
  2. Choose `1` to hide.  
  3. Enter path to cover WAV file (`samples/test_audio.wav`).  
  4. Enter your secret message.  
  5. Enter output path (`output/hidden.wav`).

- **Extract a message**  
  1. Select option `3`.  
  2. Choose `2` to extract.  
  3. Enter path to stego WAV file (`output/hidden.wav`).  
  4. Read your hidden message.

## Examples

```bash
# Image hide/extract example
python main.py
# → 1 (Image) → 1 (Hide)
#   cover: samples/test_image.png
#   message: "Secret!"
#   output: output/secret_image.png

python main.py
# → 1 (Image) → 2 (Extract)
#   stego: output/secret_image.png
# → prints "Secret!"
```

## Dependencies

- Pillow  
- NumPy  
- wave (standard library)  
- pydub  

All required packages are listed in `requirements.txt`.


