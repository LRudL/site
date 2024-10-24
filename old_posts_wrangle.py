import sys
import re

def process_file(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Process the lines
    processed_lines = []
    for line in lines:
        line = line.rstrip()  # Remove trailing whitespace
        
        # Check if line is a markdown bullet point
        is_bullet = bool(re.match(r'^\s*- ', line))
        
        # Check if line is a bold text header (e.g., "**Some Header**")
        header_match = re.match(r'^\s*\*\*([^*]+)\*\*\s*$', line)
        
        if header_match:
            # Convert **text** to ## text
            processed_lines.append(f"## {header_match.group(1)}")
        else:
            processed_lines.append(line)
        
        # Add extra linebreak unless it's a bullet point
        if not is_bullet:
            processed_lines.append('')

    # Write back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(processed_lines))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python old_posts_wrangle.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    process_file(file_path)

