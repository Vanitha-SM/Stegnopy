import wave
import numpy as np

class AudioSteganography:
    def __init__(self):
        self.delimiter = "###END###"
    
    def message_to_binary(self, message):
        """Convert message to binary"""
        binary = ''.join(format(ord(char), '08b') for char in message)
        delimiter_binary = ''.join(format(ord(char), '08b') for char in self.delimiter)
        return binary + delimiter_binary
    
    def binary_to_message(self, binary):
        """Convert binary to message"""
        message = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                try:
                    char = chr(int(byte, 2))
                    message += char
                    if message.endswith(self.delimiter):
                        return message[:-len(self.delimiter)]
                except ValueError:
                    continue
        return message
    
    def hide_message(self, audio_path, message, output_path):
        """Hide message in audio using LSB steganography"""
        try:
            # Open audio file
            with wave.open(audio_path, 'rb') as audio:
                frames = audio.readframes(-1)
                audio_data = np.frombuffer(frames, dtype=np.int16)
                params = audio.getparams()
            
            # Convert message to binary
            binary_message = self.message_to_binary(message)
            
            # Check if audio can hold the message
            if len(binary_message) > len(audio_data):
                raise ValueError("Message too long for this audio file")
            
            # Modify LSBs
            modified_data = audio_data.copy()
            for i in range(len(binary_message)):
                # Modify LSB of audio sample
                if binary_message[i] == '1':
                    modified_data[i] = modified_data[i] | 1
                else:
                    modified_data[i] = modified_data[i] & ~1
            
            # Save modified audio
            with wave.open(output_path, 'wb') as output_audio:
                output_audio.setparams(params)
                output_audio.writeframes(modified_data.tobytes())
                
        except Exception as e:
            raise Exception(f"Audio steganography error: {e}")
    
    def extract_message(self, audio_path):
        """Extract hidden message from audio"""
        try:
            # Open audio file
            with wave.open(audio_path, 'rb') as audio:
                frames = audio.readframes(-1)
                audio_data = np.frombuffer(frames, dtype=np.int16)
            
            # Extract LSBs
            binary_message = ''
            for sample in audio_data:
                binary_message += str(sample & 1)
                # Stop when we find the delimiter
                if len(binary_message) >= 8 and len(binary_message) % 8 == 0:
                    temp_message = self.binary_to_message(binary_message)
                    if temp_message.endswith(self.delimiter.replace(self.delimiter, "")):
                        break
            
            # Convert binary to message
            message = self.binary_to_message(binary_message)
            return message
            
        except Exception as e:
            raise Exception(f"Message extraction error: {e}")
