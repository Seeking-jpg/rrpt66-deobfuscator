import re
import os
import sys


IMPORT_PATTERN = r"(import base64 as \S+; import marshal as \S+; import zlib as \S+; from cryptography.fernet import Fernet)"

def load_obfuscated_file(file_path):
    """Load the obfuscated file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"[ERROR] Failed to load file: {e}")
        return None

def remove_junk_code(file_content):
    """Remove functions that don't contain the required imports."""

    function_pattern = r"(def .+?:)(.*?)(?=def |$)"
    

    functions = re.findall(function_pattern, file_content, re.DOTALL)
    
    functions_to_remove = []
    
    for function_signature, function_body in functions:
        if re.search(IMPORT_PATTERN, function_body):
            continue
        
        # If the function doesn't match the import pattern, mark it for removal
        functions_to_remove.append(function_signature + function_body)
    
    # Remove non-matching functions from the file content
    for junk_func in functions_to_remove:
        file_content = file_content.replace(junk_func, "")
    
    return file_content

def save_cleaned_code(cleaned_code, output_path):
    """Save the cleaned code to a new file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_code)
        print(f"[INFO] Cleaned code saved as: {output_path}")
    except Exception as e:
        print(f"[ERROR] Failed to save cleaned code: {e}")

def main(file_path):
    """Main function to process the obfuscated file."""
    file_content = load_obfuscated_file(file_path)
    
    if file_content is None:
        return

    # Remove junk code
    cleaned_code = remove_junk_code(file_content)

    # Generate a new filename with 'nojung-' prefix
    directory, filename = os.path.split(file_path)
    new_filename = f"nojung-{filename}"
    output_path = os.path.join(directory, new_filename)

    # Save the cleaned code to a new file
    save_cleaned_code(cleaned_code, output_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] Usage: Remove-Junk.py (filename)")
    else:
        file_path = sys.argv[1]
        main(file_path)
