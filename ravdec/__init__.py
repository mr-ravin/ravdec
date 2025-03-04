import os

__version__ = '3.3'

def check_compressability(ascii_value, read_char):
    """Ensure the character is within ASCII 0-127 range."""
    if ascii_value > 127:
        raise Exception(f"Not Compressible for character: {read_char} - Acceptable ASCII range: 0-127.")

def check_data_length_threshold(enforced_8char_input, read_data):
    """Ensure at least 24 characters are present in read_data when enforced_8char_input is set to False."""
    if not enforced_8char_input and len(read_data) < 24:
        raise Exception("Minimum 24 characters should be present when enforced_8char_input is set to False.")

def get7BitBinaryRepresentation(read_data, bit_length=8):
    """Compress text by converting each character into 7-bit representation."""
    full_binary_data = ''
    
    for character in read_data:
        ascii_value = ord(character)
        check_compressability(ascii_value, character)
        
        # Convert to binary, remove MSB (7-bit storage)
        binary_data = bin(ascii_value)[2:].zfill(bit_length)[1:]
        full_binary_data += binary_data

    return full_binary_data

def binaryToCompressedText(binary_data, bit_length=8):
    """Convert 7-bit binary stream into 8-bit ASCII characters for storage."""
    compressed_text = ""
    
    for i in range(0, len(binary_data), bit_length):
        byte = binary_data[i:i + bit_length]  # Take 8-bit chunk
        compressed_text += chr(int(byte, 2))  # Convert to character

    return compressed_text

def compressedTextToBinary(compressed_text, bit_length=8):
    """Convert stored 8-bit ASCII characters back into a 7-bit binary stream."""
    binary_data = ""
    
    for char in compressed_text:
        binary_data += bin(ord(char))[2:].zfill(bit_length)  # Convert each char to 8-bit binary
    
    return binary_data

def getTextFrom7BitBinaryRepresentation(full_binary_data, bit7_length=7):
    """Decompress 7-bit binary data back into the original text."""
    original_text = ""

    for i in range(0, len(full_binary_data), bit7_length):
        binary7bit_data = full_binary_data[i:i + bit7_length]

        # Ignore incomplete bits at the end
        if len(binary7bit_data) < bit7_length:
            break

        binary8bit_data = '0' + binary7bit_data  # Restore the missing MSB
        original_text += chr(int(binary8bit_data, 2))

    return original_text

def compression(read_data, bit_length=8, key="text", enforced_8char_input=False):
    """Compresses text using 7-bit storage."""
    if not read_data:
        return read_data
    
    check_data_length_threshold(enforced_8char_input, read_data)

    binary_string = get7BitBinaryRepresentation(read_data)

    if not enforced_8char_input:
        # Calculate padding size to make it a multiple of 8 bits
        pad_length = (bit_length - (len(binary_string) % bit_length)) % bit_length
        binary_string += "0" * pad_length  # Append padding
        compressed_text = f"{pad_length}#{binaryToCompressedText(binary_string)}"  # Store pad length
    else:
        compressed_text = binaryToCompressedText(binary_string)  # No padding indicator

    if key == "binary":
        return binary_string
    return compressed_text

def decompression(compressed_text, key="text", enforced_8char_input=False):
    """Decompresses text back to its original form."""
    if not compressed_text:
        return compressed_text

    pad_length = 0
    if not enforced_8char_input and compressed_text[1] == "#":
        try:
            pad_length, compressed_text = compressed_text.split("#", 1)
            pad_length = int(pad_length)
        except ValueError:
            raise Exception("Corrupted compressed data format.")

    binary_string = compressedTextToBinary(compressed_text)

    # Remove the padding bits
    if pad_length > 0 and pad_length < len(binary_string):
        binary_string = binary_string[:-pad_length]

    if key == "binary":
        return binary_string

    original_text = getTextFrom7BitBinaryRepresentation(binary_string)
    return original_text

def file_compression(filename, enforced_8char_input=False):
    """Compress a text file and save the compressed data."""
    with open(filename, 'r', encoding="utf-8") as read_file:
        read_data = read_file.read()
    
    compressed_text = compression(read_data, enforced_8char_input=enforced_8char_input)
    write_fname = filename + '.rdc'
    
    with open(write_fname, 'w', encoding="utf-8") as bin_file:
        bin_file.write(compressed_text)

def file_decompression(filename, enforced_8char_input=False):
    """Decompress a previously compressed file."""
    with open(filename, 'r', encoding="utf-8") as read_file:
        read_data = read_file.read()
    
    decompressed_text = decompression(read_data, enforced_8char_input=enforced_8char_input)

    base_name, ext = os.path.splitext(filename)
    write_fname = f"{base_name}_decompressed{ext}" if ext != ".rdc" else base_name

    with open(write_fname, 'w', encoding="utf-8") as bin_file:
        bin_file.write(decompressed_text)
