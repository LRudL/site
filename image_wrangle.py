import re
import os
import sys
import requests
from urllib.parse import urlparse
from pathlib import Path

def process_markdown_file(file_path):
    # Extract the label from the file name
    label = Path(file_path).stem

    # Create the destination directory if it doesn't exist
    dest_dir = Path(f"src/img/{label}")
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Read the markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Updated regular expression to find image links
    image_pattern = r'\[!\[([^\]]*)\]\([^)]+\)(?:\{[^}]+\})?\]\(([^)]+)\)(?:\{[^}]+\})?'

    def process_image(match):
        alt_text, url = match.groups()
        
        # Download the image
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image: {url}. Error: {e}")
            return match.group(0)

        # Generate a filename for the downloaded image
        filename = os.path.basename(urlparse(url).path)
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
