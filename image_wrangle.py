import re
import os
import sys
import requests
from urllib.parse import urlparse
from pathlib import Path
import hashlib  # Add this to the imports at the top

def convert_to_highres_blogger_url(blogger_url):
    """
    Convert a low-resolution Blogger image URL to its high-resolution version
    by removing the dimension specifications and anything after (e.g., /w400-h278/valueofvehicle.png).
    
    Args:
        blogger_url (str): The low-resolution Blogger image URL
        
    Returns:
        str: The high-resolution version of the URL
    """
    # Split the URL at the dimension pattern
    parts = blogger_url.split('/')
    
    # Find the part that contains dimension specifications (w#-h# format)
    for i, part in enumerate(parts):
        if re.match(r'w\d{2,}-h\d{2,}', part):
            # Remove this part and all parts after it
            parts = parts[:i]
            break
    
    # Rejoin the URL
    return '/'.join(parts)

def process_markdown_file(file_path):
    # Extract the label from the file name
    label = Path(file_path).stem

    # Create the destination directory if it doesn't exist
    dest_dir = Path(f"src/img/{label}")
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Read the markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Updated regular expression to handle both formats
    image_pattern = r'(?:\[!\[([^\]]*)\]\([^)]+\)(?:\{[^}]+\})?\]\(([^)]+)\)(?:\{[^}]+\})?)|(?:!\[([^\]]*)\]\(([^)]+)\))'

    def process_image(match):
        groups = match.groups()
        # Handle nested image pattern [![]()]() - groups[0] and groups[1]
        # Handle simple image pattern ![]() - groups[2] and groups[3]
        alt_text = groups[0] if groups[0] is not None else groups[2]
        url = groups[1] if groups[1] is not None else groups[3]
        
        print(f"\nProcessing image:")
        print(f"Alt text: {alt_text}")
        print(f"URL: {url}")
        
        try:
            if url.startswith("https://blogger.googleusercontent.com/"):
                url = convert_to_highres_blogger_url(url)
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image: {url}. Error: {e}")
            return match.group(0)

        # Generate a filename using URL hash if no filename is present
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            # Create a hash of the URL to use as filename
            url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
            # Use content type from response to determine extension
            content_type = response.headers.get('content-type', '')
            ext = '.jpg'  # default extension
            if 'png' in content_type:
                ext = '.png'
            elif 'gif' in content_type:
                ext = '.gif'
            filename = f'image_{url_hash}{ext}'
        
        local_path = dest_dir / filename

        # Save the image
        with open(local_path, 'wb') as img_file:
            img_file.write(response.content)

        # Create the new image reference
        new_reference = f'![{alt_text}](src/img/{label}/{filename})'
        
        print(f"Processed image: {url} -> {new_reference}")
        return new_reference

    # Process all images in the content
    new_content = re.sub(image_pattern, process_image, content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_mangle.py <markdown_file>")
        sys.exit(1)

    markdown_file = sys.argv[1]
    process_markdown_file(markdown_file)
    print(f"Finished processing {markdown_file}")
