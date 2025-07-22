from PIL import Image
import numpy as np

class ImageSteganography:
    def __init__(self):
        self.delimiter = "###END###"
    
    def message_to_binary(self, message):
        """Convert message to binary string"""
        binary = ''.join(format(ord(char), '08b') for char in message)
        return binary + ''.join(format(ord(char), '08b') for char in self.delimiter)
    
    def binary_to_message(self, binary):
        """Convert binary string back to message"""
        message = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                char = chr(int(byte, 2))
                message += char
                if message.endswith(self.delimiter):
                    return message[:-len(self.delimiter)]
        return message
    
    def hide_message(self, image_path, message, output_path):
        """Hide message in image using LSB steganography"""
        try:
            # Open image
            img = Image.open(image_path)
            img = img.convert('RGB')
            img_array = np.array(img)
            
            # Convert message to binary
            binary_message = self.message_to_binary(message)
            
            # Check if image can hold the message
            total_pixels = img_array.shape[0] * img_array.shape[1]
            if len(binary_message) > total_pixels * 3:
                raise ValueError("Message too long for this image")
            
            # Hide message in LSBs
            binary_index = 0
            for i in range(img_array.shape[0]):
                for j in range(img_array.shape[1]):
                    for k in range(3):  # RGB channels
                        if binary_index < len(binary_message):
                            # Modify LSB
                            img_array[i][j][k] = (img_array[i][j][k] & 0xFE) | int(binary_message[binary_index])
                            binary_index += 1
                        else:
                            break
                    if binary_index >= len(binary_message):
                        break
                if binary_index >= len(binary_message):
                    break
            
            # Save modified image
            result_img = Image.fromarray(img_array)
            result_img.save(output_path)
            
        except Exception as e:
            raise Exception(f"Image steganography error: {e}")
    
    def extract_message(self, image_path):
        """Extract hidden message from image"""
        try:
            # Open image
            img = Image.open(image_path)
            img = img.convert('RGB')
            img_array = np.array(img)
            
            # Extract LSBs
            binary_message = ''
            for i in range(img_array.shape[0]):
                for j in range(img_array.shape[1]):
                    for k in range(3):  # RGB channels
                        binary_message += str(img_array[i][j][k] & 1)
            
            # Convert binary to message
            message = self.binary_to_message(binary_message)
            return message
            
        except Exception as e:
            raise Exception(f"Message extraction error: {e}")
