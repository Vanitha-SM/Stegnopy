import os

def create_sample_files():
    """Create sample files for testing"""
    
    # Create sample directories
    os.makedirs('samples', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    # Create sample text
    sample_text = """This is a sample text file for steganography testing. 
    The quick brown fox jumps over the lazy dog. 
    We can hide secret messages in the spacing between these words."""
    
    with open('samples/test_text.txt', 'w') as f:
        f.write(sample_text)
    
    print("Sample files setup complete!")

def validate_file_exists(file_path):
    """Validate if file exists"""
    return os.path.exists(file_path)

def get_file_size(file_path):
    """Get file size in bytes"""
    return os.path.getsize(file_path)
