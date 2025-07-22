import os
import sys
from src.image_stego import ImageSteganography
from src.text_stego import TextSteganography
from src.audio_stego import AudioSteganography

def main():
    print("=== Steganography Toolkit ===")
    print("1. Image Steganography")
    print("2. Text Steganography") 
    print("3. Audio Steganography")
    print("4. Exit")
    
    while True:
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            handle_image_stego()
        elif choice == '2':
            handle_text_stego()
        elif choice == '3':
            handle_audio_stego()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_image_stego():
    img_stego = ImageSteganography()
    
    print("\n--- Image Steganography ---")
    print("1. Hide message")
    print("2. Extract message")
    
    action = input("Choose action (1-2): ").strip()
    
    if action == '1':
        image_path = input("Enter image path: ").strip()
        message = input("Enter message to hide: ").strip()
        output_path = input("Enter output path: ").strip()
        
        try:
            img_stego.hide_message(image_path, message, output_path)
            print(f"Message hidden successfully in {output_path}")
        except Exception as e:
            print(f"Error: {e}")
            
    elif action == '2':
        image_path = input("Enter stego image path: ").strip()
        
        try:
            message = img_stego.extract_message(image_path)
            print(f"Hidden message: {message}")
        except Exception as e:
            print(f"Error: {e}")

def handle_text_stego():
    text_stego = TextSteganography()
    
    print("\n--- Text Steganography ---")
    print("1. Hide message")
    print("2. Extract message")
    
    action = input("Choose action (1-2): ").strip()
    
    if action == '1':
        cover_text = input("Enter cover text: ").strip()
        message = input("Enter message to hide: ").strip()
        
        try:
            stego_text = text_stego.hide_message(cover_text, message)
            print(f"Stego text: {stego_text}")
            
            # Save to file
            with open('output/stego_text.txt', 'w') as f:
                f.write(stego_text)
            print("Stego text saved to output/stego_text.txt")
        except Exception as e:
            print(f"Error: {e}")
            
    elif action == '2':
        stego_text = input("Enter stego text: ").strip()
        
        try:
            message = text_stego.extract_message(stego_text)
            print(f"Hidden message: {message}")
        except Exception as e:
            print(f"Error: {e}")

def handle_audio_stego():
    audio_stego = AudioSteganography()
    
    print("\n--- Audio Steganography ---")
    print("1. Hide message")
    print("2. Extract message")
    
    action = input("Choose action (1-2): ").strip()
    
    if action == '1':
        audio_path = input("Enter audio file path (.wav): ").strip()
        message = input("Enter message to hide: ").strip()
        output_path = input("Enter output path: ").strip()
        
        try:
            audio_stego.hide_message(audio_path, message, output_path)
            print(f"Message hidden successfully in {output_path}")
        except Exception as e:
            print(f"Error: {e}")
            
    elif action == '2':
        audio_path = input("Enter stego audio path: ").strip()
        
        try:
            message = audio_stego.extract_message(audio_path)
            print(f"Hidden message: {message}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
