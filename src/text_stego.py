class TextSteganography:
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
                char = chr(int(byte, 2))
                message += char
                if message.endswith(self.delimiter):
                    return message[:-len(self.delimiter)]
        return message
    
    def hide_message(self, cover_text, secret_message):
        """Hide message using whitespace steganography"""
        try:
            binary_message = self.message_to_binary(secret_message)
            
            # Split cover text into words
            words = cover_text.split()
            
            if len(binary_message) > len(words) - 1:
                raise ValueError("Message too long for cover text")
            
            # Hide binary in spaces between words
            result = words[0]
            binary_index = 0
            
            for i in range(1, len(words)):
                if binary_index < len(binary_message):
                    if binary_message[binary_index] == '1':
                        # Double space for binary 1
                        result += "  " + words[i]
                    else:
                        # Single space for binary 0
                        result += " " + words[i]
                    binary_index += 1
                else:
                    result += " " + words[i]
            
            return result
            
        except Exception as e:
            raise Exception(f"Text steganography error: {e}")
    
    def extract_message(self, stego_text):
        """Extract hidden message from text"""
        try:
            # Analyze spacing between words
            binary_message = ''
            i = 0
            
            while i < len(stego_text):
                if stego_text[i] == ' ':
                    space_count = 0
                    while i < len(stego_text) and stego_text[i] == ' ':
                        space_count += 1
                        i += 1
                    
                    if space_count == 1:
                        binary_message += '0'
                    elif space_count == 2:
                        binary_message += '1'
                else:
                    i += 1
            
            # Convert binary to message
            message = self.binary_to_message(binary_message)
            return message
            
        except Exception as e:
            raise Exception(f"Message extraction error: {e}")
